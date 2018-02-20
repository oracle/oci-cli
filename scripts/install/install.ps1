# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

<#
.DESCRIPTION
    Installs the Oracle Cloud Infrastructure CLI.
.PARAMETER AcceptAllDefaults
    Run the script accepting all default options. This will suppress all prompts for user input.
    
    Default options:
    - Install required version of Python if not already installed (to $env:USERPROFILE\Python)
    - Create virtualenv in $env:USERPROFILE\lib\oracle-cli
    - Upgrade / replace any current installation in $env:USERPROFILE\lib\oracle-cli
    - Place oci executable in $env:USERPROFILE\bin
    - Add $env:USERPROFILE\bin to PATH
#>

[CmdletBinding()]
Param(
    [switch]$AcceptAllDefaults
)

$OriginalErrorActionPreference = $ErrorActionPreference

# Explicitly support TLS 1.2 only if OS supports it
if ([System.Enum]::GetNames('System.Net.SecurityProtocolType') -Contains 'Tls12') {
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Ssl3,Tls,Tls11,Tls12';
}

$PythonInstallScriptUrl = "https://raw.githubusercontent.com/oracle/oci-cli/v2.4.13/scripts/install/install.py"
$PythonVersionToInstall = "3.6.2"    # version of Python to install if none exists
$MinValidPython2Version = "2.7.5"    # minimum required version of Python 2 on system
$MinValidPython3Version = "3.5.0"    # minimum required version of Python 3 on system

function LogOutput($Output) {
    Write-Verbose $Output
    Write-Progress -Activity $Output -Status 'In progress...'
}

function VersionMeetsMinimumRequirements($Version, $MinVersion) {
    $Version = $Version.split('.')
    $MinVersion = $MinVersion.split('.')

    For ($i=0; $i -le $Version.Length; $i++) {
        # if we have reached the end of the MinVersion and we still have digits on the system version then the version is sufficient
        if ($i -ge $MinVersion.Length) {
            return $true
        }

        # loop from most significant to least significant digits in version
        # if Version digit is ever greater than MinVersion, then version is sufficient
        # if Version digit is ever less than MinVersion, the version is not sufficient
        # if they are equal, we will continue to check less significant digits
        if ($Version[$i] -gt $MinVersion[$i]) {
            return $true
        }
        elseif ($Version[$i] -lt $MinVersion[$i]) {
            return $false
        }
    }

    return $true
}

function VerifyPythonExecutableMeetsMinimumRequirements {
    Param (
        [Parameter(Mandatory=$true)]
        [AllowEmptyString()]
        [string]$PythonExecutable
    )

    if (-Not $PythonExecutable -Or (-Not (Test-Path $PythonExecutable))) {
        return $false
    }

    # need to escape spaces in the path for Invoke-Expression
    $EscapedExecutable = $PythonExecutable -replace ' ','` '
    $PythonVersion = Invoke-Expression "$EscapedExecutable -c 'import platform;print(platform.python_version())'"
    $MinVersionToCheck = $MinValidPython2Version
    if ($PythonVersion.StartsWith("3")) {
        $MinVersionToCheck = $MinValidPython3Version
    }

    if (VersionMeetsMinimumRequirements $PythonVersion $MinVersionToCheck) {
        return $true
    }
    
    LogOutput "$PythonExecutable Python version $PythonVersion is below minimum required version $MinVersionToCheck"
    return $false
}

#  Finds the most recent version of Python installed in the registry and returns 
#  the path for python.exe for that install (or $null if no install exists).
#  Documentation on the registry structure: https://www.python.org/dev/peps/pep-0514/
function FindLatestPythonExecutableInRegistry {
    Param(
        [Parameter(Mandatory=$true)]
        [string]$RootRegistryLocation
    )

    $PythonExecutable = $null
    $PythonCoreRegistryLocation = "${RootRegistryLocation}:\Software\Python\PythonCore"
    if (Test-Path $PythonCoreRegistryLocation) {
        LogOutput "Python found in registry: $PythonCoreRegistryLocation"
        $PythonInstallations = (Get-ChildItem -recurse $PythonCoreRegistryLocation) | Sort-Object -Descending
        if ($PythonInstallations) {
           ForEach ($Installation in $PythonInstallations) {
               # we are sorting by descending so this will grab the greatest installed version of python
               If ($installation.Name.EndsWith("\InstallPath")) {
                   $PythonInstallLocation = (Get-ItemProperty -LiteralPath $Installation.PSPath).'(default)'
                   return Join-Path $PythonInstallLocation "python.exe"
               }
           }
        }  
    }

    return $PythonExecutable
}

function DownloadFile($Uri, $OutFile) {
    # PowerShell V2 doesn't support Invoke-WebRequest so use WebClient
    # Use Invoke-WebRequest on versions that support it since it writes progress
    if ($PsVersionTable.PsVersion.Major > 2) {
        Invoke-WebRequest -Uri $Uri -OutFile $OutFile -UseBasicParsing
    }
    else {
        (New-Object System.Net.WebClient).DownloadFile($Uri, $OutFile)
    } 
}

function DownloadAndRunPythonExeInstaller($InstallDir, $Version) {
    LogOutput "Downloading Python..."

    # Download python executable installer
    $PythonInstallerUrl = "https://www.python.org/ftp/python/$Version/python-$Version.exe"
    $PythonInstallerExe = [System.IO.Path]::GetTempFileName() + ".exe"

    # IntPtrSize == 8 on 64 bit machines
    $IntPtrSize = Invoke-Expression [IntPtr]::Size
    if ($IntPtrSize -eq 8) {
        $PythonInstallerUrl = "https://www.python.org/ftp/python/$Version/python-$Version-amd64.exe"
    }

    DownloadFile -Uri $PythonInstallerUrl -OutFile $PythonInstallerExe

    LogOutput "Download Complete! Installer executable written to: $PythonInstallerExe"

    LogOutput "Installing Python to $InstallDir..."

    # Do a 'passive' install of Python which will not require any user interaction but will pop up a progress window
    # Options documented here: https://docs.python.org/3/using/windows.html#installing-without-ui
    $Args = "/passive PrependPath=0 Include_test=0 Include_tcltk=0 Include_launcher=0 Include_symbols=0 DefaultJustForMeTargetDir=" + $InstallDir
    $Process = Start-Process -FilePath $PythonInstallerExe -ArgumentList $Args -Wait -PassThru
    if ($Process.ExitCode -ne 0) {
        Write-Error "Failed to install Python. On some systems installing Python can require running the script as an Administrator. More detailed information can be found in the Python installation logs in $env:LOCALAPPDATA\Temp"
    }

    LogOutput "Successfully installed Python!"
}

function DownloadAndRunPythonMsiInstaller($InstallDir, $Version) {

    LogOutput "Downloading Python..."

    # Download python executable installer
    $PythonInstallerUrl = "https://www.python.org/ftp/python/$Version/python-$Version.msi"
    $PythonInstallerMsi = [System.IO.Path]::GetTempFileName() + ".msi"

    # IntPtrSize == 8 on 64 bit machines
    $IntPtrSize = Invoke-Expression [IntPtr]::Size
    if ($IntPtrSize -eq 8) {
        $PythonInstallerUrl = "https://www.python.org/ftp/python/$Version/python-$Version.amd64.msi"
    }

    DownloadFile -Uri $PythonInstallerUrl -OutFile $PythonInstallerMsi

    LogOutput "Download Complete! Installer MSI written to: $PythonInstallerMsi"

    LogOutput "Installing Python to $InstallDir..."

    $InstallDir = (Get-ChildItem Env:\USERPROFILE).Value + "\Python\"
    $DataStamp = get-date -Format yyyyMMddTHHmmss
    $logFile = '{0}-{1}.log' -f $PythonInstallerMsi,$DataStamp

    # documentation: https://www.python.org/download/releases/2.4/msi/
    $MSIArguments = @(
        "/i"
        ('"{0}"' -f $PythonInstallerMsi)
        "/qr"
        "/norestart"
        "/L*v"
        $logFile
        "TARGETDIR=`"$InstallDir`""
    )

    $Process = Start-Process "msiexec.exe" -ArgumentList $MSIArguments -Wait -NoNewWindow -PassThru
    if ($Process.ExitCode -ne 0) {
        Write-Error "Failed to install Python. On some systems installing Python can require running the script as an Administrator. More detailed information can be found in the Python installation log: $logFile"
    }

    LogOutput "Successfully installed Python!"
}

Try {
    # ensure that the script stops executing if any errors are encountered so we don't get in a weird state
    $ErrorActionPreference = "Stop"

    # check if Python is installed, and is greater than MinValidPythonVersion
    $PythonExecutable = $null
    $CurrentUserPythonExecutable = FindLatestPythonExecutableInRegistry "HKCU"
    $LocalMachinePythonExecutable = FindLatestPythonExecutableInRegistry "HKLM"

    # if python is installed in the registry but the corresponding python.exe doesn't exist
    # then the user will need to repair or uninstall python and re-run the script
    $PythonInstallationCorruptErrorMessage = "Error: Python executable referenced in registry does not exist. Uninstall or repair your Python installation manually and then re-run this script."
    $CurrentUserPythonInstallationExeMissing = $LocalMachinePythonExecutable -And (-Not (Test-Path $LocalMachinePythonExecutable))
    $LocalMachinePythonInstallationExeMissing = $CurrentUserPythonExecutable -And (-Not (Test-Path $CurrentUserPythonExecutable))
    If ($CurrentUserPythonInstallationExeMissing -Or $LocalMachinePythonInstallationExeMissing) {
        Write-Error $PythonInstallationCorruptErrorMessage
    }

    If (VerifyPythonExecutableMeetsMinimumRequirements -PythonExecutable $LocalMachinePythonExecutable) {
        $PythonExecutable = $LocalMachinePythonExecutable
    }
    ElseIf (VerifyPythonExecutableMeetsMinimumRequirements -PythonExecutable $CurrentUserPythonExecutable) {
        $PythonExecutable = $CurrentUserPythonExecutable
    }
    Else {
        LogOutput "No valid Python installation found."

        if (-Not $AcceptAllDefaults) {
            $message  = 'Python is required to run the CLI.'
            $question = 'Install Python now? (Entering "n" will exit the installation script)'

            $choices = New-Object Collections.ObjectModel.Collection[Management.Automation.Host.ChoiceDescription]
            $choices.Add((New-Object Management.Automation.Host.ChoiceDescription -ArgumentList '&Yes'))
            $choices.Add((New-Object Management.Automation.Host.ChoiceDescription -ArgumentList '&No'))

            $decision = $Host.UI.PromptForChoice($message, $question, $choices, 0)
            if ($decision -eq 1) {
                LogOutput 'Exiting script. Please re-run and elect to install Python or install Python manually and re-run.'
                Exit 1
            }
        }

        # (e.g. C:\Users\{USER}\Python\)
        $InstallDir = (Get-ChildItem Env:\USERPROFILE).Value + "\Python\"

        # use MSI installer for python 2.7.x on Windows Server 2008 SP 0
        $OsInfo = Get-WMIObject Win32_OperatingSystem -ComputerName $env:COMPUTERNAME
        if ($OsInfo.Caption.Contains('Windows Server 2008') -And $OsInfo.ServicePackMajorVersion -eq 0) {
            DownloadAndRunPythonMsiInstaller -InstallDir $InstallDir -Version "2.7.14"
        }
        else {
            DownloadAndRunPythonExeInstaller -InstallDir $InstallDir -Version $PythonVersionToInstall
        }

        $PythonExecutable = Join-Path $InstallDir 'python.exe'
    }

    # Once python is installed, execute the CLI install script
    $PythonInstallScriptPath = [System.IO.Path]::GetTempFileName()
    LogOutput "Downloading install script to $PythonInstallScriptPath"
    DownloadFile -Uri $PythonInstallScriptUrl -OutFile $PythonInstallScriptPath
    $ArgumentList = $PythonInstallScriptPath
    if ($AcceptAllDefaults) {
        $ArgumentList = "$ArgumentList --accept-all-defaults"
    }

    LogOutput "Using Python executable: $PythonExecutable to run install script..."

    $Process = Start-Process -FilePath $PythonExecutable -ArgumentList $ArgumentList -Wait -NoNewWindow -PassThru
    if ($Process.ExitCode -ne 0) {
        Write-Error "Executing $PythonExecutable $ArgumentList returned a non-zero exit code."
    }

    # install.py will only update the USER PATH in the registry, so if the user tries to invoke 'oci' immediately it will fail
    # therefore, we explicitly reload the USER PATH environment variable which will contain the path to 'oci' if the user allowed it
    # Note: this logic will only work if the script was invoked directly and not by spawning a separate powershell process
    $OldPath = [Environment]::GetEnvironmentVariable("PATH", "PROCESS")
    $UserPath = [Environment]::GetEnvironmentVariable("PATH", "USER")
    $NewPath = ("$UserPath;$OldPath" -split ';' | Select-Object -Unique) -join ';'
    [Environment]::SetEnvironmentVariable("PATH", "$NewPath", "PROCESS")

    LogOutput "Successfully installed OCI CLI!"
}
Finally {
    # we dont want to impact user's preference outside of this script
    $ErrorActionPreference = $OriginalErrorActionPreference
}
