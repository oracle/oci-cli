# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

$ociTopLevelCommands = @()
$ociSubcommands = @{}
$ociCommandsToLongParams = @{}
$ociCommandsToShortParams = @{}

$PSScriptRoot = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
$slash = [IO.Path]::DirectorySeparatorChar
$FolderPath = $PSScriptRoot
$Dir = get-childitem $FolderPath
$FileList = $Dir | where {$_.extension -eq ".psm1"}
ForEach ($file in $FileList) {
    $module = $FolderPath + $slash + $file.name
    Import-Module -Name $module
    $suffix = [io.path]::GetFileNameWithoutExtension($file.name)
    $suffix = $suffix.replace("-","_") 
    $ociTopLevelCommand = & "GetOciTopLevelCommand_$suffix"
    $newOciSubCommands = & "GetOciSubcommands_$suffix"
    $newOciCommandsToLongParams = & "GetOciCommandsToLongParams_$suffix"
    $newOciCommandsToShortParams = & "GetOciCommandsToShortParams_$suffix"

    $ociTopLevelCommands += $ociTopLevelCommand
    $ociSubcommands += $newOciSubCommands
    $ociCommandsToLongParams += $newOciCommandsToLongParams
    $ociCommandsToShortParams += $newOciCommandsToShortParams
}

$script:ociSubcommandKeys = $ociSubcommands.Keys -join '|'
$script:ociCommandsWithLongParams = $ociCommandsToLongParams.Keys -join '|'
$script:ociCommandsWithShortParams = $ociCommandsToShortParams.Keys -join '|'

function OciTabExpansion($lastBlock) {
    $res = Oci-Invoke-Utf8ConsoleCommand { OciTabExpansionInternal $lastBlock }
	$res
}

function OciTabExpansionInternal($lastBlock) {
	$ociAliasPattern = GetOciAliasPattern 
	
	switch -regex ($lastBlock -replace "^$($ociAliasPattern) ","") {
		# Handles [oci] <top-level command>
		"^(?<cmd>\w+?)$" {
            $com = $matches['cmd']
			$ociTopLevelCommands | Where-Object { $_ -like "$com*" }
		}
	
		# Handles [oci] <top-level command> <sub-command> <sub-command> ...
        "^(?<cmd>$ociSubcommandKeys)\s+(?<op>\S*)$" {
            ociCmdOperations $ociSubcommands $matches['cmd'] $matches['op']
        }
		
		# Handles [oci] <some level of commands> --<param>
        "^(?<cmd>$ociCommandsWithLongParams).* --(?<param>\S*)$" {
            expandOciLongParams $matches['cmd'] $matches['param']
        }

        # Handles [oci] <some level of commands> -<shortparam>
        "^(?<cmd>$ociCommandsWithShortParams).* -(?<shortparam>\S*)$" {
            expandOciShortParams $matches['cmd'] $matches['shortparam']
        }
	}
}

function script:ociCmdOperations($commands, $command, $filter) {
    $commands.$command -split ' ' | Where-Object { $_ -like "$filter*" }
}

function script:expandOciLongParams($cmd, $filter) {
    $ociCommandsToLongParams[$cmd] -split ' ' |
        Where-Object { $_ -like "$filter*" } |
        Sort-Object |
        ForEach-Object { -join ("--", $_) }
}

function script:expandOciShortParams($cmd, $filter) {
    $ociCommandsToShortParams[$cmd] -split ' ' |
        Where-Object { $_ -like "$filter*" } |
        Sort-Object |
        ForEach-Object { -join ("-", $_) }
}

function GetOciAliasPattern() {
	$ociAliases = @("oci") + @(Get-Alias | where { $_.Definition -eq "oci" } | select -Exp Name)
	$ociAliasPattern = "($($ociAliases -join '|'))"
	
	return $ociAliasPattern
}

function Oci-Invoke-Utf8ConsoleCommand([ScriptBlock]$cmd) {
    $currentEncoding = [Console]::OutputEncoding
    $errorCount = $global:Error.Count
    try {
        # A native executable that writes to stderr AND has its stderr redirected will generate non-terminating
        # error records if the user has set $ErrorActionPreference to Stop. Override that value in this scope.
        $ErrorActionPreference = 'Continue'
        if ($currentEncoding.IsSingleByte) {
            [Console]::OutputEncoding = [Text.Encoding]::UTF8
        }
        & $cmd
    }
    finally {
        if ($currentEncoding.IsSingleByte) {
            [Console]::OutputEncoding = $currentEncoding
        }

        # Clear out stderr output that was added to the $Error collection, putting those errors in a module variable
        if ($global:Error.Count -gt $errorCount) {
            $numNewErrors = $global:Error.Count - $errorCount
            $invokeErrors.InsertRange(0, $global:Error.GetRange(0, $numNewErrors))
            if ($invokeErrors.Count -gt 256) {
                $invokeErrors.RemoveRange(256, ($invokeErrors.Count - 256))
            }
            $global:Error.RemoveRange(0, $numNewErrors)
        }
    }
}

if (Test-Path Function:\TabExpansion) {
    Rename-Item Function:\TabExpansion TabExpansionBackupFromOciAutocomplete
}

function TabExpansion($line, $lastWord) {
    $lastBlock = [regex]::Split($line, '[|;]')[-1].TrimStart()

	$ociAliasPattern = GetOciAliasPattern
	
	switch -regex ($lastBlock) {
        # Execute OCI tab completion
        "^$($ociAliasPattern) (.*)" { OciTabExpansion $lastBlock }

        # Fall back on existing tab expansion
        default {
            if (Test-Path Function:\TabExpansionBackupFromOciAutocomplete) {
                TabExpansionBackupFromOciAutocomplete $line $lastWord
            }
        }
    }
}