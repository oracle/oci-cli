==========
Change Log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`__.

2.5.10 - 2019-05-14
-------------------
Added
~~~~~
* Support for changing the recovery window for backup in the Database service (``--recovery-windows-in-days``  option for ``oci db database create``)

* Support for LoggingContext option in Key Management Service (``--logging-context`` option for ``oci kms crypto encrypt|decrypt|generate-data-encryption-key``)

  * An example on using Key Management Service LoggingContext option can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/kms_example.sh>`__.
  * (``oci kms crypto encrypt --logging-context``)
  * (``oci kms crypto decrypt --logging-context``)
  * (``oci kms crypto generate-data-encryption-key --logging-context``)

* opc-prev-page header added to Email List responses (``oci email sender list``)

Changed
~~~~~~~
* Warning messages for invalid file permissions. Include OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING in messages.

2.5.9 - 2018-05-07
------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Tokyo (NRT) region (``--region ap-tokyo-1``)

Changed
~~~~~~~
* Jinja2 was upgraded to version 2.10.1 to address a vulnerability identified on GitHub as CVE-2019-10906. Jinga isn't used in our run-time system but as part of our documentation build process.

2.5.8 - 2019-04-16
------------------
Added
~~~~~
* Improve information to customer premise equipment by introducing Customer Reference Name in the VPN Service.

  * (``oci network cpe create --customer-reference-name [text]``)
  * (``oci network cpe update --customer-reference-name [text]``)

* Improve information to IPSecConnection by introducing Customer Reference Name in the VPN Service.

  * (``oci network ipsecconnection create --customer-reference-name [text]``)
  * (``oci network ipsecconnection update --customer-reference-name [text]``)

* Improve information to RemorePeeringConnection by introducing Provider Service Key Name in the VPN Service.

  * (``oci network remote-peering-connection create --provider-service-key-name [text]``)
  * (``oci network remote-peering-connection update --provider-service-key-name [text]``)

* Support Autonomous Database to change the License Type in the Database Service.

  * (``oci db autonomous-database update --license-model [LICENSE_INCLUDED|BRING_YOUR_OWN_LICENSE]``)

* Support Autonomous Database to change the whitelistips in the Database Service.

  * (``oci db autonomous-database update --whitelisted-ips '[  "1.1.1.1","2.2.2.2/24" ]'``)

* Content-type auto option for object storage put and bulk-upload commands.

* Tagging support for create Dynamic Group and update Dynamic Group flow as part of the Identity Service

  * (``oci iam dynamic-group create --defined-tags --freeform-tags``)
  * (``oci iam dynamic-group update --defined-tags --freeform-tags``)

Fixed
~~~~~
* Installation issues in Ubuntu 18.04.

2.5.7 - 2019-04-09
------------------
Fixed
~~~~~~
* Fixed inconsistencies in SDK and CLI for Compute's create app catalog subscription. All the options are made optional to make it consistent with the SDK. 

* Use of ``--region`` option with instance principal auth 

2.5.6 - 2019-04-02
------------------
Added
~~~~~
* New command as mentioned below is added to the FastConnect Service. A provider service key is an
  identifier for a provider's virtual circuit.

  * ``oci network fast-connect-provider-service-key get``

* Improvement that introduces --customer-reference-name to CrossConnect and CrossConnectGroup in the FastConnectService.

  * (``oci network cross-connect create --customer-reference-name [text]``)
  * (``oci network cross-connect update --customer-reference-name [text]``)
  * (``oci network cross-connect-group create --customer-reference-name [text]``)
  * (``oci network cross-connect-group update --customer-reference-name [text]``)

* Improvement that introduces --provider-service-key-name to VirtualCircuit in the FastConnect Service.

  * (``oci network virtual-circuit create --provider-service-key-name [text]``)
  * (``oci network virtual-circuit update --provider-service-key-name [text]``)

Changed
~~~~~~~~
* Make cx-Oracle used by Database Service an optional package for OCI CLI installer. It's installation instructions are as below:

  * In \*NIX systems, type below commands in bash shell:

    * ``curl -L -O https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh"``
    * ``./install.sh --optional-features db``
  * In Windows systems using powershell, type below commands:

    * ``((New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1', "$pwd\\install.ps1"))``
    * ``.\install.ps1 -OptionalFeatures db``
  * If just using pip:

    * ``pip install 'oci-cli[db]'``


2.5.5 - 2019-03-26
------------------
Added
~~~~~
* Support for token-based authentication for the CLI allowing customers to authenticate their session interactively, then use the CLI for a single session without an API signing key

 * ``oci session authenticate``
 * ``oci session export``
 * ``oci session import``
 * ``oci session refresh``
 * ``oci session terminate``
 * ``oci session validate``

* Support for an interactive process to create a CLI config file using username / password based login through a browser. Also handles generating API keys and uploading them to your Oracle Cloud Infrastructure account.

 * ``oci setup bootstrap``

* Support for obtaining and updating Authentication Policy in the Identity Service.

  * ``oci iam authentication-policy get | update``

Changed
~~~~~~~~
* Documentation enhancements and corrections for traffic management in the DNS service.

* Improve Object Lifecycle Management policy in Object Storage by supporting glob patterns and exclusions.

  * An example on writing object lifecycle policy can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/write_object_lifecycle_policy.sh>`__.


2.5.4 - 2019-03-19
------------------
Added
~~~~~
* Support for provisioning a new autonomous database or autonomous data warehouse as a clone of another in the Database service

  * ``oci db autonomous-database create-from-clone``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/database_example.sh>`__.

* Support for specifying metadata on node pools in the Container Engine for Kubernetes service

  * ``oci ce node-pool create --node-metadata``

2.5.3 - 2019-03-12
------------------
Added
~~~~~
* Support DbSystem timezone on provisioning API.

  * (``oci db system launch --time-zone``)
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/database_launch_exadata_sparse_example.sh>`__.

* DbWorkload Type Introduced for Autonomous Database Create Request.

  * (``oci db autonomous-database create --db-workload``)
  * (``oci db autonomous-database list --db-workload``)

* Support for enabling I/O Resource Management (IORM) feature for Exadata Database Systems

  * (``oci db system get-exadata-iorm-config``)
  * (``oci db system update-exadata-iorm-config``)
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/database_exadata_iorm_example.sh>`__.

* Support for Tag Default feature as a part of the Identity Service

  * (``oci iam tag-default``)
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/tagging_example.sh>`__.

* Support for email on user accounts in the Identity Service

  * (``oci iam user create --email``)
  * (``oci iam user update --email``)

* Support for OCI Budget Service.

  * (``oci budgets budget create``)
  * (``oci budgets budget delete``)
  * (``oci budgets budget get``)
  * (``oci budgets budget list``)
  * (``oci budgets budget update``)
  * (``oci budgets alert-rule create``)
  * (``oci budgets alert-rule delete``)
  * (``oci budgets alert-rule get``)
  * (``oci budgets alert-rule list``)
  * (``oci budgets alert-rule update``)
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/budget_example.sh>`__.

2.5.2 - 2019-02-28
------------------
Added
~~~~~
* Support for OCI Monitoring Service

  * (``oci monitoring``)
  * An example using monitoring alarms can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/monitoring_alarm_example.sh>`__.
  * An example using monitoring metrics can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/monitoring_metrics_example.sh>`__.

* Support for Resource Manager service

  * (``oci resource-manager``)
  * An example of using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/resource_manager_example.sh>`__

* Support for Notification service

  * (``oci ons``)
  * An example of using notification subscriptions can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/notification_subscription_example.sh>`__
  * An example of using notification topics can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/notification_topic_example.sh>`__

* Support for Auto Scaling Configurations as part of Compute Autoscaling Service

  * (``oci autoscaling configuration create``)
  * (``oci autoscaling configuration delete``)
  * (``oci autoscaling configuration get``)
  * (``oci autoscaling configuration list``)
  * (``oci autoscaling configuration update``)
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/autoscaling_example.sh>`__.

* Support for Auto Scaling Policies as part of Compute Autoscaling Service

  * (``oci autoscaling policy create``)
  * (``oci autoscaling policy delete``)
  * (``oci autoscaling policy get``)
  * (``oci autoscaling policy list``)
  * (``oci autoscaling policy update``)

* Support to specify fault domains in Database system launch in Database service.

   * (``oci db system launch --fault-domains``)
   * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/database_launch_dbsystem_example.sh>`__.

* Support for Load Balancers for Instance Pools

    * (``oci compute-management instance-pool attach-lb``)
    * (``oci compute-management instance-pool detach-lb``)
    * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/instance_pools_example.sh>`__.

* Support for change Tag Namespace Compartment as a part of the Identity Service

  * (``oci iam tag-namespace change-compartment``)
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/tagging_example.sh>`__.

* Support for instance launch with agent configuration for enabling monitoring and retrieving agent configuration
 
  * (``oci compute instance launch --agent-config``) 
  * (``oci compute instance update --agent-config``)
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/compute_agent_enable_disable_example.sh>`__

2.5.1 - 2019-02-21
------------------
Added
~~~~~
* Tagging support for Key Management (``--freeform-tags`` and ``--defined-tags`` option for ``oci kms management vault/key create/update``)

  * An example on using KMS tagging can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/kms_example.sh>`__.

* Support for Oracle Streaming Service. (``oci streaming``)

  * An example on using the Streaming Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/streaming_example.sh>`__.

Changed
~~~~~~~
* Support for regional subnets, which you can create by omitting the ``availability-domain`` option in the ``oci network subnet create`` command.

* [Breaking] Removed 'followup' field from response for ``oci announce announcements get|list``

Fixed
~~~~~
* [Breaking] Aborting a multipart upload using CLI now returns an error code of 1 if the upload-id does not exist. Earlier it would return 0.

* [Breaking] CLI commands providing an option of wait-for-state will now set a return code of 2 in case of timeout. This differs from the earlier behavior when it would set a return code of 0. Similarly for any other error during the wait-for-state, a return code of 1 will be returned.

* Help text for Announcements Service (``oci announce``)


2.4.44 - 2019-02-07
-------------------
Added
~~~~~
* Connection Strings for Database Resource API in Database Service

  * The following commands responses have a new attribute `connectionStrings` added to them.
     * (``oci db database get``)
     * (``oci db database list``)

* Support for OCI DNS Traffic Management

  * (``oci dns steering-policy``)
  * (``oci dns steering-policy-attachment``)

* Support for Health Check Service (``oci health-checks``)

  * Ability to create and manage http health check 
  * Ability to create and manage ping health check 
  * Ability to list available vantage points
  * Ability to create on demand http probe 

* Support for tagging Approved Senders in the Email Service.

  * (``oci email sender create --defined-tags --freeform-tags``)
  * (``oci email sender update --defined-tags --freeform-tags``)

* Support for Web Application Acceleration and Security Service (``oci waas``)

  * An example on using the WAAS Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/waas_example.sh>`__.

Changed
~~~~~~~
* Changed the behavior of kubernetes configuration download command (``oci ce cluster create-kubeconfig``) in Container Engine service as follows:

  * Support for ``--overwrite`` flag while downloading kubernetes configuration. Using this flag ensures current behavior
    of ``oci ce cluster create-kubeconfig`` command where an existing kubeconfig file is overwritten by downloaded content.
  * Support for merging kubernetes configuration in Container Engine service. The command when used without ``--overwrite``
    flag merges the downloaded kubeconfig with existing kubeconfig in the config file, if it exists.
  * Support for writing kubernetes configuration to default location in Container Engine service. To support this, ``--file``
    option in ``oci ce cluster create-kubeconfig`` command has been made optional. When not given, the default kubeconfig
    location used is ``~/.kube/config``
  * The details about this change are documented in (``oci ce cluster create-kubeconfig --help``)

2.4.43 - 2019-01-31
-------------------
Added
~~~~~
* Support for Announcements Service (``oci announce``)

  * An example on using the Announcements Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/announcements_service_example.sh>`__.

2.4.42 - 2019-01-24
-------------------
Added
~~~~~
* Support for renaming the new database when restoring a database backup to an existing dbsystem (--db-name option for ``oci db database create-from-backup``)

* Support for renaming the new database when launching new dbsystem from a database backup (--db-name option for ``oci db system launch-from-backup``)

  * An example on using --db-name parameter while restoring a database from backup can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/rename_database_during_backup_restore.sh>`__.

* Support for calling Oracle Cloud Infrastructure services in the ``ca-toronto-1`` region (``--region ca-toronto-1``)

Changed
~~~~~~~
* Upgraded third party module versions for requests, cx_Oracle, pyOpenSSL, and cryptography. This should improve support for Python 3.7.

2.4.41 - 2019-01-14
-------------------
Added
~~~~~
* Support for passing device while attaching volume to instance in Compute service

  * (``oci compute volume-attachment attach --device``)

* Support for fetching devices for an instance in Compute service

  * (``oci compute device list-instance``)

* Support for Custom Header Rule Sets in the Load Balancer service

  * (``oci lb rule-set``)

2.4.40 - 2018-12-13
-------------------
Added
~~~~~
* Support for sparse diskgroup option with Exadata shape in the following command:

  * (``oci db system launch``)

* Support for Data Guard on VM DB Shape

* Support create option with-new-db-system along with from-existing-db-system

  * (``oci db data-guard-association create with-new-db-system``)

* Support for tagging Zones in the DNS service.

* Block Storage paravirtualized-encryption-in-transit feature

  * Ability to enable encryption-in-transit for paravirtualized volume attachment for both boot volumes and data volumes (``oci compute volume-attachment attach-paravirtualized-volume``)

* Support for resetting idp scim client as part of Identity Service.

  * (``oci iam scim-client-credentials reset-idp-scim-client --identity-provider-id``)

* Support for updating user capabilities as part of Identity Service.

  * (``oci iam user update-user-capabilities --user-id``)

* Support for listing identity provider groups as part of Identity Service.

  * (oci iam identity-provider-group list)

Changed
~~~~~~~
* New Attribute ``is-latest-for-major-version`` is included in (``oci db version list``) response

* pyOpenSSL was upgraded to version 17.5.0 and cryptography to version 2.1.4 to address a vulnerability identified on GitHub as CVE-2018-1000808.

2.4.39 - 2018-11-29
-------------------
Added
~~~~~
* Support for fetching bucket statistics in Object Storage getBucket service.

  * (``oci os bucket get --bucket-name --namespace-name --fields``)
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/get_bucket_example.sh>`__

2.4.38 - 2018-11-15
-------------------
Added
~~~~~
* VCN Transit Routing (VTR) feature as part of Virtual Cloud Network

    * Ability to associate route table when creating drg-attachment (`oci network drg-attachment create --routeTableId`)
    * Ability to associate route table when creating local-peering-gateway (`oci network local-peering-gateway create --routeTableId`)
    * Ability to associate route table when updating drg-attachment (`oci network drg-attachment update --routeTableId`)
    * Ability to associate route table when updating local-peering-gateway (`oci network local-peering-gateway update --routeTableId`)
    * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/vcn_transit_routing.sh>`__.

2.4.37 - 2018-11-01
-------------------
Added
~~~~~
* Support for tagging as part of FSS

  * (``oci fs file-system create --freeform-tags --defined-tags``)
  * (``oci fs snapshot create --freeform-tags --defined-tags``)
  * (``oci fs mount-target create --freeform-tags --defined-tags``)

* Support for modifying the route table, DHCP options, or security lists associated with a subnet.

* Improvements to access control of compartments by allowing users to only show accessible compartments and list all compartments under the current tenancy.

  * (``oci iam compartment list --access-level``)
  * (``oci iam compartment list --compartment-id-in-subtree``)

2.4.36 - 2018-10-26
---------------------
Fixed
~~~~~~~
* Fix malformed instance metadata keys for ``oci compute-management instance-configuration create`` and  ``oci compute-management instance-configuration launch-compute-instance``.  This was preventing SSH access to instances created through these commands.

2.4.35 - 2018-10-18
---------------------
Added
~~~~~~~~
* Support to Generate and Download wallet for Autonomous Transaction Processing Database and Autonomous Data Warehouse

  * (``oci db autonomous-data-warehouse generate-wallet``)
  * (``oci db autonomous-database generate-wallet``)

* Support for creating a standalone backup from an on-premises database as part of the Database service

  * Details can be found `here <https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm>`__.
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/src/oci_cli/scripts/database/dbaas.py>`__.

* Support for Cross Region Backup Copy in Block Storage.

  * (``oci bv backup copy --volume-backup-id --destination-region``)

* Support for Cost Tracking Tags as part of Identity Service.

  * (``oci iam tag create --is-cost-tracking``)
  * (``oci iam tag update --is-cost-tracking``)
  * (``oci iam tag list-cost-tracking``)

* Support for Compartment Delete, listing WorkRequests under a compartment and getting details for a work request.

  * (``oci iam compartment delete --compartment-id``)
  * (``oci iam work-request list --compartment-id``)
  * (``oci iam work-request get --work-request-id``)

* Support for Instance Configurations as part of Compute Management service

  * (``oci compute-management instance-configuration create``)
  * (``oci compute-management instance-configuration delete``)
  * (``oci compute-management instance-configuration get``)
  * (``oci compute-management instance-configuration list``)
  * (``oci compute-management instance-configuration update``)
  * (``oci compute-management instance-configuration launch-compute-instance``)

* Support for Instance Pools as part of Compute Management service

  * (``oci compute-management instance-pool create``)
  * (``oci compute-management instance-pool terminate``)
  * (``oci compute-management instance-pool get``)
  * (``oci compute-management instance-pool list``)
  * (``oci compute-management instance-pool update``)
  * (``oci compute-management instance-pool reset``)
  * (``oci compute-management instance-pool softreset``)
  * (``oci compute-management instance-pool start``)
  * (``oci compute-management instance-pool stop``)
  * (``oci compute-management instance-pool list-instances``)

Changed
~~~~~~~~
* New Attribute ``dbVersion`` is included in the GET Response for Autonomous Transaction Processing Database and Autonomous Data Warehouse.
* New Attribute ``allConnectionStrings`` is included in the GET Response for Autonomous Transaction Processing Database and Autonomous Data Warehouse.

2.4.34 - 2018-10-04
---------------------
Added
~~~~~~~~
* Support to consume Image Catalog Listings as part of Compute Service

  * (``oci compute pic listing``)
  * (``oci compute pic version``)
  * (``oci compute pic agreements``)
  * (``oci compute pic subscription``)  

* Support for Cross Region Copy in Object Storage.

  * (``oci os object copy --bucket-name --source-object-name --destination-region --destination-namespace --destination-bucket --destination-object``)

  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/copy_object_example.sh>`__

* Support for Object Lifecycle Management as part of the Object Storage service.

  * (``oci os object-lifecycle-policy put``)
  * (``oci os object-lifecycle-policy get``)
  * (``oci os object-lifecycle-policy delete``)

* Support for network address translation gateway in Networking service

  * (``oci network nat-gateway create``)
  * (``oci network nat-gateway delete``)
  * (``oci network nat-gateway get``)
  * (``oci network nat-gateway list``)
  * (``oci network nat-gateway update``)

2.4.33 - 2018-09-27
---------------------
Added
~~~~~~~~
* Support for Key Management Service (``oci kms``)

  * Examples on using the Key Management Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/kms_example.sh>`__.
* Support for ``--wait-for-state`` option on multiple commands.
* Improved custom image support by introducing PARAVIRTUALIZED as a launch mode option in the Image Import command.

  * (``oci compute image import --launch-mode PARAVIRTUALIZED``)
* Support for creating bucket with ``--kms-key-id``, updating ``--kms-key-id`` of a bucket.
* Support for creating data volume, boot volume, launch instance with ``--kms-key-id``, updating ``--kms-key-id`` for a data volume or boot volume.

2.4.32 - 2018-09-06
---------------------
Added
~~~~~~~~
* Support for updating user custom metadata on an instance in the Compute service after the instance has launched

  * (``oci compute instance update --instance-id --metadata --extended-metadata``)

* Ability to increase size of boot and block volumes during creation (from clone or restore from backup) in the Block Storage Service.

  * (``oci bv boot-volume create --size-in-gbs``)
  * (``oci bv volume create --size-in-gbs``)

Changed
~~~~~~~~
* Updated the Description of Database API to include new character set.
* The default License Type for Autonomous DataWarehouse and Autonomous Transaction Processing will be Bring Your Own License.

2.4.31 - 2018-08-23
---------------------
Added
~~~~~~~~
* Support for Autonomous DataWarehouse and Autonomous Transaction Processing features as a part of the Database Service

  * (``oci db autonomous-data-warehouse``)
  * (``oci db autonomous-data-warehouse-backup``)
  * (``oci db autonomous-database``)
  * (``oci db autonomous-database-backup``)

* Ability to increase size of boot and block volumes in the Block Storage Service.
   
  * (``oci bv boot-volume update --size-in-gbs``)
  * (``oci bv volume update --size-in-gbs``)

* Support for Fault Domains feature in the Identity Service. (``oci iam fault-domain``)

2.4.30 - 2018-08-09
---------------------
Added
~~~~~~~~
* Support for instances in the Compute service by fault domains (--fault-domain option for ``oci compute instance launch``)
* The ability to use a FIPS compliant version of libcrypto on linux platforms.
* Support for short date and time format when providing a datetime parameter to the CLI.

  * YYYY-MM-DD HH:mm, e.g. 2017-09-15 17:25. The timezone for this date will be taken as UTC. (Needs to be surrounded by single or double quotes)

Fixed
~~~~~~~~
* The minimum python version check in the Windows install script now works properly with the following scenario.  Previously version 2.7.13 was not being detected as greater than 2.7.5.

Changed
~~~~~~~~
* Moved all example scripts to separate 'examples' directory under scripts

2.4.29 - 2018-07-26
---------------------
Added
~~~~~~~~
* Support for Resource Search service (``oci search``)

  * An example on using the Resource Search Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/resource_search_example.sh>`__.

* Ability to set the scheduled backup policy on Boot Volume creation in the Block Storage Service. (``oci bv boot-volume create --backup-policy-id``)

2.4.28 - 2018-07-12
---------------------
Added
~~~~~~~~
* Human-friendly Resource, Compartment and User name fields in Events listed by Audit Service (``oci audit event list``).
* Improve access control to file systems by introducing NFS Export option in the File Storage Service.

  * (``oci fs export create --export-options``)
  * (``oci fs export update --export-options``)

* Support for updating a load balancer.

  * (``oci lb load-balancer update``)

* Support for tagging of load balancer resource enabled in the Load Balancer service.

  * (``oci lb load-balancer create --defined-tags --freeform-tags``)
  * (``oci lb load-balancer update --defined-tags --freeform-tags``)

Fixed
~~~~~~~~
* Output created by ``--generate-param-json-input`` has been customized to produce more helpful json for defined and free-form tags.

2.4.27 - 2018-06-28
---------------------
Added
~~~~~~~~
* Support for Service Gateway feature in the Networking Service (``oci network service`` and ``oci network service-gateway``)
* Support for Backup and Clone of Boot Volumes in the Block Storage Service (``oci bv boot-volume-backup`` and ``oci bv boot-volume create``)

Fixed
~~~~~~~~
* ``oci setup oci-cli-rc`` now works without specifying --file option

2.4.26 - 2018-06-15
---------------------
Fixed
~~~~~~~~
* Cluster create command in Oracle Container Engine Service is not working correctly in previous release v2.4.25. It has been fixed as part of this release. (``oci ce cluster create`` fixed)

  * A sample test using the Oracle Container (Kubernetes) Engine Service feature can be found on `Github <https://github.com/oracle/oci-cli/blob/master/tests/examples/test_containerengine.py>`__

2.4.25 - 2018-06-14
---------------------
Added
~~~~~~~~
* Support for Oracle Container Engine Service (``oci ce``)

  * A sample test using the Oracle Container (Kubernetes) Engine Service feature can be found on `Github <https://github.com/oracle/oci-cli/blob/master/tests/examples/test_containerengine.py>`__

NOTE: Release 2.4.25 should not be used if you are trying to use Oracle Container Engine Service.
A bug with `oci ce cluster create` was discovered shortly after releasing version 2.4.25 to PyPi, so there is no 2.4.25 release on Github.
Users should upgrade to release 2.4.26 to use Oracle Container Engine Service related functionality.

Fixed
~~~~~~~~
* Enabled 'namespace-name' parameter for all commands in the Object Storage service.
* Add dependency to idna >=2.5,<2.7 since cryptography and requests both have a dependency on the library and pip can install a version that is incompatable with requests.

2.4.24 - 2018-05-31
---------------------
Added
~~~~~~~~
* Support for launching database system from backup in the Database service (``oci db system launch-from-backup``)
* Support for soft shutdown of instances in the Compute service (SOFTSTOP option for --action in ``oci compute instance action``)
* Use the root compartment ID (tenancy ID) from the config file as a default value for compartment/tenancy parameter for the following commands in the Identity service:

  * ``oci iam region-subscription list``
  * ``oci iam availability-domain list``
  * ``oci iam group list | add-user | create | list-users | remove-user``
  * ``oci iam user list | list-groups | create``
  * ``oci iam dynamic-group list | create``

Changed
~~~~~~~~
* Bumped version number of python-dateutil package (2.7.3) to address clock skew warning
* Name for "Swift Passwords" to "Auth Tokens" in Identity service (Use ``oci iam auth-token`` instead of ``oci iam swift-password`` or ``oci iam user swift-password``)

Fixed
~~~~~~~~
* Support for escaping non-alphanumeric characters in the Windows installation script.

2.4.23 - 2018-05-17
---------------------
Added
~~~~~~~~
* Support for backup or clone of multiple volumes at once using volume groups in the Block Storage service
* Support for the ability to optionally specify a compartment filter when listing exports in the File Storage service
* Support for tagging virtual cloud network resources in the Networking service
* Support for specifying a custom python installation directory using the --python-install-location parameter of the bash install script

Changed
~~~~~~~~
* For object storage commands (``oci os``), update --namespace parameter to be optional and fetch it from the server if it is not provided from the user

Fixed
~~~~~~~~
* Force bash install script to use TLS 1.2 when downloading Python

2.4.22 - 2018-05-03
---------------------
Added
~~~~~~~~
* Support for returning ``event-name`` in logs extracted from Audit Service. (``oci audit event list``)
* Support for multiple hostnames per listener in Load Balancer Service. An example can be found on `Github <https://github.com/oracle/oci-cli/blob/master/scripts/examples/create_load_balancer.sh>`__ (``oci lb hostname`` and ``oci lb listener create --hostname-names``)
* Support for FastConnect service. New commands as mentioned below are added:

  * ``oci network cross-connect-group``
  * ``oci network cross-connect``
  * ``oci network cross-connect-location``
  * ``oci network cross-connect-port-speed-shape``
  * ``oci network cross-connect-status``
  * ``oci network fast-connect-provider-service``
  * ``oci network virtual-circuit``
  * ``oci network virtual-circuit-public-prefix``

Fixed
~~~~~~~~
* Multiple OCI CLI installation issues as specified below:

  * Corrected usage of ``--accept-all-defaults`` to prevent an infinite loop.
  * An issue which causes failure of OCI CLI installations in non-default directories.
  * An issue related to download of virtualenv package on Windows instances.

2.4.21 - 2018-04-19
---------------------
Added
~~~~~~~~
* Support for the following features for the Database service:

  * Tagging support for the following resources

    * Update database (``oci db database update --defined-tags --freeform-tags``)
    * Launch and update database system (``oci db system launch|update --defined-tags --freeform-tags``)

  * Filter set of database versions based on database system ID (``oci db version list --db-system-id``)

2.4.20 - 2018-04-05
---------------------
Added
~~~~~~~~
* An example of how to scale existing VM instances using the CLI can be found on `Github <https://github.com/oracle/oci-cli/blob/master/scripts/examples/scale_vm_example.sh>`__
* A warning message informing use of ``--all`` flag to get all items during list operations.

Fixed
~~~~~~~~
* Multipart bulk download to correctly enable downloads as per size thresholds set by the user.
* Check all required parameters are present before prompting for deleting resource

Changed
~~~~~~~~
* Use root compartment OCID (tenancy OCID) as default value for --compartment-id  in ``oci iam compartment list`` command.

2.4.19 - 2018-03-26
---------------------
Added
~~~~~~~~
* Support for managing SMTP credentials in the Identity Service (``oci iam smtp-credential``)
* Support for remote VCN peering across regions (``oci network remote-peering-connection``)
* Support for calling Oracle Cloud Infrastructure services in the uk-london-1 (LHR) region

Changed
~~~~~~~~
* When listing audit events (``oci audit event list``) the ``--start-time`` and ``--end-time`` parameters specify values with granularity to the minute. If you provide values which have non-zero seconds or milliseconds, these will be rounded to the nearest minute with greater than or equal to 30 seconds rounding upwards and less than 30 seconds rounding downwards

Fixed
~~~~~~~
* When providing a datetime parameter to the CLI, v2.4.18 and below did not parse datetimes correctly but instead of failing they silently coverted values to midnight of the date provided and sent this value to the service. This version fixes the datetime parsing and the following inputs will be considered valid:

  * ``YYYY-MM-DDTHH:mm:ss.sssTZD`` (UTC) with milliseconds, e.g. 2017-09-15T20:30:00.123Z
  * ``YYYY-MM-DDTHH:mm:ssTZD`` (UTC) without milliseconds, e.g. 2017-09-15T20:30:00Z
  * ``YYYY-MM-DDTHH:mmTZD`` (UTC) with minute precision, e.g. 2017-09-15T20:30Z
  * ``YYYY-MM-DDTHH:mm:ssTZD`` (timzone with offset) with milliseconds, e.g. 2017-09-15T12:30:00.456-08:00, 2017-09-15T12:30:00.456-0800
  * ``YYYY-MM-DDTHH:mm:ssTZD`` (timezone with offset) without milliseconds, e.g. 2017-09-15T12:30:00-08:00, 2017-09-15T12:30:00-0800
  * ``YYYY-MM-DDTHH:mmTZD`` (timezone with offset) with minute precision, e.g. 2017-09-15T12:35-08:00, 2017-09-15T12:35-0800
  * ``YYYY-MM-DD``, e.g. 2017-09-15. This date will be taken as midnight UTC of that day
  * Unix time in seconds, e.g. 1412195400

Security Notice
~~~~~~~~~~~~~~~~~~
* Versions of oci-cli prior to 2.4.10 are affected by a security vulnerability. Versions 2.4.11 and later will automatically detect vulnerable installations, and if issues are detected, a warning will be displayed to the user. These issues can be remediated automatically by running the ``oci setup repair-file-permissions`` command.

2.4.18 - 2018-03-08
---------------------
Added
~~~~~~~~~~
* Support for the Email Service. (``oci email``)

  * A sample test using the email feature can be found on `Github <https://github.com/oracle/oci-cli/blob/master/tests/examples/test_email.py>`__
  * This release does not include support for managing SMTP credentials.  Please use the web console or any OCI SDK to manage SMTP credentials.

* Support for the following features in the Core Services:

  * paravirtualized volume attachments (--type option for ``oci compute volume-attachment attach``)
  * variable size boot volumes (--boot-volume-size-in-gbs option for ``oci compute instance launch``)

* Support for auto-pagination for the Domain Name System Service. (--all, --page-size options for ``oci dns record domain get``, ``oci dns record rrset get``, ``oci dns record zone get``)
* Support for no-overwrite flag for the object put operation for the Object Service (--no-overwrite for ``oci os object put``).

Fixed
~~~~~~~~~~
* Updated config / key file permissions logic on Windows to depend on well known SIDs instead of account / group name to
  fix localization issues. This affects ``oci setup config``, ``oci setup repair-file-permissions``, and the general
  config / key file permissions check performed by other commands.

2.4.17 - 2018-02-22
---------------------
Added
~~~~~~~~~~
* Support for the File Storage Service. (``oci fs``)
* Support for Path Route Sets in the Load Balancer Service. An example can be found on `Github <https://github.com/oracle/oci-cli/blob/master/scripts/examples/create_load_balancer.sh>`__ (``oci lb path-route-set``)
* Tagging support for *Bucket* resources in the Object Storage Service

  * Create a bucket with tags: ``oci os bucket create --defined-tags --freeform-tags``
  * Update a bucket with tags: ``oci os bucket update --defined-tags --freeform-tags``
  * List buckets and display defined and freeform tags in the results: ``oci os bucket list --fields tags``

* Support for specifying a restore period for archived objects in the *RestoreObjects* operation of the Object Storage service. (``oci os object restore --hours``)
* Support for filtering by *backupId* in *ListDbSystems* operation in the Database Service (``oci db system list --backup-id``)
* Support for getting plink (the `PuTTY <https://www.putty.org/>`__ command line interface) compatible instance console connection string for Windows users (``oci compute instance-console-connection get-plink-connection-string``)

2.4.16 - 2018-02-08
---------------------
Added
~~~~~~~~~~
* Support for Domain Name System Service (oci dns)

  * An example on using the Domain Name System Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/dns_example.sh>`__.

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
  * Operations which support applying tags will have --defined-tags and --freeform-tags options. Check the help dump (https://github.com/oracle/oci-cli/blob/master/tests/output/inline_help_dump.txt) for resources which support tags. A general list of taggable resources can also be found in: https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Taggable
  * An example of using tagging can be found at https://github.com/oracle/oci-cli/blob/master/scripts/examples/tagging_example.sh

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

  * An example of creating a load balancer can be found a https://github.com/oracle/oci-cli/blob/master/scripts/examples/create_load_balancer.sh

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
* Support for getting archived object restore status ('oci os object restore-status') more details in sample (https://github.com/oracle/oci-cli/scripts/examples/restore_archived_object.sh)

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
