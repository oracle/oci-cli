===================
Installation issues
===================

* Error "Could not download Oracle Cloud Infrastructure CLI install script"
  Usually happens when curl is not working, Please try the following:

  * Make sure you have internet connection
  * Make sure there is no proxy issue

* Error "Python is not working correctly":
  Usually happens when python path is not setup correctly, Please try the following

  * If you have python installed, please make sure its path is setup correctly
  * Run "python --version" or "python3 --version" and make sure the version is correct

===========================
Offline Installation issues
===========================

* Ubuntu

  * Error "System was unable to use venv, Please make sure Python3 venv is installed."

    * To fix the above error, please install the package "python3-venv" in the System and try the installation again

  * Error "command 'x86_64-linux-gnu-gcc' failed with exit status 1"

    * To fix the above error, please install the packages python3-dev, gcc and libssl-dev in the System and try the installation again

* Oracle Linux, CentOS

  * Error "command 'gcc' failed with exit status 1"

    * To fix the above error, please install the packages gcc, zlib-devel, python3-devel and OpenSSL 1.1.1-latest in the System and try the installation again

================
Troubleshooting
================

* Error: Got unexpected extra arguments, can be caused by one of the following reasons

  * You are passing an extra argument to one of the parameters
  * One of the parameters has an invalid value

* Service Errors

  * Any operation resulting in a service error causes an error of type "ServiceError" to be returned by the CLI. See `API Errors <https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#API_Errors>`__
