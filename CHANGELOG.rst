==========
Change Log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <http://keepachangelog.com/>`__.

2.4.16 - 2018-02-08
---------------------
Added
~~~~~~~~~~
* Support for Domain Name System Service (oci dns)
    * An example on using the Domain Name System Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/dns_example.sh>`_.
* Support for Reserved Public IPs in Virtual Networking Service (oci network public-ip)
* Support for the following features in Block Storage Service
    * Automated and policy-based scheduled backups (oci bv volume-backup-policy | volume-backup-policy-assignment)
    * Read-only volume attachments (--is-read-only option while attaching volume)
    * Incremental backups (--type option while creating a volume backup)

2.4.15 - 2018-01-25
---------------------
Added
~~~~~~~~~~
* Support for using the ``ObjectReadWithoutList`` public access type when creating and updating buckets
* Support for managing dynamic groups (oci iam dynamic-group)
* Support for instance principal auth (using --auth instance_principal option)

2.4.14 - 2018-01-11
--------------------
Added
~~~~~~~~~~
* Support for tagging

  * Tags and tag namespaces can be managed via the 'oci iam tag-namespace' and 'oci iam tag' commands
  * Operations which support applying tags will have --defined-tags and --freeform-tags options. Check the help dump (https://github.com/oracle/oci-cli/blob/master/tests/output/inline_help_dump.txt) for resources which support tags. A general list of taggable resources can also be found in: https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Taggable
  * An example of using tagging can be found at https://github.com/oracle/oci-cli/blob/master/scripts/tagging_example.sh

* Support for bringing your own custom image for emulation mode virtual machines in Compute Service (--launch-mode parameter on create image)
* Support for returning unquoted strings when the result of a JMESPath --query is a single string value (using --raw-output option)
* Support for launching an instance from an image or boot volume using the --image-id or --source-boot-volume-id parameters (these are alternatives to specifying --source-details)
* Support for boot volume attachment operations (oci compute boot-volume-attachment)
* Support wait for state on detach operations (e.g. oci compute volume-attachment detach --wait-for-state)

Changed
~~~~~~~~~~
* Upgraded cryptography dependency to 2.1.3

  * Changed dependency on pyOpenSSL <= 17.4.0 as the minimum cryptography version for pyOpenSSL 17.5.0 is 2.1.4

* Upgraded six dependency to 1.11.0
* Ugraded requests dependency to 2.18.4


2.4.13 - 2017-12-11
--------------------
Added
~~~~~~~~~~
* Support for Load Balancing Service operations ('oci lb')

  * An example of creating a load balancer can be found a https://github.com/oracle/oci-cli/blob/master/scripts/create_load_balancer.sh

* Support for user managed boot volumes: 'oci bv boot-volume', 'oci compute instance launch --source-details', 'oci compute instance terminate --preserve-boot-volume'
* Operations which create, update or delete resources with a lifecycle-state now support a --wait-for-state option which allows you to perform the action and then wait until the resource reaches a given state
* Support for specifying --profile option through OCI_CLI_PROFILE environment variable

Changed
~~~~~~~~~~
* When listing audit events ('oci audit event list'), audit events can now have a 'response-payload' attribute which contains metadata of interest. For example, the OCID of a resource

2.4.12 - 2017-11-27
-------------------

Added
~~~~~~~~~~
* Support option for using second physical NIC on X7 Bare Metal instances (--nic-index option on 'oci compute instance attach-vnic')
* Support for Local Peering Gateway operations ('oci network local-peering-gateway')
* Support for specifying a default for the --profile option in the oci_cli_rc file
* Support create database from backup (oci db database create-from-backup)
* Support for getting archived object restore status ('oci os object restore-status') more details in sample (https://github.com/oracle/oci-cli/scripts/restore_archived_object.sh)

Changed
~~~~~~~~~~
* Help displayed via the --help/-h/-? option is now formatted like man pages found on Unix (or Unix-like) systems. To switch back to the previous way of displaying help, add `use_click_help = True` to the `OCI_CLI_SETTINGS` section of your oci_cli_rc file

2.4.11 - 2017-11-02
-------------------

Added
~~~~~~~~~~
* 'oci setup oci-cli-rc' command to generate an oci_cli_rc file with default aliases and pre-defined queries
* Support for defining named JMESPath queries and command / parameter aliases in oci_cli_rc file
* 'oci setup repair-file-permissions' command to set appropriate file permissions on key / config files. Warnings are emitted if permissions are too open on these files.
* Support for --all parameter for 'list' operations to return all items in a list without manual pagination
* Support for audit operations: 'oci audit'
* Support for archive storage tier, object rename and namespace metadata in Object Storage
* Support for fast clones of volumes in Block Storage service
* Support for backup and restore in Database service
* Support for sorting and filtering in list APIs in Core Services
* Support for multipart download for 'oci os object get' and 'oci os object bulk-get'

Deprecated
~~~~~~~~~~~
* The top level parameter --defaults-file has been renamed to --oci-cli-rc and the default location for the file has moved from ~/.oci/cli-defaults to ~/.oci/oci_cli_rc.

Changed
~~~~~~~~~~
* Upgraded cryptography dependency to 1.9.
* Minimum version of Mac OS supported is now 10.8

2.4.10 - 2017-10-12
-------------------

Added
~~~~~~~~~~
* Support for new Database service operations: VM DBs, Bring Your Own License, and Data Guard.
* Support for autocomplete on Windows (PowerShell only)
* Support for defaults file to specify default values for CLI parameters (https://github.com/oracle/oci-cli/issues/20)
* Support for parallelization in bulk object storage commands: bulk upload / download / delete).
* Support for including / excluding files in bulk upload / download / delete based on file patterns.
* Support for enabling / disabling VNIC source/destination checks (https://github.com/oracle/oci-cli/issues/15)
* Support for adding and updating display names for captured instance serial console data.
* Display public key fingerprint in output of 'oci setup config' (https://github.com/oracle/oci-cli/issues/18)
* Support for table output using --output table
* Support for JMESPath queries using --query parameter

Fixed
~~~~~~~~~~
* Allow piping input through STDIN for 'oci os object put' (https://github.com/oracle/oci-cli/issues/21)
* Use full path when writing 'key_file' in 'oci setup config' (https://github.com/oracle/oci-cli/issues/19)
* Added missing files and instructions to allow running tests

Deprecated
~~~~~~~~~~
* oci bv volume create --size-in-mbs parameter is now deprecated in favor of the new --size-in-gbs parameter

2.4.9 - 2017-09-13
------------------

Fixed
~~~~~~~~~~
* On Windows, fall back to old default config location (%USERPROFILE%\.oraclebmc\config) if new default location doesn't exist (%USERPROFILE%\.oci\config).

Added
~~~~~~~~~~
* Support for CustomerSecretKey operations (oci iam customer-secret-key create / delete / list / update).

2.4.8 - 2017-09-11
------------------

Deprecated
~~~~~~~~~~
* The CLI entry point (command name) has been changed from bmcs to oci. The old entry point will continue to work, but is deprecated.
* The CLI package name has been changed from oraclebmc-cli to oci-cli. The oraclebmc-cli package is deprecated and will no longer be maintained starting March 2018. Please upgrade to the oci-cli package to avoid interruption at that time.
* The default configuration file location has been changed from ~/.oraclebmc/config to ~/.oci/config. The old location still works if the file at the new location does not exist.

Added
~~~~~
* Support for the Database service
* Object Storage bulk operations (oci os object bulk-upload / bulk-download / bulk-delete)
* Support for compartment renaming
* Scripts to simplify install process
* Complex input can now be provided as a file instead of having to escape JSON input at the command line. The path to the file can be provided using the file:// prefix, for example --my-complex-param file://<path>, and the following paths are supported

  * Relative paths from the same directory, such as file://my-input.json and file://relative/path/to/input.json
  * Absolute paths on Linux, macOS or Unix, such as file:///absolute/path/to/input.json
  * Full file paths on Windows, such as file://C:\path\to\input.json
  * Using file path expansions, for example '~/', './', and '../' is supported. On Windows, the '~/' expression expands to your user directory, stored in the %USERPROFILE% environment variable
  * Using environment variables in paths is also supported

Changed
~~~~~~~
* The default configuration file location is now ~/.oci/config

2.4.7 - 2017-08-22
------------------

Fixed
~~~~~
- Upgraded pyOpenSSL dependency to 17.0.0

2.4.6 - 2017-08-10
------------------

Added
~~~~~
- Subcommands to 'bmcs compute image import / export' to allow specifying 
  source / destination in multiple formats.
- Secondary IP operations ('bmcs network private-ip', 'bmcs network vnic 
  assign/unassign-private-ip').
- '-h' alias for global '--help' option (https://github.com/oracle/bmcs-cli/issues/6)

Fixed
~~~~~
- 'bmcs os object put' accepts input from stdin (https://github.com/oracle/bmcs-cli/issues/7)
- 'bmcs compute image export' successfully exports image (https://github.com/oracle/bmcs-cli/issues/4)

Changed
~~~~~~~
- Upgraded cryptography dependency to 1.8.2 (https://github.com/oracle/bmcs-cli/issues/5)
- Deprecated --image-source-details param of 'bmcs compute image create' in 
  favor of subcommands (see Added section).

2.4.5 - 2017-07-20
------------------

Added
~~~~~
- Support for VCN multi-VNIC operations.
- Support for compute image import/export operations.

2.4.4 - 2017-06-09
------------------

Added
~~~~~

-  Support for tab completion for commands and parameters. It can be
   enabled by using 'bmcs setup autocomplete'.
-  Support for object storage pre-authenticated requests and public
   buckets.
-  Support for uploading parts in parallel for multipart uploads to
   object storage.
-  Support for nested instance metadata operations.

2.4.2 - 2017-05-18
------------------

Added
~~~~~

-  Support for 'bmcs iam region list' and 'bmcs iam region-subscription'
   operations
-  First class support for new IAD region
-  --assign-public-ip, --private-ip and --vnic-display-name parameters
   for 'bmcs compute instance launch'
-  --prohibit-public-ip-on-vnic parameter for 'bmcs network subnet
   create'

Fixed
~~~~~

-  Updated parsing of --region parameter to enable better support for
   unrecognized regions

2.4.1 - 2017-05-11
------------------

Added
~~~~~

-  Support for Object Storage multipart uploads
-  --ssh-authorized-keys-file and --user-data-file parameters for 'bmcs
   compute instance launch'

2.4.0 - 2017-04-06
------------------

Added
~~~~~

-  Support for DHCP Search Domain Option.
-  Support for 'bmcs compute instance get-windows-initial-creds'.
-  A progress bar is shown during 'bmcs os object get' and 'bmcs os
   object put'. Note that this is shown on STDERR, such that the output
   on STDOUT will still be standard JSON.
-  New options 'passphrase' and 'passphrase-file' for 'bmcs setup keys'
   that allow specifying a private key passphrase.

2.3.0 - 2017-03-28
------------------

Fixed
~~~~~

-  Handle service responses containing new model subtypes without
   throwing an exception.

Added
~~~~~

-  Support for hostnames for instances and DNS labels for VCNs and
   subnets.

2.2.0 - 2017-03-16
------------------

Added
~~~~~

-  Support for generating an RSA key pair using 'bmcs setup keys'
-  Support for generating the CLI config using 'bmcs setup config'

Fixed
~~~~~

-  Order is preserved in prefixes returned by 'object list'

Changed
~~~~~~~

-  Updated crytography version to 1.8.1.
-  Includes requests security feature, which will allow requests to use
   the version of openssl that's bundled with cryptography.
-  Parameter "--name" for Put Object is now optional and defaults to the
   filename provided in "--file"

2.1.3 - 2017-02-23
------------------

Added
~~~~~

-  If using a private key with a passphrase that has not been specified
   in your config file, then you will be prompted to provide the
   passphrase.
-  Support for stateless security list rules.

2.1.1 - 2017-02-03
------------------

Added
~~~~~

-  Support for IPXE script parameter in launch instance operation.

2.1.0 - 2017-01-17
------------------

Added
~~~~~

-  Support for Compute Service, Networking Service, and Block Volume
   Service, API version 20160918.

2.0.0 - 2016-12-16
------------------

Added
~~~~~

-  Support for Identity and Access Management Service, API version
   20160918 (see commands under 'bmcs iam')
-  Options to set the endpoint and certificate bundle ('--endpoint' and
   '--cert-bundle')
-  Options in object put for content-type, content-language, and
   content-encoding.

Fixed
~~~~~

-  Object get will no longer try to decode the object based on the
   encoding.

Changed
~~~~~~~

-  All Object Storage Service operations are now underneath 'bmcs os'.
-  All successful responses are in JSON format or empty (unless debug is
   enabled or there is a confirmation prompt). The body of each response
   is under a field called 'data', and headers such as 'etag' and
   'opc-next-page' are included in the response.
-  All dictionary keys in the JSON response are lowercase and use
   hyphens between words, with the exception of keys for user-defined
   metadata.
-  Many option shortcuts have been removed.
-  Metadata for objects and buckets must now be specified in JSON
   format. The previous format was 'key1=value1,key2=value2', and the
   new format is ''{"key1":"value1","key2":"value2"}'.
-  All delete operations will prompt the user for confirmation, unless
   the '--force' option is used.
-  Object put will prompt the user for confirmation if the object
   already exists, unless '--force' or '--if-match' is used.
-  The '--if-none-match' option has been removed from object put.
-  Options that are defined at the root level (under 'bmcs') can now be
   specified anywhere in the command.
-  Help will be provided for any command with '-?' in addition to
   '--help'.

1.0.1 - 2016-11-18
------------------

Added
~~~~~

-  Improved config file validation

1.0.0 - 2016-10-20
------------------

Added
~~~~~

-  Initial Release
-  Support Object Storage Service, API version 20160918.
