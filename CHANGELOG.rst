==========
Change Log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`__.

2.24.1 - 2021-04-22
-------------------
Fixed
~~~~~
* Previous release had a bug which caused CLI installations on Windows operating systems to fail with an error. Please see `github issue #404 <https://github.com/oracle/oci-cli/issues/404>`_ for more details


2.24.0 - 2021-04-20
-------------------
Added
~~~~~

* Support for enabling and disabling Operations Insights for External Non-Container and External Pluggable Databases in Database service

  * ``oci db external-non-cdb enable-operations-insights``
  * ``oci db external-non-cdb disable-operations-insights``
  * ``oci db external-pdb enable-operations-insights``
  * ``oci db external-pdb disable-operations-insights``

* Support for customer contract for Autonomous Databases in Database Service

  * ``oci db autonomous-database create --customer-contacts``
  * ``oci db autonomous-database create-from-backup-id --customer-contacts``
  * ``oci db autonomous-database create-from-backup-timestamp --customer-contacts``
  * ``oci db autonomous-database create-from-clone --customer-contacts``
  * ``oci db autonomous-database create-refreshable-clone --customer-contacts``
  * ``oci db autonomous-database update --customer-contacts``

* Support for business name annotation of harvested objects in Data Catalog service

  * ``oci data-catalog attribute | entity | folder update --business-name``

* Support for opt-in/opt-out of live migration at an instance level in Compute service

  * ``oci compute instance launch --availability-config '{"isLiveMigrationPreferred": true}'``

Changed
~~~~~~~

* [Breaking] This version drops support for Python 3.5

  * Due to a possible security issue in the version of the dependent cryptography package, we have bumped up the version to 3.3.2. This version does not support Python 3.5.

* Updated help text for putting messages into a stream in Streaming Service

  * ``oci streaming stream message put``

* Some unused commands have been removed from the DNS service

  * ``oci dns resolver-endpoint create-resolver-endpoint-create-resolver-vnic-endpoint-details``
  * ``oci dns resolver-endpoint update-resolver-endpoint-update-resolver-vnic-endpoint-details``

* Some parameters made optional for signing uploads in Artifacts service

  * ``oci artifacts container image-signature sign-upload --description --metadata``

2.23.0 - 2021-04-13
-------------------
Added
~~~~~

* Support for Database Migration service

  * ``oci database-migration``

* Support for following in Network Service

  * Support for Networking Topology

    * ``oci network networking-topology``
    * ``oci network vcn-topology``

  * Support to improve the DRG functionality

    * ``oci network drg get-all-drg-attachments``
    * ``oci network drg get-upgrade-status``
    * ``oci network drg upgrade``
    * ``oci network drg-attachment remove-export-route-distribution``
    * ``oci network drg-route-distribution``
    * ``oci network drg-route-distribution-statement``
    * ``oci network drg-route-rule``
    * ``oci network drg-route-table``
    * ``oci network internal-public-ip delete-drg-route-table``

  * Support to asssign/unassign IPV6 for the VNIC

    * ``oci network vnic assign-ipv6``
    * ``oci network vnic unassign-ipv6``

  * Support for enabling IPv6 support in the existing subnet

    * ``oci network subnet update --ipv6-cidr-block``

  * Support to list the Cross Connect mapping Details for the specified Virtual Circuit

    * ``oci network cross-connect-mapping-details-collection list-cross-connect-mappings --virtual-circuit-id``

* Support for following in OCVS Service

  * [Breaking] New required parameter --current-sku has been added to the below command

    * ``oci ocvs esxi-host create --current-sku``

  * [Breaking] New required parameter --initial-sku has been added to the below command

    * ``oci ocvs sddc create --initial-sku``

  * New parameter --next-sku has been added to the below command

    * ``oci ocvs esxi-host update --next-sku``

* Support for getting a cluster cache metrics for a specified RAC CDB Managed Database in the Database Management service

  * ``oci database-management cluster-cache-metric``

* Support for new parameter --response-cache-details in the API Gateway service

  * ``oci api-gateway gateway create --response-cache-details``
  * ``oci api-gateway gateway update --response-cache-details``

* Support for preemptible instances in Compute service

  * ``oci compute instance launch --preemptible-instance-config``

* Improvements for Operations Insights in the OPSI service

  * ``oci opsi database-insights``
  * ``oci opsi enterprise-manager-bridges``
  * ``oci opsi host-insights``
  * ``oci opsi work-requests``


Changed
~~~~~~~~

* Updated parameters for database insight list operation in the OPSI service.

  * ``oci opsi database-insights list``

* Following commands changed in Network Service

  * [Breaking] Optional param --is-internet-access-allowed is deleted for the below commands

    * ``oci network ipv6 update``
    * ``oci network vnic assign-ipv6``

  * [Breaking] Optional param --ipv6-cidr-block is deleted for the below commands

    * ``oci network vcn add-ipv6-vcn-cidr``
    * ``oci network vcn create``


2.22.2 - 2021-04-06
-------------------
Added
~~~~~

* Support for Database Software Image for Database service

  * ``oci db database-software-image create --image-shape-family EXACC_SHAPE``
  * ``oci db database-software-image list --image-shape-family EXACC_SHAPE``

* Support for new parameters in Compute service

  * ``oci compute dedicated-vm-host list --remaining-ocpus-greater-than-or-equal-to``
  * ``oci compute dedicated-vm-host list --remaining-memory-in-gbs-greater-than-or-equal-to``

* Support for new parameters ``total-memory-in-gbs`` and ``remaining-memory-in-gbs`` in Compute service

  * ``oci compute dedicated-vm-host create``
  * ``oci compute dedicated-vm-host list``
  * ``oci compute dedicated-vm-host get``
  * ``oci compute dedicated-vm-host update``

* Support for new parameters ``access-type``, ``object-name``, ``bucket-listing-action`` in Preauth-request service

  * ``oci os preauth-request create --access-type --object-name --bucket-listing-action``

* Support for SDK generation feature in the API Gateway service

  * ``oci api-gateway sdk --help``
  * ``oci api-gateway sdk-language-type --help``

* Support for a new parameter ``image-policy-config`` for Container Engine in Kubernetes service

  * ``oci ce cluster create``
  * ``oci ce cluster update``

* Support for new parameter ``routing-policy`` in Network service.

  * ``oci network virtual-circuit create --routing-policy``
  * ``oci network virtual-circuit update --routing-policy``

* Support for new parameter ``capacity`` in autoscaling service.

  * ``oci autoscaling policy create --capacity``

* Support for cross-region asynchronous volume replication in Block Storage service

  * ``oci bv block-volume-replica``
  * ``oci bv boot-volume-replica``
  * ``oci bv volume update --block-volume-replicas``
  * ``oci bv boot-volume update --boot-volume-replicas``
  * ``oci bv volume create --source-volume-replica-id``
  * ``oci bv boot-volume create --source-volume-replica-id``

* Support for Container Image Signing in artifacts service

  * ``oci artifacts container image-signature``

* Support for new type of authorizationDetails in Application Migration service.

  * ``oci application-migration source create-source-ocic-authtoken --authorization-details-client-app-url --authorization-details-access-token``
  * ``oci application-migration source update-source-ocic-authtoken --authorization-details-client-app-url --authorization-details-access-token``

Changed
~~~~~~~~

* The parameter ``specification`` is now optional for API deployment in the API Gateway service

  * ``oci api-gateway deployment create --specification``

* PyYAML was upgraded to 5.3.1

* Tox was upgraded to version 3.23.0. Tox isn't used in our run-time system but as part of our documentation build process.

  * Pluggy upgraded to 0.13.0 and virtualenv upgraded to 16.7.10 for same reasons as above.

Fixed
~~~~~

* Fixed timeout issue in log-analytics service

  * ``oci log-analytics upload upload-log-file``
  * ``oci log-analytics upload upload-log-events-file``


2.22.1 - 2021-03-30
-------------------
Added
~~~~~
* Support for the Vulnerability Scanning service.
  
  * ``oci vulnerability-scanning``

* Support for vSphere 7.0 in the VMware Solution service. 
  
  * ``oci ocvs sddc create --provisioning-vlan-id, --replication-vlan-id``
  * ``oci ocvs sddc update --provisioning-vlan-id, --replication-vlan-id``
  
* Support for forecasting in the Usage service.
  
  * ``oci usage-api usage-summary request-summarized-usages --forecast``

* Support for listing, changing, and resetting parameters for on-premise Oracle databases in the Database Management service
  
  * ``oci database-management managed-database change-database-parameters``
  * ``oci database-management managed-database list-database-parameters``
  * ``oci database-management managed-database reset-database-parameters``

* Support for listing tablespaces of managed databases in the Database Management service
  
  * ``oci database-management tablespace list``

* Support for cross-regional replication of keys in the Key Management service
  
  * ``oci kms management replication-status-details get-replication-status``
  * ``oci kms management vault create-vault-replica``
  * ``oci kms management vault delete-vault-replica``
  * ``oci kms management vault list-vault-replicas``
  
* Support for highly-available database systems in the MySQL Database service
  
  * ``oci mysql db-system create --is-highly-available``
  * ``oci mysql db-system import --is-highly-available``
  
* Support for Oracle Enterprise Manager bridges, source auto-association, source event type mappings, and plugins to upload data in the Logging Analytics service
  
  * Support for partitioning/searching data via logset 
    
    * ``oci log-analytics storage list-log-sets``
  
  * Support for Source Auto Association 
  
    * ``oci log-analytics source list-auto-assocs``
    * ``oci log-analytics source enable-auto-assoc``
    * ``oci log-analytics source disable-auto-assoc``
  
  * Support for Source Event Types Mapping 
  
    * ``oci log-analytics source add-event-types``
    * ``oci log-analytics source disable-event-types``
    * ``oci log-analytics source enable-event-types``
    * ``oci log-analytics source remove-event-types``
    * ``oci log-analytics source list-event-type``
  
  * Support for Enterprise Manager bridges 

    * ``oci log-analytics em-bridge``
  
  * Support for Log events API used by plugins like fluentd, fluentbit, etc to upload data to logging analytics
  
    * ``oci log-analytics upload upload-log-events-file``
  
  * Support for Lookups Summary 
  
    * ``oci log-analytics lookup get-summary``
  
  * Support for Source Associable Entities 
  
    * ``oci log-analytics source list-associable-entities``
  
  * Additional fields in the following commands
  
    * ``oci log-analytics entity list --creation-source-details, --creation-source-type``
    * ``oci log-analytics parser extract-structured-log-field-paths --field-delimiter,  --field-qualifier``
    * ``oci log-analytics parser extract-structured-log-header-paths --field-delimiter,  --field-qualifier``
    * ``oci log-analytics parser test-parser --field-delimiter,  --field-qualifier``
    * ``oci log-analytics parser upsert-parser --field-delimiter,  --field-qualifier``
    * ``oci log-analytics scheduled-task list --display-name-contains --saved-search-id``
    * ``oci log-analytics upload list --warnings-filter``
    * ``oci log-analytics upload upload-log-file --log-set``

Changed
~~~~~~~
* Jinja2 was upgraded to version 2.11.3. Jinja isn't used in our run-time system but as part of our documentation build process.

* Fixed bug in the dry-run option for bulk download command.
  
  * ``oci os object bulk-download --dry-run``

2.22.0 - 2021-03-23
-------------------
Added
~~~~~
* Support for Network Load Balancer service

  * ``oci nlb``

* Support for Organizations Domain and Domian Governance in Organization service

  * ``oci organizations domain``
  * ``oci organizations domain-governance``

* Support for query to filter and aggregate in Usage API service

  * ``oci usage-api query``

* Support to list and get maintenance runs for autonomous database in Database service.

  * ``oci db maintenance-run list --target-resource-type AUTONOMOUS_DATABASE``
  * ``oci db maintenance-run list --target-resource-id <autonomous-database-ocid>``
  * ``oci db maintenance-run get --maintenance-run-id <maintenance-run-ocid>``

* Support for Marketplace Publication feature in Marketplace service

  * ``oci marketplace publication``
  * ``oci marketplace publication-package``
  * ``oci marketplace publication-summary``

* Support for Compute Capacity Reservation feature in Compute service

  * ``oci compute capacity-reservation``

* Support for Announcements Preferences in Announcements Service.

  * ``oci announce announcements-preferences``

* Support for HeatWave Cluster (in-memory analytics accelerator) in MySQL Database Service.

  * ``oci mysql db-system heatwave-cluster``
  * ``oci mysql db-system heatwave-cluster-memory-estimate generate``
  * ``oci mysql db-system heatwave-cluster-memory-estimate get``

* [Breaking] The parameter --vnic-id is now required for create IPv6 for the specified VNIC in Network service.

  * ``oci network ipv6 create``

Fixed
~~~~~
* Fixed upload large files bug in create-model-artifact in Data Science service

  * ``oci data-science model create-model-artifact``

2.21.6 - 2021-03-16
-------------------
Added
~~~~~
* Support for Routing Policies and HTTP2 Listener protocol features in Load Balancer service

  * ``oci lb routing-policy``
  * ``oci lb listener create --routing-policy-name --protocol HTTP2``
  * ``oci lb listener update --routing-policy-name --protocol HTTP2``

* Support for updating instance usage type, (NONPRIMARY, PRIMARY), in OCE service

  * ``oci oce oce-instance update --instance-usage-type``

* Support for private clusters to the Container Engine in Kubernetes service

  * ``oci ce cluster create --endpoint-subnet-id --endpoint-public-ip-enabled --endpoint-nsg-ids``
  * ``oci ce cluster update-endpoint-config --is-public-ip-enabled --nsg-ids``
  * ``oci ce cluster create-kubeconfig --kube-endpoint``

* Support for model deployment in Data Science service

  * ``oci data-science model-deployment``

* Support for copying stacks in Resource Manager service

  * ``oci resource-manager stack copy``

* Support for retrieving certificates for clusters and nodes in Roving Edge Infrastructure service

  * ``oci rover cluster get-certificate``
  * ``oci rover node get-certificate``
  * ``oci rover node setup-identity``

Fixed
~~~~~
* Bug with resource_principal not properly working with --region parameter

2.21.5 - 2021-03-09
-------------------
Added
~~~~~
* Support for SMS subscriptions through the Oracle Cloud Infrastructure Notifications service.

  * ``oci ons message publish``
  * ``oci ons subscription confirm``
  * ``oci ons subscription create``
  * ``oci ons subscription unsubscribe``

* Support for friendly formatting messages when target is ONS as part of the Service Connector Hub service.

  * ``oci sch service-connector create``
  * ``oci sch service-connector update``

* Support the ability to attach and detach instance from instance pool in Compute Management service.

  * ``oci compute-management instance-pool-instance attach``
  * ``oci compute-management instance-pool-instance detach``
  * ``oci compute-management instance-pool-instance get``

* Support for Application Performance Monitoring Trace service

  * ``oci apm-traces``

* Support for Application Performance Monitoring Synthetic service

  * ``oci apm-synthetics``

* Support for APM service control plane

  * ``oci apm-control-plane``

* Support for GoldenGate service

  * ``oci goldengate``

Changed
~~~~~~~~
* Updated incremental delay and retry mechanism for create-backup-from-onPrem script in Database service

2.21.4 - 2021-03-02
-------------------
Added
~~~~~
* Support for Clones Feature in File System Service

  * ``oci fs file-system create``
  * ``oci fs file-system list``

* Support for pipelines and pipeline tasks for Dataflow service

  * ``oci data-integration pipeline``

* Enhanced support for publishing Data Integration tasks for Dataflow service

  * ``oci data-integration task get --expand-references``
  * ``oci data-integration task-run list --aggregator-key``
  * ``oci data-integration connection update--password-secret``
  * ``oci data-integration data-entity list --is-pattern``
  * ``oci data-integration schema list --name-list``
  * ``oci data-integration work-request list --workspace-id``

2.21.3 - 2021-02-23
-------------------
Added
~~~~~
* Support for exporting an existing running VM, or a copy of VM, into a VMDK, QCOW2, VDI, VHD, or OCI formatted image in the Compute service

  * ``oci compute image export to-object --export-format``
  * ``oci compute image export to-object-uri --export-format``

* Support for providing target-tags and target-compartments in the Profile in the Optimizer service

  * ``oci optimizer profile create --target-compartments, --target-tags``
  * ``oci optimizer profile update --target-compartments, --target-tags``

* Support for Optional param ``--actions`` in Recommendation Bulk Apply in the Optimizer service

  * ``oci optimizer recommendation bulk-apply --actions``

* Support for the 'Fix it' feature in the Optimizer service

  * ``oci optimizer recommendation-strategy-summary list-recommendation-strategies``

* Support for the OCI Registry Service

  * ``oci artifacts``

* Support for configuring the Platform Configuration of type AMD_MILAN_BM of an Instance in Compute service.

  * ``oci compute instance launch --platform-config '{"type":"AMD_MILAN_BM","numaNodesPerSocket":"NPS1"}'``

Changed
~~~~~~~~
* Fix volume create commands to not infer availability domain if it is manually specified by the user

  * ``oci bv volume create``
  * ``oci bv boot-volume create``

* Required param ``--resource-action-ids`` has been made optional in Recommendation Bulk Apply in the Optimizer service

  * ``oci optimizer recommendation bulk-apply --resource-action-ids``

* Param ``--name`` can now be updated in Profile in the Optimizer service

  * ``oci optimizer profile update --name``

2.21.2 - 2021-02-16
-------------------
Added
~~~~~
* New parameter --is-selective-migration is added for the below commands in Application Migration Service

  * ``oci application-migration migration create --is-selective-migration``
  * ``oci application-migration migration update --is-selective-migration``

* Support for "OCC" Source type in Application Migration Service

  * ``oci application-migration source``

* Support for change network endpoint for integration instance in Integration Service

  * ``oci integration integration-instance change-network-endpoint``

2.21.1 - 2021-02-09
-------------------
Added
~~~~~
* Support for Database Management service

  * ``oci database-management``

* Support for additional upgrade options in Database service

  * ``oci db database upgrade-with-db-home``
  * ``oci db database upgrade-with-database-software-image``
  * ``oci db database upgrade-with-db-version``

* Support for discovering available plugins in Oracle Cloud Agent service

  * ``oci instance-agent plugin``
  * ``oci instance-agent available-plugins``

* Support for Erratum List API in OS Management service

  * ``oci os-management erratum-summary list-errata``
  * ``oci os-management managed-instance list-managed-instance-errata``

* Support to Enable/Disable Oracle Cloud Agent plugins in Compute service

  * ``oci compute instance launch --agent-config '{ "are-all-plugins-disabled" : true|false,"plugins-config": []}'``
  * ``oci compute instance update --agent-config '{ "are-all-plugins-disabled" : true|false,"plugins-config": []}'``

* Support for recommending glossary terms in Data Catalog service

  * ``oci data-catalog catalog recommendations``
  * ``oci data-catalog catalog process-recommendation``

* Support for setting the offset to start budget processing in Budgets service

  * ``oci budgets budget create --budget-processing-period-start-offset``
  * ``oci budgets budget update --budget-processing-period-start-offset``

Changed
~~~~~~~

* Minor help text updates for

  * ``oci os object bulk-delete-versions``
  * ``oci os object bulk-delete``
  * ``oci os object bulk-download``


2.21.0 - 2021-02-02
-------------------
Added
~~~~~

* Support for checking if a contact for Exadata infrastructure is valid in My Oracle Support in the Database service

  * ``oci db exadata-infrastructure create --contacts``
  * ``oci db exadata-infrastructure update --contacts``

* Support for external databases in the Database service
  
  * ``oci db external-cdb``
  * ``oci db external-database-connector``
  * ``oci db external-pdb``
  * ``oci db external-non-cdb``

* Support for uploading objects to the infrequent access storage tier in the Object Storage service
  
  * ``oci os object put --storage-tier``
  * ``oci os object copy --destination-object-storage-tier``
  * ``oci os object bulk-upload --storage-tier`` 

* Support for changing the storage tier of existing objects in the Object Storage service

  * ``oci os object update-storage-tier --storage-tier`` 

* Support for private templates in the Resource Manager service

  * ``oci resource-manager template create``
  * ``oci resource-manager template get``
  * ``oci resource-manager template delete``
  * ``oci resource-manager template get-template-logo``
  * ``oci resource-manager template get-template-tf-config``
  * ``oci resource-manager template list``
  * ``oci resource-manager template update``
  * ``oci resource-manager template list-template-categories``
  * ``oci resource-manager template change-compartment``

* Support for multiple encryption domains on IPSec tunnels in the Networking service
  
  * ``oci network ip-sec-tunnel update --encryption-domain-config``

Changed
~~~~~~~

* Input parameter ``--vnic-id`` is now optional for the command ``oci network ipv6 create``

* [Breaking] Response field ``vnicId`` is now optional for the following commands

  * ``oci network ipv6 create``
  * ``oci network ipv6 get``
  * ``oci network ipv6 update``


2.20.0 - 2021-01-26
-------------------
Added
~~~~~

* Support for Load Balancer Shape update for Blockchain Platform in Blockchain Service

  * ``oci blockchain blockchain-platform update --load-balancer-shape``

* [Breaking] The parameter --idcs-access-token is now required for Blockchain Platform create in Blockchain Service

  * ``oci blockchain blockchain-platform create``

* Support for private access channel in Analytics Service

  * ``oci analytics analytics-instance create-private-access-channel ``
  * ``oci analytics analytics-instance get-private-access-channel``
  * ``oci analytics analytics-instance update-private-access-channel``
  * ``oci analytics analytics-instance delete-private-access-channel``

* Support for vanity URL in Analytics Service

  * ``oci analytics analytics-instance create-vanity-url``
  * ``oci analytics analytics-instance update-vanity-url``
  * ``oci analytics analytics-instance delete-vanity-url``

* Support assignment of Volume Backup Policy to Volume Group in Block Volume Service

  * ``oci bv volume-group create --backup-policy-id``

* Support for --max-wait-seconds, --wait-for-state, --wait-interval-seconds for Change Compartment of Dedicated VM Host in Compute Service

  * ``oci compute dedicated-vm-host change-compartment --max-wait-seconds --wait-for-state --wait-interval-seconds``

* Support for --max-wait-seconds, --wait-for-state, --wait-interval-seconds for the below commands of Network Service

  * ``oci network byoip-range validate``
  * ``oci network drg change-compartment``
  * ``oci network subnet change-compartment``
  * ``oci network vcn add-vcn-cidr``
  * ``oci network vcn change-compartment``
  * ``oci network vcn modify-vcn-cidr``
  * ``oci network vcn remove-vcn-cidr``
  * ``oci network vlan change-compartment``

* support for Access Control List for Autonomous Database with Data Guard enabled on Exadata Cloud Customer in Database Service

  * ``oci db autonomous-database create --are-primary-whitelisted-ips-used, --standby-whitelisted-ips``
  * ``oci db autonomous-database update --are-primary-whitelisted-ips-used, --standby-whitelisted-ips``

* Support to specify Peer ACD unique name when creating Data Guard enabled Autonomous Container Database on Exadata Cloud Customer in Database Service

  * ``oci db autonomous-container-database create --peer-db-unique-name``

* Support for drift detection on individual resources of a stack in Resource Manager Service

  * ``oci resource-manager stack detect-drift --resource-addresses``

* Support for listing drift detection details given a work request id in Resource Manager Service

  * ``oci resource-manager stack list-resource-drift-details --work-request-id``

* Support for Create, Manage and Use of AsymmetricKeys in KeyManagement Service.

  * ``oci kms crypto encrypt --key-version-id --encryption-algorithm``
  * ``oci kms crypto decrypt --key-version-id --encryption-algorithm``

2.19.0 - 2021-01-19
-------------------
Added
~~~~~

* Support for Data Archive and Recall features as a part of the Logging Analytics Service

  * ``oci log-analytics storage``

* Support for lookups in the Logging Analytics service

  * ``oci log-analytics lookup *``

* Support for Agent Collection Warnings in the Logging Analytics service

  * ``oci log-analytics warning list``
  * ``oci log-analytics warning suppress``
  * ``oci log-analytics warning unsuppress``

* Scheduled Task commands in the Logging Analytics service

  * ``oci log-analytics scheduled-task pause``
  * ``oci log-analytics scheduled-task resume``

* Support to specify whether or not an object-collection-rule is currently enabled in the Logging Analytics service

  * ``oci log-analytics object-collection-rule create --is-enabled``
  * ``oci log-analytics object-collection-rule update --is-enabled``

* Support for Logging Analytics as a target in the Service Connector Hub service

* [BREAKING] The --sort-by parameter for few of the commands in log-analytics is restricted to only name field
  * ``oci log-analytics source list-meta-source-types --sort-by``
  * ``oci log-analytics parser list-parser-functions --sort-by``
  * ``oci log-analytics parser list-parser-meta-plugins --sort-by``
  * ``oci log-analytics source list-source-label-operators --sort-by``


2.18.0 - 2021-01-12
-------------------
Added
~~~~~

* Support for specifying region using numbers for the setup configuration command

  * ``oci setup config``

* Support for auto-scaling in the Big Data service

  * ``oci bds auto-scale-config create``
  * ``oci bds auto-scale-config get``
  * ``oci bds auto-scale-config edit``
  * ``oci bds auto-scale-config list``
  * ``oci bds auto-scale-config delete``
  * [BREAKING] ``UPDATING_INFRA`` option removed for ``oci bds instance list --lifecycle-state``

* Documentation fixes for the Logging Search service

Fixed
~~~~~~~~
* Fixed node-shape-config to be recognized as complex type

  * ``oci ce node-pool create --generate-param-json-input node-shape-config``

2.17.0 - 2020-12-15
-------------------
Added
~~~~~

* Support for the following in the Roving Edge Infrastructure Service

  * Rover Cluster API

    * ``oci rover cluster``

  * Rover Node API

    * ``oci rover node``

* Database Service

  * Support for Customer-Managed Key features

    * ``oci db database migrate-vault-key``
    * ``oci db database rotate-vault-key``

  * Support for listing flex components

    * ``oci db flex-component list``

* Support for filtering listKeys based on KeyShape in Key Management Service

  * ``oci kms management key list --algorithm, --length``

* Support for Github configuration source provider in Resource Manager Service

  * ``oci resource-manager configuration-source-provider create-github-access-token-provider``
  * ``oci resource-manager configuration-source-provider update-github-access-token-provider``

* Data Catalog Service

  * Support for listing harvested rules

    * ``oci data-catalog rule-summary list-rules``

  * Additional filtering options available for Logical Entity list calls

    * ``oci data-catalog entity list-aggregated-physical --display-name-contains``
    * ``oci data-catalog entity list-derived-logical-entities --display-name-contains``

* Support for flexible load balancers in Load Balancer Service

  * ``oci lb load-balancer create --shape-details``

Changed
~~~~~~~

* [BREAKING] Deprecated support for Autonomous Data Warehouse in Database Service

  * ``oci db autonomous-data-warehouse``

2.16.1 - 2020-12-08
-------------------
Added
~~~~~

* Support for custom endpoint feature in the Integration Service
 
  * ``oci integration integration-instance create --custom-endpoint``
  * ``oci integration integration-instance update --custom-endpoint``

* Support for the following in the Database Service

  * Maintenance Schedule feature for Exadata Infrastructure resources
 
    * ``oci db exadata-infrastructure create --maintenance-window``
    * ``oci db exadata-infrastructure update --maintenance-window`` 

  * ORDS and SSL certificate rotation for Autonomous Exadata Infrastructure
 
    * ``oci db autonomous-exadata-infrastructure rotate-ords-certs --autonomous-exadata-infrastructure-id``
    * ``oci db autonomous-exadata-infrastructure rotate-ssl-certs --autonomous-exadata-infrastructure-id``

* Support added for fine-grained data analysis and improved SQL insights 
 
  * Added IMPROVING field for ``oci opsi database-insights summarize-sql-statistics --category``

2.16.0 - 2020-12-01
-------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Santiago region (``--region sa-santiago-1``)

* Support for Mysql Database Service Channels

  * ``oci mysql channel``

* Support for Data Safe on-prem-connector

  * ``oci data-safe on-prem-connector``

* Support for Availability Status and History of Management Agent

  * ``oci management-agent agent list-availability-histories``

* Backups now can be filtered by creation type in MySql Service

  * ``oci mysql backup list --creation-type``

Changed
~~~~~~~

* Upgraded versions for the following packages: arrow (0.14.7), cryptography (3.2.1), pyOpenSSL (19.1.0) and pycparser (2.20).

* Added optional parameter ``--tenancy-name`` to ``oci session authenticate``

* [Breaking] The command ``oci data-safe configuration get`` has been changed to ``oci data-safe service get`` in Data Safe Service

* [Breaking] The parameter --compartment-id is now required for private endpoint list in Data Safe Service

  * ``oci data-safe private-endpoint list --compartment-id``

* [Breaking] The parameter --compartment-id is now required for work request list in Data Safe Service

  * ``oci data-safe work-request list --compartment-id``

* [Breaking] The parameter --is-enabled is now required for service enable in Data Safe Service

  * ``oci data-safe service enable --is-enabled``

* Help text improvements for blockchain platform in Blockchain Service

  * ``oci blockchain blockchain-platform``

* The parameter --variables is now optional for mysql configuration in MySql Service

  * ``oci mysql configuration create --variables``

* The parameter --configuration-id is now optional for the below commands in MySql Service

  * ``oci mysql db-system clone --configuration-id``
  * ``oci mysql db-system create --configuration-id``
  * ``oci mysql db-system import --configuration-id``

2.15.0 - 2020-11-17
-------------------
Added
~~~~~
* Support to bulk edit tags on resources in Identity and Access Management Service

  * ``oci iam tag bulk-edit --bulk-edit-operations``

* Support to retrieve bulk edit tags enabled resources in Identity and Access Management Service

  * ``oci iam tag bulk-edit-tags-resource-type list``

* New Options have been added to the following command in Database Service

  * ``oci db autonomous-container-database create --peer-autonomous-vm-cluster-id --peer-autonomous-container-database-compartment-id --peer-autonomous-container-database-backup-config``

* New Option has been added to the following commands in Database Service

  * ``oci db database-software-image list --is-upgrade-supported``
  * ``oci db version list --is-upgrade-supported``

* Support for Database Upgrade in Database Service

  * ``oci db database list-upgrade-history``
  * ``oci db upgrade-history get``
  * ``oci db database upgrade``
  * ``oci db database upgrade-rollback``
  * ``oci db database upgrade-with-database-software-image``
  * ``oci db database upgrade-with-db-home``
  * ``oci db database upgrade-with-db-version``


Changed
~~~~~~~
* Added automatic retries for ``oci os object put`` (single part and multipart uploads) in case of certain errors. Retry will happen a maximum of 3 times and will have exponential backoff. To disable these retries, please use the `-—no-retry` flag
* Removed the constraints about the accepted values for status in Work Requests list in Container Engine Service

  * ``oci ce work-request list --status``

* ID field is now optional for the below command in Management Dashboard Service

  * ``oci management-dashboard saved-search create --id``

* [Breaking] Following changes in the Log Analytics Service

  * Moved commands under ``oci log-analytics error-details`` to be under ``oci log-analytics source`` in Log Analytics Service
  * Moved commands under ``oci log-analytics extended-fields-validation-result`` to be under ``oci log-analytics source``  in Log Analytics Service
  * Moved commands association* to assoc
    * Example ``oci log-analytics log-analytics-association-collection list-source-associations`` to ``oci log-analytics assoc list-source-assocs``
  * Moved commands estimate* and storage-work-request to storage
    * Example ``oci log-analytics estimate-purge-data-size-result estimate-purge-data-size`` to ``oci log-analytics storage estimate-purge-data-size``
    * Example ``oci log-analytics storage-work-request list`` to ``oci log-analytics storage list-storage-work-requests``


2.14.5 - 2020-11-10
-------------------
Added
~~~~~
* Support for --dry-run option for bulk-upload and bulk-download command in object storage service

  * ``oci os object bulk-download --dry-run``
  * ``oci os object bulk-upload --dry-run``

* Support for creating a Data Guard association with a standby database from a database software image in the Database service

  * ``oci db data-guard-association create from-existing-db-system --database-software-image-id``
  * ``oci db data-guard-association create from-existing-vm-cluster --database-software-image-id``
  * ``oci db data-guard-association create with-new-db-system --database-software-image-id``

* Support for specifying a TDE wallet password when creating/updating a database or database system in the Database service

  * ``oci db database create --tde-wallet-password``
  * ``oci db system launch --tde-wallet-password``
  * ``oci db database update --new-admin-password --new-tde-wallet-password --old-tde-wallet-password``

* Support for private DNS resolvers, resolver endpoints, and views in the DNS service

  * ``oci dns resolver``
  * ``oci dns resolver-endpoint``
  * ``oci dns view``

* Support for analytics clusters (database accelerators) in the MySQL Database service

  * ``oci mysql db-system analytics-cluster-memory-estimate generate``
  * ``oci mysql db-system analytics-cluster-memory-estimate get``
  * ``oci mysql db-system analytics-cluster``

* Support for migrations to Java Cloud Service and Oracle Weblogic Server instances that use existing databases in the Application Migration service

  * ``oci application-migration migration create --pre-created-target-database-type``

* Support for Enabling Access Control Lists for Autonomous Databases on Exadata Cloud At Customer

  * ``oci db autonomous-database create --is-acl-enabled``
  * ``oci db autonomous-database create-from-clone --is-acl-enabled``
  * ``oci db autonomous-database update --is-acl-enabled``

* Support for getting a VCN and resolver association in the Networking service

  * ``oci network vcn-dns-resolver-association get``

* Support for specifying reserved IPs when creating load balancers in the Load Balancing service

  * ``oci lb load-balancer create --reserved-ips``

* Support for additional parameters when updating subnets and VLANs in the Networking service

  * ``oci network vcn add``
  * ``oci network vcn modify-vcn-cidr``
  * ``oci network vcn remove``

Changed
~~~~~~~~

* Create db-home requires either db-version or database-software-image-id

  * ``oci db db-home create``

* ``cidr-block`` parameter is now Optional for the following commands in the Network Service

  * ``oci network subnet update --cidr-block``
  * ``oci network vcn create --cidr-block``
  * ``oci network vlan update --cidr-block``

Fixed
~~~~~~~

* Incorrect help text for --fields parameter for following command in Object Storage Service

  * ``oci os bucket get --fields``

2.14.4 - 2020-11-03
-------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Cardiff region (``--region uk-cardiff-1``)

* Support for the Organizations service

  * ``oci organizations``

* Support for the Optimizer service

  * ``oci optimizer``

* Support for tenancy ID and name on responses in the Usage service

* Support for specifying a syslog URL for applications in the Functions service

  * ``oci fn application create --syslog-url``

* Support for creation of always-free NoSQL database tables in the NoSQL Database service

  * ``oci nosql table create`` has a new option ``--is-auto-reclaimable`` to request the creation of a free table. 

2.14.3 - 2020-10-29
-------------------
Fixed
~~~~~

* Upgraded version of OCI Python SDK to fix Object Storage Service issue. Please see `github issue #300 <https://github.com/oracle/oci-python-sdk/issues/300>`_ for more details.

* Bug in installation script for --accept-all-defaults installs with TTY (`Pull Request <https://github.com/oracle/oci-cli/pull/344/files>`__)


2.14.2 - 2020-10-27
-------------------
Added
~~~~~

* Support for Compute Instance Agent Service

  * ``oci instance-agent``

* Support for Key Store Resource representing Oracle Key Vault Instances in Database Service

  * ``oci db key-store``

* Support for customer managed key store in Autonomous Container Databases in Database Service

  * ``oci db autonomous-container-database create --key-store-id``

Changed
~~~~~~~

* Installation script will prompt users to upgrade to Python 3 if Python 2 is installed

Fixed
~~~~~

* Unicode errors for bulk object operations in Object Storage Service

  * ``oci os object bulk-upload | bulk-download | bulk-delete``

* Documentation fixes for Logging Search Service

  * ``oci logging-search``


2.14.1 - 2020-10-20
--------------------
Added
~~~~~

* Support for Operations Insights service

  * ``oci opsi``

* Support to enable/disable Operations Insights Service for Autonomous Database in Database Service

 * ``oci db autonomous-database enable-operations-insights --autonomous-database-id``
 * ``oci db autonomous-database disable-operations-insights --autonomous-database-id``

* New lifecycle state NEEDS_ATTENTION to Improve DB System in Database Service

  * ``oci db system``

* Support for HCX for create/update Software Defined Data Center (SDDC) in Oracle Cloud VMware Solution Service (OCVS)

  * ``oci ocvs sddc create --is-hcx-enabled --hcx-vlan-id``
  * ``oci ocvs sddc update --hcx-vlan-id``

* Improvement for Service Connector Hub documentation

  * ``oci sch``

Fixed
~~~~~

* Parameter --package-name is now optional for Software Source Search in OS Management Service (`Issue 332 <https://github.com/oracle/oci-cli/issues/332>`__)

  * ``oci os-management software-source search --package-name``


2.14.0 - 2020-10-13
--------------------
Added
~~~~~

* Support for API definitions in the API Gateway service

  * ``oci api-gateway api --help``

* Support for pattern-based Logical Entities, namespace-bound Custom Properties, and faceted search in the Data Catalog service

  * ``oci data-catalog pattern``
  * ``oci data-catalog data-asset add-data-selector-patterns``
  * ``oci data-catalog entity list-aggregated-physical``
  * ``oci data-catalog namespace``
  * ``oci data-catalog custom-property``
  * ``oci data-catalog type associate-custom-properties``
  * ``oci data-catalog search query``

* Support for Autonomous Data Guard for Autonomous Infrastructure

   * ``oci autonomous-container-database-dataguard``
   * ``oci autonomous-database-dataguard``

* Support for creating a Data Guard association on an existing standby database home in the Database service.

 * ``oci db data-guard-association create from-existing-db-system --peer-db-home-id``
 * ``oci db data-guard-association create from-existing-vm-cluster --peer-db-home-id``

* Support for list database homes by version.

 * ``oci db db-home list --db-version``

* Support for upgrading Cloud VM Cluster Grid Infrastructure

  * ``oci db cloud-vm-cluster update [options]``

Changed
~~~~~

* Help messages for Logging Ingestion Service

* Support for updating saved search logs for Logging Service

  * ``oci logging log-saved-search``
  * ``oci logging log-included-search``

* [Breaking]  Required param ``is-quick-start`` is deleted from ``oci logging log-saved-search create/update``
* [Breaking]  Command ``oci db autonomous-exadata-infrastructure-shape list`` has been changed to ``oci db autonomous-exadata-infrastructure shape list``

2.13.0 - 2020-10-06
--------------------
Added
~~~~~

* Support for the following features in the Database service

  * Rotating keys on autonomous container databases and autonomous databases
  
    * ``oci db autonomous-container-database rotate-key``
    * ``oci db autonomous-database rotate-key``

  * Managing Cloud Exadata Infrastructure resources
 
    * ``oci db cloud-exa-infra``

  * Managing Cloud VM Cluster resources
 
    * ``oci db cloud-vm-cluster`` 

* Support for the following features in the Data Integration Service

  * Application list patch changes (``oci data-integration application list-patch-changes``)
  * Application references (``oci data-integration reference``)
  * Publishing Data Integration tasks to OCI Dataflow service 

    * ``oci data-integration external-publication``
    * ``oci data-integration external-publication-validation``

  * Generic JDBC and MySQL data asset types

    * ``oci data-integration data-asset update | create``

  * [Breaking] The following commands have been moved

    * ``oci data-integration task delete-task-validation`` to ``oci data-integration task-validation delete``
    * ``oci data-integration task get-task-validation`` to ``oci data-integration task-validation get``
    * ``oci data-integration task list-task-validations`` to ``oci data-integration task-validation list``

* Support for disabling the legacy Instance Metadata endpoints v1 in the Compute service

  * ``oci compute instance launch --instance-options``

* Support for instance configurations specifying instance options in the Compute Management service

  * ``oci compute-management instance-configuration create --instance-details`` 

* Support for controlling the display of tax banners in the Marketplace service
  
  * ``oci marketplace tax-summary list-taxes`` 

* Streaming output support for listing objects in Object Storage (`Issue 323 <https://github.com/oracle/oci-cli/issues/323>`__)

  * ``oci os object list --stream-output``

* Support for calling Oracle Cloud Infrastructure services in the Dubai region (``--region me-dubai-1``)

2.12.13 - 2020-09-29
--------------------
Added
~~~~~

* Support for Custom SSL Certificates for Gateways as part of the API Gateway Service

  * ``oci api-gateway certificate create``
  * ``oci api-gateway certificate delete``
  * ``oci api-gateway gateway create --certificate-id``
  * ``oci api-gateway gateway update --certificate-id``

* Support for specifying custom content dispositions when downloading objects in the Object Storage service

  * ``oci os object get``

* Support for updating the tags of an instance console connection in Compute Service

  * ``oci compute instance-console-connection update``

* Support for the “bring your own IP address” feature in the Virtual Networking service

  * ``oci network byoip-range``
  * ``oci network public-ip-pool``

* Support for db-home update in Database Service

  * ``oci db db-home update --db-home-id <Db Home OCID> --db-version <DB Home Patch Details>``

2.12.12 - 2020-09-22
--------------------
Added
~~~~~

* Support for Software Keys in Key Management Service

  * ``oci kms management key create --protection-mode SOFTWARE``
  * ``oci kms management key import --protection-mode SOFTWARE``
  * ``oci kms management key list --protection-mode SOFTWARE``

* Support for exporting software keys in Key Management Service

  * ``oci kms crypto key export``

* Support to update open mode and permission level for Autonomous Database

  * ``oci db autonomous-database update --open-mode``
  * ``oci db autonomous-database update --permission-level``

* Support to specify number of memory in GB when launching or updating a Compute instance

  * ``oci compute instance launch --shape-config "shapeConfig":{"memoryInGBs": 0.0, "ocpus": 0.0}``
  * ``oci compute instance update --shape-config``

* Support for managing shape compatibility entries with memory constraints for Compute images

  * ``oci compute image-shape-compatibility-entry``

* Added new parameter to specify the allow memory in GB range per ocpu for Compute shapes

  * ``oci compute shape list --max-per-ocpu-in-gbs, --min-per-ocpu-in-gbs``

* Pagination support for listing announcements from Announce service (`Issue 311 <https://github.com/oracle/oci-cli/issues/311>`__)

  * ``oci announce announcements list --all, --limits, --page-size``

Changed
~~~~~~~

* Support specifying customer contacts when creating or updating an exadata infrastructure

  * ``oci db exadata-infrastructure create --contacts <json with contacts>``
  * ``oci db exadata-infrastructure update --contacts <json with contacts>``

2.12.11 - 2020-09-15
--------------------
Added
~~~~~

* Support for specifying desired consumption models when creating instances in the Integration service

  * ``oci integration integration-instance create --consumption-model``

* Support for updating load balancer shape in the Load Balancing service
  
  * ``oci lb load-balancer update-load-balancer-shape``

* Support for the Cloud Guard Service
  
  * ``oci cloud-guard``

*  Support for no tty option for non-interactive installation on non-Windows systems (`Issue 282 <https://github.com/oracle/oci-cli/issues/321>`__)
  
  * ``./install.sh --no-tty``

* Support for retrieving specified tenancy information in Identity Service

  * ``oci iam tenancy get``

Fixed
~~~~~

* Error when using wait-for-state for creating a compartment

  * ``oci iam compartment create --wait-for-state``


2.12.10 - 2020-09-08
--------------------
Added
~~~~~

* Support for searching Oracle Cloud resources across tenancies in the Search Service

  * ``oci search resource free-text-search --tenant-id``
  * ``oci search resource structured-search --tenant-id``

* Support for Management Agent Cloud Service

  * ``oci management-agent``

* Support for sending diagnostic interrupt to a VM instance in the Compute Service

  * ``oci compute instance action --action SENDDIAGNOSTICINTERRUPT --instance-id``

* Support for custom Database Software Images in the Database Service

  * ``oci db database-software-image``

* Support for Management Dashboard Service

  * ``oci management-dashboard``

* Support for Logging Analytics Service

  * ``oci log-analytics``

* Support for Logging Service

  * ``oci logging``

* Support for Logging Ingestion Service

  * ``oci logging-ingestion``

* Support for Logging Search Service

  * ``oci logging-search``

* Support for Service Connector Hub service

  * ``oci sch``

* Support for getting and listing container database patches for Autonomous Container Database resources in the Database Service

  * ``oci db autonomous-patch get --autonomous-patch-id``
  * ``oci db autonomous-patch list-container-database-patches --autonomous-container-database-id``

* Support for updating patch id on maintenance run for Autonomous Container Database resources in the Database Service

  * ``oci db maintenance-run update --patch-id``

Changed
~~~~~~~

* Support for Policy based Request/Response transformation

  * ``oci api-gateway deployment``


2.12.9 - 2020-09-01
-------------------
Added
~~~~~

* Support for customers to find the latest CLI version

  * ``oci --latest-version``

* Support for customers to view changelog entries for newer CLI versions

  * ``oci --release-info``

* Support for returning all results for Resource Manager job logs

  * ``oci resource-manager job get-job-logs --all``

* Improvement for DB System, Cloud VMCluster and Cloud Exadata Infrastructure by introducing lifecycle state MAINTENANCE_IN_PROGRESS in Database Service

  * ``oci db system``
  * ``oci db vm-cluster``
  * ``oci db exadata-infrastructure``

* VM DB cloning - clone dbSystem from a source dbSystem

  * ``oci db system launch-from-db-system``

* Option private-ip for other type of dbSystem launches

  * ``oci db system launch --private-ip``
  * ``oci db system launch-from-backup --private-ip``
  * ``oci db system launch-from-database --private-ip``

* Support for Network Sources in Authentication Policy in Identity Service

  * ``oci iam authentication-policy update``

* Support for AMD Flexible Shapes with configurable CPU to the Container Engine for Kubernetes service

  * ``oci ce node-pool create --node-shape-config``
  * ``oci ce node-pool update --node-shape-config``

* New options for listener and backendset to specify ssl protocols, ssl ciphersuite and server order preference in Load Balancer Service

  * ``oci lb backend-set``
  * ``oci lb listener``
  * ``oci lb load-balancer``
  * ``oci lb ssl-cipher-suite``

* Support for calling Oracle Cloud Infrastructure services in the Chiyoda region (``--region ap-chiyoda-1``)

Changed
~~~~~~~

* jmespath package requirement bumped to 0.10.0


2.12.8 - 2020-08-18
-------------------
Added
~~~~~

* Support for configuring VM instances for scheduled maintenance or hypervisor reboots in the Compute service

  * ``oci compute instance launch --availability-config '{"recoveryAction": "STOP_INSTANCE"}'``
  * ``oci compute instance update --availability-config '{"recoveryAction": "STOP_INSTANCE"}'``

* Support for custom boot volume size and other node pool updates in the Container Engine for Kubernetes service

  * ``oci ce node-pool create --node-source-details`` with bootVolumeSizeInGBs in the complex type
  * ``oci ce node-pool create --node-boot-volume-size-in-gbs`` shortcut
  * ``oci ce node-pool update --node-source-details`` with bootVolumeSizeInGBs in the complex type
  * ``oci ce node-pool update --node-source-details --node-shape --node-metadata --ssh-public-key``

* Support for Data Guard on Exadata Cloud at Customer VM clusters in the Database service
 
  * ``oci db data-guard-association create from-existing-vm-cluster``

Fixed
~~~~~

* Multipart upload using ``oci os object bulk-upload`` may fail with SSL bad write error

2.12.7 - 2020-08-11
-------------------
Added
~~~~~

* Support for additional list filtering in the Data Catalog service

  * ``oci data-catalog <object type within catalog> list --display-name-contains``
  * ``oci data-catalog job-definition list --job-execution-state``

* Support for new db workload type AJD in the Autonomous Database service

  * ``oci db autonomous-database --db-workload AJD``

*  Support for script directory option for non-interactive installations on Mac, Linux, and Windows OS. (`Issue 282 <https://github.com/oracle/oci-cli/issues/282>`__) (`Issue 305 <https://github.com/oracle/oci-cli/issues/305>`__)

  * ``./install.sh --script-dir <directory>``
  * ``.\install.ps1 -ScriptDir <directory>``

Changed
~~~~~~~

* Idna package has been removed from the requirements. (`Issue 295 <https://github.com/oracle/oci-cli/issues/295>`__)

Fixed
~~~~~

* Bug fix in raw requests operations to correctly handle hyphens in headers. (`Issue 269 <https://github.com/oracle/oci-cli/issues/269>`__)

2.12.6 - 2020-08-04
-------------------
NOTE: OCI CLI is now available for install through Homebrew

  * ``brew update && brew install oci-cli``

Added
~~~~~

* Support to allow a customer to create and manage private endpoints in data-flow service.

  * ``oci data-flow application create private-endpoint-id``

* Support for Big Data service Change Shape and restart BDS node

  * ``oci bds instance change-shape``
  * ``oci bds instance restart-node``

* Support for Creating stacks from Compartment as part of Resource Manager service.
  * ``oci resource-manager stack create-from-compartment --compartment-id --config-source-compartment-id --config-source-region --config-source-services-to-discover``
  * ``oci resource-manager stack list-resource-discovery-services --compartment-id``

* Support for additional versions in BDS model, e.g. CSQL version

* Support for calling Oracle Cloud Infrastructure services in the Cardiff region (``--region uk-gov-cardiff-1``)

2.12.5 - 2020-07-28
-------------------
Added
~~~~~
* Support for specifying OS type and version when importing compute images in the Compute service

  * ``oci compute image import from-object --operating-system --operating-system-version``
  * ``oci compute image import from-object-uri --operating-system --operating-system-version``

* Support to change the fault domain for VM instances in the Compute service

  * ``oci compute instance update --fault-domain <fault-domain>``

* Support to update VM instances with different launch options (networking type, boot volume attachment type, and in-transit encryption for the boot volume's paravirtualized attachment) in the Compute service

  * ``oci compute instance update --launch-options <launch-options>``

* Support for 'Patch Now' Maintenance Runs for Autonomous Exadata Infrastructure and Autonomous Container Database resources in the Database service

  * ``oci db maintenance-run update --is-patch-now-enabled``

* Support for automatic performance and cost tuning on volumes in the Block Storage service

  * ``oci bv boot-volume create --is-auto-tune-enabled``
  * ``oci bv boot-volume update --is-auto-tune-enabled``
  * ``oci bv volume create --is-auto-tune-enabled``
  * ``oci bv volume update --is-auto-tune-enabled``

* Support for image capability schemas and schema versions as a part of the Compute Imaging Service

  * ``oci compute global-image-capability-schema``
  * ``oci compute global-image-capability-schema-version``
  * ``oci compute image-capability-schema``

* Support for calling Oracle Cloud Infrastructure services in the San Jose region (``--region us-sanjose-1``)

Fixed
~~~~~~~~
* Remove access_token from GitlabAccessTokenConfigurationSourceProvider model in the Resource Manager service

2.12.4 - 2020-07-21
-------------------
Added
~~~~~
* Added Instance License Type support for OCE instances

  * ``oci oce oce-instance create instance-license-type``
  * ``oci oce oce-instance update instance-license-type``


Fixed
~~~~~
* Bug fix in Key Management Service restore-from-file command to handle binary backup files

  * ``oci kms management vault restore-from-file``

2.12.3 - 2020-07-14
-------------------
Added
~~~~~
* Support for Oracle Blockchain Platform, a comprehensive distributed ledger cloud platform

  * ``oci blockchain``

* Support for Gitlab configuration source provider as part of the Resource Manager service

  * ``oci resource-manager configuration-source-provider``
  * ``oci resource-manager stack create-from-git-provider``
  * ``oci resource-manager stack update-from-git-provider``

* Support for switching over an Autonomous Database that has Data Guard enabled

  * ``oci db autonomous-database switchover --autonomous-database-id``

* Support for specifying that an autonomous database should have Data Guard enabled

  * ``oci db autonomous-database create --is-data-guard-enabled``
  * ``oci db autonomous-database create-refreshable-clone --is-data-guard-enabled``
  * ``oci db autonomous-database create-from-backup-id --is-data-guard-enabled``
  * ``oci db autonomous-database create-from-backup-timestamp --is-data-guard-enabled``
  * ``oci db autonomous-database create-from-clone --is-data-guard-enabled``
  * ``oci db autonomous-database list --is-data-guard-enabled``
  * ``oci db autonomous-database update --is-data-guard-enabled``

Changed
~~~~~~~
* Virtual Cloud Network List Endpoints Required param --vcn-id has been made optional

  * ``oci network dhcp-options list --vcn-id``
  * ``oci network internet-gateway list --vcn-id``
  * ``oci network local-peering-gateway list --vcn-id``
  * ``oci network route-table list --vcn-id``
  * ``oci network security-list list --vcn-id``
  * ``oci network subnet list --vcn-id``

2.12.2 - 2020-07-07
-------------------
Added
~~~~~
* Support for Autonomous DataWarehouse and Autonomous Transaction Processing features to allow switching from Non PE to PE (and vice versa) for existing databases as a part of the Database Service for Autonomous Databases

  * ``oci db autonomous-database update --private-endpoint-label``
  * ``oci db autonomous-database update --subnet-id``

* Support for private endpoint (ingress) and public endpoint whitelisting in Analytics Service

  * ``oci analytics analytics-instance create --network-endpoint-details``
  * ``oci analytics analytics-instance change-network-endpoint --network-endpoint-details``

* Support for re-encrypting an object in the Object Storage Service, by introducing a command line option to specify a new encryption key.

  * ``oci os object reencrypt``

* Support to register and deregister autonomous dedicated databases with Datasafe

  * ``oci db autonomous-database data-safe register``
  * ``oci db autonomous-database data-safe deregister``

2.12.1 - 2020-06-30
-------------------
Added
~~~~~
* Support for Usage API service

  * ``oci usage``

* Support for Oracle Cloud VMware Solution service

  * ``oci ocvs``

* Support for one-off patches in Database service

  * ``oci db database patch --one-off-patches``

* Support for Vlan features as part of support Layer 2 Virtual Networking

  * ``oci network vlan``
  * ``oci network private-ip list --vlan-id``
  * ``oci network vnic assign-private-ip --vlan-id``
  * ``oci compute instance attach-vnic --vlan-id``

* Validator parameter added for updating tags in Identity service

  * ``oci iam tag update --validator``

* Improve Create Instance Configuration to include the latest AttachVolumeDetails properties in the Compute Management service

  * ``oci compute-management instance-configuration create --instance-details``


2.12.0 - 2020-06-23
-------------------
Added
~~~~~

* Tagging support when creating database and db-home in the Database Service

  * ``oci db database create --defined-tags, --freeform-tags``
  * ``oci db database create-from-backup --defined-tags, --freeform-tags``
  * ``oci db database create-from-database --defined-tags, --freeform-tags``
  * ``oci db db-home create --defined-tags, --freeform-tags``

* Support for Data Integration Service

  * ``oci data-integration``

* Support for managing Autonomous VM Cluster resources at Customer Cloud.

  * ``oci db autonomous-vm-cluster``

* Support for backups on Autonomous Databases at Customer Cloud.

  * ``oci db autonomous-container-database create --db-unique-name``
  * ``oci db backup-destination create-nfs-details --local-mount-point-path, --mount-type-details``
  * ``oci db backup-destination update --nfs-mount-type, --nfs-server, --nfs-server-export``

* Support for a dependency archive zip file to be specified for use by an application for data flow service.

    * ``oci data-flow application create --archive-uri``

* Support for accessing data assets via private endpoint in the Data Catalog service

  * ``oci data-catalog catalog-private-endpoint``
  * ``oci data-catalog catalog attach``
  * ``oci data-catalog catalog detach``

* Support to get passphrase of export job

  * ``oci dts export get-passphrase --job-id``

* New parameter added to the following command

  * ``oci dts physical-appliance initialize-authentication --export-job-id``

Changed
~~~~~~~
* Parameters --appliance-label and --job-id are now optional for the following command

  * ``oci dts physical-appliance initialize-authentication``

* [BREAKING] for the Data Catalog service, the following parameters have been restricted to specific values.

  * ``lifecycle_state, wait-for-state, job_type, harvest_status, workflow_status, schedule_type``




2.11.1 - 2020-06-16
-------------------
Added
~~~~~

* Support creating a new database from another database for the Database service

  * ``oci db database create-from-database --point-in-time-recovery-timestamp``

* Support for the new DNS format of the Data Transfer service

* Support for Schedule-based Autoscaling via a new policy type (scheduled) in the Autoscaling service

* Support for enabling/disabling individual policies in the Autoscaling service

  * ``oci autoscaling policy update --is-enabled``

* Support for filtering lists by name, lifecycle state and sorting by value, order for compartments, dynamic group, group, identity provider, network sources, policy, user in the Identity Service

  * ``oci iam compartment list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam dynamic-group list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam group list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam identity-provider list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam network-sources list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam policy list --name --lifecycle-state --sort-by --sort-order``
  * ``oci iam user list --name --lifecycle-state --sort-by --sort-order``

* Support for filtering lists by name and lifecycle state for identity provider group in the Identity Service

  * ``oci iam identity-provider-group list --name --lifecycle-state``

Changed
~~~~~~~

* Added DB version field in Autonomous Container Database summary response for the Database service

  * ``oci db autonomous-database``

* DTS service endpoint is updated to ``https://datatransfer.{region}.oci.{secondLevelDomain}``

Fixed
~~~~~

* Bug fix in appliance-status update in ``oci dts export configure-physical-appliance``

2.11.0 - 2020-06-09
-------------------
Added
~~~~~

* Support for enabling File Server capability for an Integration Instance

  * ``oci integration integration-instance create --is-file-server-enabled``
  * ``oci integration integration-instance update --is-file-server-enabled``

* Support for deleting non empty tag namespace and bulk deleting tags

  * ``oci iam tag bulk-delete``
  * ``oci iam tag-namespace cascade-delete``

* Support bulk actions in Compartment Explorer

  * ``oci iam compartment bulk-move-resources``
  * ``oci iam compartment bulk-delete-resources``

* Support get, list commands for DB Patch for given DB Home

  * ``oci db patch list-db-home --db-home-id``
  * ``oci db patch get-db-home --db-home-id``

* Support get, list commands for DB Patch for given VM Cluster

  * ``oci db patch list-vm-cluster --vm-cluster-id``
  * ``oci db patch get-vm-cluster --vm-cluster-id``

* Support get, list commands for DB Patch History for given DB Home

  * ``oci db patch-history list-db-home --db-home-id``
  * ``oci db patch-history get-db-home --db-home-id``

* Support get, list commands for DB Patch History for given VM Cluster

  * ``oci db patch-history list-vm-cluster --vm-cluster-id``
  * ``oci db patch-history get-vm-cluster --vm-cluster-id``

* Support specifying a Patch Id and Patch Action when patching a VM Cluster.

  * ``oci db vm-cluster update --patch-id --patch-action``

* New parameter --include-root to include root compartment

  * ``oci iam compartment list --include-root``

* New entry in the User-Agent for CloudShell to differentiate between requests coming from CLI and CloudShell

Fixed
~~~~~

* The fields defindedTags and freeformTags of backupPolicy Complex Object in MySQL Service were invalid in the JSON output

  * ``oci mysql db-system create --generate-full-command-json-input``

Changed
~~~~~~~

* [BREAKING] Lifecycle state "OFFLINE" was removed and new state "DISCONNECTED" was added.

  * ``oci db exadata-infrastructure activate --wait-for-state``
  * ``oci db exadata-infrastructure create --wait-for-state``
  * ``oci db exadata-infrastructure delete --wait-for-state``
  * ``oci db exadata-infrastructure list --wait-for-state``
  * ``oci db exadata-infrastructure update --wait-for-state``

* Man page outputs for --help reformatted to line break on complete words

* ``--verify-native-dependencies`` option within install.py script is removed.

2.10.5 - 2020-06-02
-------------------
Added
~~~~~

* Support for Identity Provider

  * ``oci iam identity-provider create``
  * ``oci iam identity-provider list``
  * ``oci iam identity-provider get``
  * ``oci iam identity-provider delete``
  * ``oci iam identity-provider update``

* Support for getting image id of Image Listing Package in Marketplace Service

  * ``oci marketplace package get``

Changed
~~~~~~~

* Data Transfer Service

  * ``oci dts physical-appliance finalize``

    * Validates upload_user_config file and returns explicit config error message if invalid

  * ``oci dts export create``

    * Prevents export job create if bucket type is Archive

* Marketplace API updated to ignore signature parameter and mark it as deprecated

  * ``oci marketplace accepted-agreement delete --signature``

2.10.4 - 2020-05-19
-------------------
Added
~~~~~

* Support for Native JWT Validation in Oracle Cloud Infrastructure API Gateway service

  * ``oci api-gateway deployment create --specification``
  * ``oci api-gateway deployment update --specification``

* Support for Autonomous DataWarehouse and Autonomous Transaction Processing features as a part of the Database Service to display the Private IP for Private Endpoint Database service for Autonomous Databases

  * ``autonomous-database get --autonomous-database-id``

Fixed
~~~~~

* Combination of --stream-output, --all and --query with pagination was returning invalid JSON output.

  * ``oci audit event list``

* For CLI operations returning Unauthorized error, fixed bug where FileNotFoundError was displayed instead of error message.  (`Issue 280 <https://github.com/oracle/oci-cli/issues/280>`__)  (`Issue 278 <https://github.com/oracle/oci-cli/issues/278>`__)

2.10.3 - 2020-05-12
-------------------
Added
~~~~~

* Support for Drift Detection feature as part of Resource Manager Service

  * ``oci resource-manager stack detect-drift --stack-id``
  * ``oci resource-manager stack list-resource-drift-details --stack-id, --resource-drift-status``

Fixed
~~~~~

* ``oci session refresh`` was generating incorrect URL for gov regions.

2.10.2 - 2020-05-05
-------------------
Added
~~~~~

* Support for updating the license type of database systems in the Database service

  * ``oci db system update --license-model``

* Support for updating the version of 19c autonomous databases in the Database service

  * ``oci db autonomous-database update --db-version``

* Support for backup and restore functionality in the Key Management service

  * ``oci kms management vault backup``
  * ``oci kms management vault restore``
  * ``oci kms management vault restore-from-file``
  * ``oci kms management key backup``
  * ``oci kms management key restore``
  * ``oci kms management key restore-from-file``

* Support for calling Oracle Cloud Infrastructure services in the Hyderabad region (``--region ap-hyderabad-1``)

2.10.1 - 2020-04-28
-------------------
Added
~~~~~

* Support for the MySQL Database Service

  * ``oci mysql``

* Marketplace Service updates to support gov regions

  * ``oci marketplace agreement get --compartment-id``
  * ``oci marketplace agreement list --compartment-id``
  * ``oci marketplace category list --compartment-id``
  * ``oci marketplace package get --compartment-id``
  * ``oci marketplace package list --compartment-id``
  * ``oci marketplace listing get --compartment-id``
  * ``oci marketplace listing list --compartment-id``
  * ``oci marketplace publisher list --compartment-id``
  * ``oci marketplace report-collection list-reports --compartment-id``
  * ``oci marketplace report-type-collection list-report-types --compartment-id``

* Support for updating a dbHomeId of a database in the Database Service

  * ``oci db database update --db-home-id``

* Support for Instance Stop and Instance Start as part of the Integration Service

  * ``oci integration integration-instance stop --id``
  * ``oci integration integration-instance start --id``

* Support for Windows managed instances in OS Management

  * ``oci os-management managed-instance install-all-windows-updates``
  * ``oci os-management managed-instance install-windows-update``
  * ``oci os-management managed-instance list-available-windows-updates``
  * ``oci os-management managed-instance list-installed-windows-updates``


2.10.0 - 2020-04-21
-------------------
Added
~~~~~

* Support for Data Safe service

  * ``oci data-safe``

* Support for Incident Management and Creation service

 * ``oci support``

* Support for object versions in Object Storage

  * ``oci os object list-object-versions``
  * ``oci os bucket create --versioning``
  * ``oci os bucket update --versioning``
  * ``oci os object copy --source-version-id``
  * ``oci os object copy-part --source-version-id``
  * ``oci os object delete --version-id``
  * ``oci os object restore --version-id``
  * ``oci os object get --version-id``
  * ``oci os object head --version-id``
  * ``oci os object list --start-after``

* Support for user-provided encryption keys in Object Storage, by introducing optional parameters to specify a file containing the encryption key

  * ``oci os object put --encryption-key-file``
  * ``oci os object get --encryption-key-file``
  * ``oci os object head --encryption-key-file``
  * ``oci os object bulk-download --encryption-key-file``
  * ``oci os object bulk-upload --encryption-key-file``
  * ``oci os object copy --encryption-key-file --source-encryption-key-file``

* Support for managing shape compatibility entries for Compute images.

  * ``oci compute image-shape-compatibility-entry``

* Support for maintenance preferences while launching and updating an Exadata DB System.

  * ``oci db system launch --maintenance-window-details``
  * ``oci db system update --maintenance-window-details``

* Added new parameter ``--shape-config`` to specify number of cores when launching or updating a Compute instance.

  * ``oci compute instance launch``
  * ``oci compute instance update``

* Added new parameter ``--destination-region`` to support scheduled cross region backups for Boot Volumes

  * ``oci bv volume-backup-policy create``
  * ``oci bv volume-backup-policy update``

* New Attribute isFreeTierEnabled is included in the response of

  * ``oci db autonomous-db-version-list``

* New json input parameters are now available for ``oci compute-management instance-configuration create``

  * createVnicDetails

    * definedTags
    * freeformTags

  * instanceDetails.blockVolumes.createDetails

    * kmsKeyId
    * vpusPerGB

  * instanceDetails.launchDetails

    * shapeConfig
    * dedicatedVmHostId
    * launchMode
    * launchOptions
    * agentConfig
    * isPvEncryptionInTransitEnabled
    * preferredMaintenanceAction

Changed
~~~~~~~
* [BREAKING] Removed Stream Archiving

  * ``oci streaming admin archiver``

2.9.11 - 2020-04-14
-------------------
Added
~~~~~~

* Instance Access Type support for OCE instances

  * ``oci oce oce-instance create --instance-access-type --upgrade-schedule``

Fixed
~~~~~~~~

* Use client specific endpoint for clock skew check instead of always Compute

Changed
~~~~~~~

* Custom bashrc file is created on user input when default rc file is not found during CLI installation.

2.9.10 - 2020-04-07
-------------------
Added
~~~~~

* Support for getting usage of Vault in KMS Management Service.

  * ``oci kms management vault usage get``

* The ability to change the compartment of Runs and Applications in Data Flow Service.

  * ``oci data-flow application change-compartment``
  * ``oci data-flow run change-compartment``

* New options for stream-pool create/update in Streaming Service.

  * ``oci streaming admin stream-pool create --custom-encryption-key-details, --private-endpoint-details``
  * ``oci streaming admin stream-pool update --custom-encryption-key-details``

Fixed
~~~~~~~~

* Bug where uploading the zip file to model-artifact would fail

  * ``oci data-science model create-model-artifact --model-artifact-file --model-id``

2.9.9 - 2020-03-31
------------------
Added
~~~~~

* Support to allow update of class name, file URI, language and spark version of an existing application in the Data Flow service

  * ``oci data-flow application update --class-name, --file-uri, --language, --spark-version``

* Support for enabling and disabling the pod security policy admission controller in the Container Engine Service

  * ``oci ce cluster create | update --options '{"admissionControllerOptions": {"isPodSecurityPolicyEnabled": true}}'``

* Support for Cross Region Replication in the Object Storage Service

  * ``oci os replication create-replication-policy``
  * ``oci os replication delete-replication-policy``
  * ``oci os replication get-replication-policy``
  * ``oci os replication list-replication-policies``
  * ``oci os replication list-replication-sources``
  * ``oci os replication make-bucket-writable``

* Support for Retention Rules in the Object Storage Service

  * ``oci os retention-rule``

* Support for Big Data service

  * ``oci bds``

* Support for Secrets and Vault service

  * ``oci secrets``
  * ``oci vault``

Fixed
~~~~~

* Bug where checking the status of the boot volume backup copy operation would fail

  * ``oci bv boot-volume-backup copy``

Changed
~~~~~~~

* The following operations within the Data Transfer Service

  * ``oci dts export configure-physical-appliance`` is now idempotent

  *  Prompt requiring user confirmation when region values are different in config and config_upload_user in the following commands

    * ``oci dts job create``
    * ``oci dts physical-appliance finalize``

  * Perform deep-search and return additional appliance information instead of only appliance-label

    * ``oci dts job show``

  * User credentials validation step and check to determine if the specified bucket belongs to the specified compartment. Introduced new optional argument.

    * ``oci dts job create --skip-upload-user-check``

2.9.8 - 2020-03-24
------------------
Added
~~~~~

* Support for conditions in the JavaScript Challenge

  * ``oci waas js-challenge update``

* Support for new settings in Policy Config

  * ``oci waas policy-config update --load-balancing-method``
  * ``oci waas policy-config update --websocket-path-prefixes``
  * ``oci waas policy-config update --health-checks``

* Support for exclusions in Custom Protection Rules

  * ``oci waas custom-protection-rule list``

* Support for IP Address List in IP Whitelist

  * ``oci waas whitelist update``

* Support for WAF configuration for existing OCE instances

  * ``oci oce oce-instance update --waf-primary-domain``

* Support for Exacs database creation from backup

  * ``oci db database create-database-from-backup``

2.9.7 - 2020-03-17
------------------
Added
~~~~~

* Support for connecting to database system via terminal

  * ``oci db console-connection create --db-node-id --public-key``
  * ``oci db console-connection delete --console-connection-id --db-node-id --force``
  * ``oci db console-connection get --console-connection-id --db-node-id``
  * ``oci db console-connection list --db-node-id --all-pages``

Changed
~~~~~~~

* Upgraded dependency for configparser.

* ``--verify-native-dependencies`` option within install.py script is being deprecated.

2.9.6 - 2020-03-10
-------------------

Added
~~~~~

* New option for load balancer listener create/update.

  * ``oci lb listener create --connection-configuration-backend-tcp-proxy-protocol-version``
  * ``oci lb listener update --connection-configuration-backend-tcp-proxy-protocol-version``

* COMMON_ISSUES.rst file: includes common user installation issues and how to fix them.

Changed
~~~~~~~

* Bulk VNIC Data Fetch by compartment-id.

  *  ``--instance-id`` is optional for ``oci compute instance list-vnics --compartment-id``

* Creating a budgets alert rule.

  * ``--recipients`` is optional for ``oci budgets alert-rule create``

* Improved Installation experience by checking if Curl and Python are working in the system before using them.

2.9.5 - 2020-03-03
-------------------

Added
~~~~~

* Support for updating the shape of a Database System in the Database service

  * ``oci db system update --shape``

* Support for generating CPE Configuration for customer to download in the Networking service

  * ``oci network cpe get-cpe-device-config-content``
  * ``oci network cpe-device-shape list``
  * ``oci network cpe-device-shape-detail get-cpe-device-shape``
  * ``oci network tunnel-cpe-device-config``
  * ``oci network cpe create --cpe-device-shape-id``
  * ``oci network cpe update --cpe-device-shape-id``
  * ``oci network ip-sec-connection get-ipsec-cpe-device-config-content``

* Private IP and Fault Domain for Kubernetes cluster nodes in the NodePool response

* Support for calling Oracle Cloud Infrastructure services in the Montreal region (``--region  ca-montreal-1``)

Changed
~~~~~~~

* The following for the Data Transfer service

  * Notifications setup

    * ``oci dts job create`` has a new option called ``--setup-notificaitons``
    * ``oci dts appliance request`` has a new option called ``--setup-notificaitons``

  * Bug fixes in ``oci dts export configure-physical-appliance``

  * Prevent archive buckets for DTS export

* Upgraded dependencies for arrow, jmespath, python-dateutil, pytz, six.

Fixed
~~~~~

* Bug found in DB system patch command for Database Service. (`Issue 223 <https://github.com/oracle/oci-cli/issues/223>`__)

  * ``oci db system patch``

2.9.4 - 2020-02-25
-------------------

Added
~~~~~

* Support for OAuth 2.0 Client Credentials features as a part of the Identity User Service

  * ``oci iam user oauth2-credential create | delete | list | update``
  * ``oci iam user update-user-capabilities --can-use-o-auth2-client-credentials``

* Support for Private Endpoint Database service for Autonomous Databases

  * ``oci db autonomous-database create | create-from-backup-id | create-from-backup-timestamp | create-from-clone --nsg-ids --private-endpoint-label --subnet-id``
  * ``oci db autonomous-database update --nsg-ids``

* Support for restarting autonomous Database as part of Database service

  * ``oci db autonomous-database restart``

* Support for Identity IP Based Policy feature

  * ``oci iam network-sources create | delete | get | list | update``

* Support for Functions as a subscription of the Notifications service

  * ``oci ons subscription create --protocol ORACLE_FUNCTIONS``


2.9.3 - 2020-02-18
-------------------

Added
~~~~~

* Support for Oracle NoSQL Database Cloud (``nosql``)

  * ``oci nosql``

* List Db version by storage management type.

  * ``oci db version list --storage-management``

* Added instance type param for create operation to specify whether instance will be primary or non-primary.

  * ``oci oce oce-instance create --instance-usage-type``

Changed
~~~~~~~

* The `isEnabled` flag is returned for the Actions that are added to a Rule resource

  * ``oci events rule``

2.9.2 - 2020-02-11
-------------------

Added
~~~~~

* Installer now uses Python3 venv if installed instead of downloading Virtualenv

* Support for list Database versions command for Autonomous Database Serverless.

  * ``oci db autonomous-db-version list``

* Support for ``--db-version`` when provisioning Autonomous Database Serverless.

  * ``oci db autonomous-database create --db-version``
  * ``oci db autonomous-database create-from-clone --db-version``
  * ``oci db autonomous-database create-from-backup-id --db-version``
  * ``oci db autonomous-database create-from-backup-timestamp --db-version``
  * ``oci db autonomous-database list --db-version``

Changed
~~~~~~~

* Compute Volume Attachment list now can get compartment-id by instance-id.

  * ``oci compute volume-attachment list --compartment-id (required to optional)``

2.9.1 - 2020-02-04
-------------------

Added
~~~~~

* Support for Data Science Service

  * ``oci data-science``

* Support for new OCI regions ``ap-osaka-1`` and ``ap-melbourne-1``.

2.9.0 - 2020-01-28
-------------------

Added
~~~~~

* Support for Data Catalog Service

  * ``oci data-catalog``

* Support for Data Flow Service

  * ``oci data-flow``

* Support for Application Migration Service

  * ``oci application-migration``

* Support for offline data export in the Data Transfer Service

  * ``oci dts export``

* Support for cross shape Data Guard. Customer to provide shape information when setting up Data Guard association.

  * ``oci db data-guard-association create with-new-db-system --shape``

Changed
~~~~~~~

* [Breaking] ``oci oce cluster create --dashboard-enabled`` is now disabled by default.

2.8.2 - 2020-01-21
-------------------

Added
~~~~~

* Support for getting DRG redundancy status in the Networking service

  * ``oci network drg-redundancy-status get --drg-id``

* Support for cloning autonomous databases from backups in the Database service

  * ``oci db autonomous-database create-from-backup-id``
  * ``oci db autonomous-database create-from-backup-timestamp``

2.8.1 - 2020-01-14
-------------------
Added
~~~~~

* Support for description field to Route rule and Security rules.

  * ``oci route-table create``
  * ``oci route-table update``
  * ``oci security-list create``
  * ``oci security-list update``

* Support for create, get, delete, list commands for db-home command

  * ``oci db db-home create --db-system-id <Db System OCID> --db-version <Database Version>``
  * ``oci db db-home get --db-home-id <Db Home OCID>``
  * ``oci db db-home delete --db-home-id <Db Home OCID>``
  * ``oci db db-home list --compartment-id <compartment OCID>``

* Support for stopping and starting Digital Assistant Instances

  * ``oci oda instance start``
  * ``oci oda instance stop``

* Support for specifying db home when a creating database.

  * ``oci db database create --db-home-id <Db Home OCID>``

* Support for --backup-id parameter in the list database command

  * ``oci db database list --backup-id <backup OCID>``

Fixed
~~~~~

* Crytography package requirement bumped to version 2.8 to fix a compatibility issue with Python 3.8

* OCI CLI installation now works with virtualenv or venv name as "oci_cli" (`Issue 213 <https://github.com/oracle/oci-cli/issues/213>`__)

2.8.0 - 2020-01-07
-------------------
Added
~~~~~

* Improved configuration of the maintenance window details for Autonomous Container Database by adding the option in the Database Service

  * ``oci db autonomous-container-database create --maintenance-window-details``
  * ``oci db autonomous-container-database update --maintenance-window-details``

Changed
~~~~~~~

* Corporate proxy field is now optional when a creating exadata infrastructure.

  * ``oci db exadata-infrastructure create --corporate-proxy``

* [Breaking] Hostname field within Node details which is part of VM Networks field is now required

  * ``oci db vm-cluster-network update --vm-networks``

Fixed
~~~~~

* `--all` option for ``api-gateway`` list commands

  * ``oci api-gateway deployment list``
  * ``oci api-gateway gateway list``

2.7.0 - 2019-12-17
-------------------
Added
~~~~~

* Support for Oracle Cloud Infrastructure API Gateway service

  * ``oci apigateway``

* Boot volumes support for cross-region backups in Block Volume Service

  * ``oci bv boot-volume-backup copy``
  * ``oci bv boot-volume-backup list --source-boot-volume-backup-id``

* Support for managing TSIG Key resources in the DNS service.

  * ``oci dns tsig-key``

* Support for referencing TSIG Key resources by OCID within Zone resources in the DNS service.

  * ``oci dns zone create --external-masters``
  * ``oci dns zone update --external-masters``

* Removed Identity Cloud service(idcs) access token requirement for Container Engine delete operation. Also, support secondary idcs stripe for Container Engine creation.

  * ``oci oce oce-instance delete``
  * ``oci oce oce-instance create --identity-stripe``

* Support to resize compute virtual machine instance to a different shape in Compute Service.

  * ``oci compute instance update --id <id> [--shape <shape>]``

* Support for OS Management Service.

  * ``oci os-management``

* Improve nodepool creation, specify the image of the nodes by the image OCID in the Container Engine Service.

  * ``oci ce node-pool create --node-image-id``

* Add management configuration for oracle-cloud-agent in Compute Service

  * ``oci compute instance launch --agent-config``

* Support for Marketplace Service.

  * ``oci marketplace``

* Allow customers to bring their own keys to Key Management Service.

  * ``oci kms management get-wrapping-key``
  * ``oci kms management import-key``
  * ``oci kms management import-key-version``

* Allow customers to create and use new vault with "DEFAULT" as type in Key Management Service

  * ``oci kms management key-version cancel-key-version-deletion --key-id, --key-version-id``
  * ``oci kms management key-version schedule-key-version-deletion --key-id, --key-version-id, --time-of-deletion``

Changed
~~~~~~~

* [Breaking] Removed support for v1 auth tokens (1.0.0) in kubeconfig files in Container Engine Service.

  * ``oci ce cluster create-kubeconfig --token-version``

* Enable updating a stream pool name and modified existing commands in Streaming Service.

  * ``oci streaming admin stream list --compartment-id (required to optional)``
  * [Breaking] `` oci streaming admin stream-pool list --compartment-id (optional to required)``
  * ``oci streaming admin stream-pool update --name (new param added)``

2.6.15 - 2019-12-10
-------------------
Added
~~~~~~
* Support for Stream Pools and Connect Harness

  * ``oci streaming admin connect-harness``
  * ``oci streaming admin stream-pool``

* Support for recovering the compartment from DELETED state to ACTIVE state.

  * ``oci iam compartment recover``

* Support for multi-attach feature for block storage.

  * ``oci compute volume-attachment attach --is-shareable``
  * ``oci compute volume-attachment attach-iscsi-volume --is-shareable``
  * ``oci compute volume-attachment attach-paravirtualized-volume --is-shareable``

* New parameters added to ``oci os object put`` command.

  * ``oci os object put --cache-control --content-disposition``

Changed
~~~~~~~
* Improved retry strategy for multipart uploads.

* Modified stream create to make compartment ID optional and include stream pool id parameter

  * ``oci streaming admin stream create --compartment-id, --stream-pool-id``
  * ``oci streaming admin stream list --stream-pool-id``
  * ``oci streaming admin stream update --stream-pool-id``

2.6.14 - 2019-11-26
-------------------
Added
~~~~~
* get the OCPUs info of an exadata infrastructure instance for ATP-D

  * ``oci db exadata-infrastructure get-compute-units --autonomous-exadata-infrastructure-id``

Changed
~~~~~~~
* Added timeMaintenanceBegin & timeMaintenanceEnd to autonomous database api response
* Inline help text has been removed, ``--help`` will still work as normal

Fixed
~~~~~
* ``oci waas policy-config update`` command which now takes multiple values for ``--tls-protocols`` option

2.6.13 - 2019-11-19
-------------------
Added
~~~~~
* Support for Autonomous Database to create and update with whitelisted ips.

  * ``oci db autonomous-database create --whitelisted-ips``
  * ``oci db autonomous-database update --whitelisted-ips``

* Support for Four Byte ASN support for Fast-Connect.

* Ability to choose fault domains when creating instance pools.

  * ``oci compute-management instance-pool create``

Fixed
~~~~~
* Broken links in help documents.

2.6.12 - 2019-11-12
-------------------
Added
~~~~~
* Support to register and deregister an autonomous data warehouse, or autonomous transaction processing, database with Data Safe.

  * ``oci db autonomous-database data-safe register --autonomous-database-id <autonomous database OCID>``
  * ``oci db autonomous-database data-safe deregister --autonomous-database-id <autonomous database OCID>``

* Add capability to redirect an input HTTP/HTTPS request URI to a different URI in Load Balancer service.

  * ``oci lb rule-set create --items``

* Console access to APEX and SQL Dev features for Create and Update ATP/ADW in the Database service

* Support for Volume Performance Units for Block Volumes in Block Storage service.

  * ``oci bv boot-volume create --vpus-per-gb``
  * ``oci bv boot-volume update --vpus-per-gb``

* Support for specifying compartment for OKE options APIs

  * ``oci ce cluster-options get --compartment-id``
  * ``oci ce node-pool-options get --compartment-id``

* Support for HTTP raw requests

  * ``oci raw-request``

* Deprecation warning message for python 2. This can be turned-off by setting the environment variable ``SUPPRESS_PYTHON2_WARNING``.

Changed
~~~~~~~
* Removed deprecated ``bmcs`` entry point for CLI. Now only ``oci`` is supported.

2.6.11 - 2019-11-5
-------------------
Added
~~~~~
* Support for Analytics Service (``oci analytics``)

* Support for Oracle Integration Service (``oci integration``)

* Support for adding optional parameter to IPSecconnection in Core Service.

  * ``oci network ip-sec-connection update --ike-version``

* Support for GetStackTfState API as part of Resource Manager service.

  * ``oci resource-manager stack get-stack-tf-state --file, --stack-id``



2.6.10 - 2019-10-29
-------------------
Added
~~~~~
* Support for retrieving metadata for Autonomous Wallet, both regional and instance, as well as requesting rotation of Autonomous Wallets, both regional instance. Generate wallet now allows for specifying the wallet type to download, All or Single.

  * ``oci db autonomous-database get-metadata --id <an OCID of an autonomous database>``
  * ``oci db autonomous-database get-regional-wallet-metadata``
  * ``oci db autonomous-database-wallet rotate --should-rotate true --id <an OCID of an autonomous database>``
  * ``oci db autonomous-database-wallet rotate-regional-wallet --should-rotate true``
  * ``oci db autonomous-database generate-wallet --generate-type ALL``
  * ``oci db autonomous-database generate-wallet --generate-type SINGLE``

* Support for adding and removing image shape compatibility entries

   * ``oci compute image-shape-compatibility-entry add``
   * ``oci compute image-shape-compatibility-entry remove``

* Support for managing redirects (e.g. create, update, delete, get list)

  * ``oci waas http-redirect change-compartment --compartment-id, --http-redirect-id``
  * ``oci waas http-redirect create --compartment-id, --domain, --target, --defined-tags, --display-name, --freeform-tags, --response-code``
  * ``oci waas http-redirect delete --http-redirect-id, --force``
  * ``oci waas http-redirect get --http-redirect-id``
  * ``oci waas http-redirect list --compartment-id, --all-pages, --display-name, --id, --time-created-greater-than-or-equal-to, --time-created-less-than``
  * ``oci waas http-redirect update --http-redirect-id, --defined-tags, --display-name, --force, --freeform-tags, --response-code, --target``

* Support for migrating Dyn HTTP Redirect Service to OCI DNS

  * ``oci dns zone migrate-from-dynect``

Changed
~~~~~~~
* ``oci setup oci-cli-rc`` will try to create the directory for the oci_cli_rc file, if it does not exist.

Fixed
~~~~~
* Added validation check for thread count ``--parallel-upload-count`` and also improved error message when threads are exhausted.

* Upload parts in ``oci os object put`` now correctly limited to 10000 parts

* Updated help messages for the overwrite and no-overwrite flags in object storage operations

  * ``oci os object bulk-upload --overwrite --no-overwrite``
  * ``oci os object put --overwrite --no-overwrite``

* Using ``oci os object bulk-download`` correctly prints out downloaded objects in a new line instead of overwriting the same line

* Problem with ``oci setup`` when there were spaces in a user's profile name on Windows.

* Data Transfer Service - Fix the broken output string for showing progress during command

  * ``oci dts nfs-dataset seal``

* Data Transfer Service - Provide help string to monitor progress after running the command

  * ``oci dts nfs-dataset seal``

* Typo in the install README

2.6.9 - 2019-10-15
-------------------
Added
~~~~~
* Support for Digital Assistant service

  * ``oci oda``
* Includes the ``opc-workrequest-id`` in the response header of 3 APIs belonging to Instance Pools
* Support for the following environment variables for CLI:

  * OCI_CLI_PROFILE
  * OCI_CLI_REGION
  * OCI_CLI_USER
  * OCI_CLI_FINGERPRINT
  * OCI_CLI_KEY_FILE
  * OCI_CLI_TENANCY
  * OCI_CLI_ENDPOINT
  * OCI_CLI_CONFIG_FILE
  * OCI_CLI_RC_FILE
  * OCI_CLI_CERT_BUNDLE
  * OCI_CLI_AUTH
  * OCI_CLI_DELEGATION_TOKEN_FILE
  * OCI_CLI_SECURITY_TOKEN_FILE

Fixed
~~~~~
* Fix Json output format for "oci audit event list" with streaming enabled and when output is null. (`Issue 204 <https://github.com/oracle/oci-cli/issues/204>`__)
* Fix User can update database with backup-destination.

  * ``oci db database update --backup-destination``
* Fix CLI Installation issue if the installation path contains ``oci_cli``
* Fix Windows issue where there is a local account and network account with the same username causing permission problems during ``oci setup bootstrap``.
* Fix Windows issue where profile created by ``New-Item -Path $Profile -Type File`` can not be updated for autocomplete by the CLI installer.
* Fix CLI pytest failures caused by unpinned dependency (pytest-forked v1.0.2) of a pinned dependent package (pytest-xdist) getting updated to a new incompatible version (pytest-forked v1.1.1)

2.6.8 - 2019-10-08
-------------------
Added
~~~~~
* Support for Health Checks API regional behavior changed to support OCI Monitoring integration and DNS Traffic Management dependencies (``oci health-checks``)

  * ``oci health-checks ping-monitor list --home-region``
  * ``oci health-checks http-monitor list --home-region``

* Support for create/update/delete/list new custom scheduled backup policies. Customers will be able to determine the frequency of the backup, time of day, type of backup and time to retain the backup. Policies will be assigned to volumes the same as the current predefined policies.

  * ``oci bv volume-backup-policy create``
  * ``oci bv volume-backup-policy update``
  * ``oci bv volume-backup-policy delete``

* Support for specifying network type when launching VM instances by introducing launch-options option in the compute service

  * ``oci compute instance launch --launch-options``

* Adding entitlements request and show capabilities to Data Transfer Service (``oci dts``)

* CLI options for DTS Appliance Request and Update have been updated to conform with old CLI version (``oci dts appliance request`` and ``oci dts appliance update-shipping-address``)


Fixed
~~~~~
* Object storage bulk upload verify checksum now works when in FIPS mode.

  * ``oci os object bulk-upload --verify-checksum``

2.6.7 - 2019-10-01
-------------------
Added
~~~~~
* Support for tag definition validators in the Tag object used by get, list, create, and update tag. Currently the only tag validator is the Enum validator.
* Improvement to provisioning time for launching VMDB instance in DBaaS.

  * ``oci db system launch --storage-management``
  * ``oci db system launch-from-backup --storage-managament``
* Support for migrating zones from Dyn Managed DNS to OCI Public DNS.

  * ``oci dns zone migrate-from-dynect``
* Support for resource principal authorization type, ``--auth resource_principal``.
* New field added to Tag Default object ``isRequired`` to designate that a value must be provided for the tag upon resource creation.
* New API ``assembleEffectiveTagSet`` added to conveniently get all tags that must be applied to a resource in a given compartment.
* Add new API to list work requests for tagging, as well as APIs to list logs and errors for those work requests.

  * ``oci iam tagging-work-request get``
  * ``oci iam tagging-work-request list``
  * ``oci iam tagging-work-request-error list``
  * ``oci iam tagging-work-request-log list``
* Support for change of compartments for DRG in the Networking Service

  * ``oci network drg change-compartment --compartment-id, --drg-id``
* Support for Oracle Linux 8.

* Support for multiple ``--wait-for-state`` parameters. You can specify multiple ``--wait-for-state`` parameters for any supporting command and it will return on the first seen state. For example, ``--wait-for-state AVAILABLE --wait-for-state FAILED`` will return on whichever lifecycle state is observed first.

Changed
~~~~~~~
* Updates the API endpoint URL for Oracle Functions to be of the form ``*.oci.oraclecorp.com``.


2.6.6 - 2019-09-24
-------------------
Added
~~~~~
* ``--verify-checksum`` option for the following commands: ``oci os object put`` and ``oci os object bulk-upload``. This option will print a message indicating whether the checksum for the uploaded file matches the local file. Sample message: 'md5 checksum matches [Local: AikPDj8xbhaUNKeS956p1A==]'

* Support for re-encrypting a bucket.

  * ``oci os bucket reencrypt --namespace-name --bucket-name``

* Support for enabling/disabling bucket level events.

  * ``oci os bucket create --object-events-enabled``
  * ``oci os bucket update --object-events-enabled``

* Improve Autonomous Database to change the whitelist ips feature.

  * ``oci db autonomous-database update --whitelisted-ips``

* Support for Autonomous Database to create with the whitelist ips feature.

  * ``oci db autonomous-database create --whitelisted-ips``

Changed
~~~~~~~
* Default CreateKubeconfig so it uses token version 2.0.0

  * ``oci ce cluster create-kubeconfig``

Fixed
~~~~~
* ``oci session authenticate`` was not correctly redirecting to the correct URL for government regions

2.6.5 - 2019-09-17
-------------------
Added
~~~~~~
* Support for backup destination(nfs, zdlra) as a part of database backup service for its create, read, update and delete operations.

  * ``oci db backup-destination create-nfs-details``
  * ``oci db backup-destination get``
  * ``oci db backup-destination update``
  * ``oci db backup-destination delete``

* Support for backup destination in create and update database.

  * ``oci db database create --backup-destination``
  * ``oci db database create --backup-destination``

* Support for managing Exadata Infrastructure resources at Customer Cloud.

  * ``oci db exadata-infrastructure``

* Supports for managing VM Cluster Network resources at Customer Cloud.

  * ``oci db vm-cluster-network``

* Support for managing VM Cluster resources at Customer Cloud.

  * ``oci db vm-cluster``

* Support for getting a list of supported GI versions for VM Cluster.

  * ``oci db gi-version``

* Support for creating new databases on VM Cluster.

  * ``oci db database create``

* Support for listing databases within a VM Cluster instead of a Db System.

  * ``oci db database list --vm-cluster-id``

* Support for getting a list of database nodes in the specified VM Cluster.

  * ``oci db node list --vm-cluster-id``

* Support for ``create-import-tf-state-job`` command in Resource Manager.

* Separated ``resource-manager job create`` into operation-specific commands.

  * ``oci resource-manager job create-plan-job``
  * ``oci resource-manager job create-apply-job``
  * ``oci resource-manager job create-destroy-job``
  * ``oci resource-manager job create-import-tf-state-job``
  * ``oci resource-manager job resource-manager job create`` is now deprecated.

2.6.4 - 2019-09-10
-------------------
Added
~~~~~
* Support for CreateKubeconfig token version 2.0.0.

  * ``oci ce cluster generate-token``

* Support creating and updating node pool using regional subnets.

  * ``oci ce node-pool create --size --placement-configs``
  * ``oci ce node-pool update --size --placement-configs``

* Support for using KMS to encrypt Kubernetes secret.

  * ``oci ce cluster create --kms-key-id``

* Support for user to specify a two hour window when the auto-backup would kick in. Default is anytime. Example values are SLOT_ONE, SLOT_TWO.

  * ``oci db database create --auto-backup-window``
  * ``oci db database update --auto-backup-window``

* Support for specifying ``nsgIds`` parameter for ``LaunchAutonomousDbSystemDetails`` and ``UpdateAutonomousDbSystemDetails``

  * ``oci db autonomous-exadata-infrastructure launch --nsg-ids``
  * ``oci db autonomous-exadata-infrastructure update --nsg-ids``

* Support for Oracle Content and Experience service.

  * ``oci oce``

* New read-only `system-tags` parameter for Load Balancer object.

Fixed
~~~~~
* Outdated doc link. (`Pull Request <https://github.com/oracle/oci-cli/pull/186/files>`__)

* Downloads that fail when ``oci os object --bulk-download`` when object names ended with a '/'.

2.6.3 - 2019-09-03
-------------------
Added
~~~~~
* Support for Cluster Networks as part of the Compute Management Service

  * ``oci compute-management cluster-network``

* Made session token file permissions restricted to the file owner only.

Fixed
~~~~~
* CVE-2017-18342 - In PyYAML before 4.1, the yaml.load() API could execute arbitrary code. In other words, yaml.safe_load is not used.

2.6.2 - 2019-08-27
-------------------
Added
~~~~~
* Support for Dedicated Virtual Machine Host feature as a part of the Compute Service.

  * ``oci compute dedicated-vm-host``
  * ``oci compute dedicated-vm-host-instance``

* Support for using resource groups in Monitoring Service.

  * ``oci monitoring alarm create --resource-group [text]``
  * ``oci monitoring alarm update --resource-group [text]``
  * ``oci monitoring metric list --resource-group [text]``
  * ``oci monitoring metric-data summarize-metrics-data --resource-group [text]``

2.6.1 - 2019-08-20
-------------------
Added
~~~~~
* Support for kms encryption of file system in the File Storage Service.

  * ``oci fs file-system create --kms-key-id``
  * ``oci fs file-system update --kms-key-id``

* Support for an option to set up archiving to Object Storage in the Streaming Service.

  * ``oci streaming admin archiver``

* Support for interacting with the resource limits of a specific resource type in the Limits Service.

  * ``oci limits definition list``
  * ``oci limits resource-availability get``
  * ``oci limits service list``
  * ``oci limits value list``

* Support for ETag on Streaming Resources.

  * ``oci streaming admin stream delete --if-match``
  * ``oci streaming admin stream update --if-match``

* Support for change of compartments for Public IP, Dhcp Options, Local Peering Gateway, Internet Gateway, Network Security Group (nsg) resources in the Networking Service.

  * oci network internet-gateway change-compartment --compartment-id, --ig-id
  * oci network dhcp-options change-compartment --compartment-id, --dhcp-id
  * oci network local-peering-gateway change-compartment --compartment-id, --local-peering-gateway-id
  * oci network nsg change-compartment --compartment-id, --nsg-id
  * oci network public-ip change-compartment --compartment-id, --public-ip-id

* Support for AddressLists resource management in the WAF Policy Service:

  * ``oci waas address-list``

* Support for clearing cached resources in Edge nodes in the WAF Policy Service.

  * ``oci waas purge-cache --waas-policy-id, --resources``

* Support for Cache control in WAF Policy Service

  * ``oci waas caching-rule list``
  * ``oci waas caching-rule update``

* Support for Custom Protection Rule resource management in the WAF Policy Service.

  * ``oci waas customer-protection-rule``
  * ``oci waas waas-policy custom-protection-rule list``

* Improve support for WAF Policy settings by introducing new options in the WAF Policy Service.

  * ``oci waas policy-config update --cipher-group, --client-address-header, --force, --is-behind-cdn, --is-cache-control-respected, --is-origin-compression-enabled, --is-response-buffering-enabled, --tls-protocols``

* Improve support for WAF Policy by introducing custom-protection-rule usage configuration in the WAF Policy Service.

  * ``oci waas waas-policy custom-protection-rule list --waas-policy-id, --action, --all-pages, --mod-security-rule-id``

* Improve support for WAF Policy sercice by introducing new Origin Groups option in the WAF Policy Service.

  * ``oci waas waas-policy create --origin-groups``
  * ``oci waas waas-policy update --origin-groups``

* Improve support for WAF config in WAF Policy service by introducing options for caching-rules, custom-protection-rules and origin-groups in the WAF Policy Service.

  * ``oci waas waf-config update --caching-rules, --custom-protection-rules, --origin-groups``

* Launching database system with --auto-backup-enabled and --recovery-window-in-days options in the Database Service.

  * ``oci db system launch --auto-backup-enabled and --recovery-window-in-days``

Fixed
~~~~~~~
* os bulk-delete did not print long object names that ended with slash

2.6.0 - 2019-08-13
-------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Zurich region (``--region eu-zurich-1``)

* Support for Data Transfer Service

  * ``oci dts``

Fixed
~~~~~~~
* JSON input generation for certain commands

* Help text for certain commands was displaying required parameters as optional

* Links to GitHub examples are being updated in the changelog itself.

Updated
~~~~~~~
* [Breaking] Changes to response structure for certain WAF commands

  * ``oci waas``

2.5.22 - 2019-08-06
---------------------
Added
~~~~~
* Support for Enabling IPV6 support in the networking service:

  * ``oci network ipv6 list --subnet-id``
  * ``oci network ipv6 get --ipv6-id``
  * ``oci network ipv6 update --ipv6-id``
  * ``oci network ipv6 delete --ipv6-id``

* Support for IPV6 load balancers by providing ``--ip-mode`` option for the load-balancer create command.

  * ``oci lb load-balancer create --ip-mode``

* Support for private IPv6 addressing to establish the BGP peering for FastConnect Service.

  * Adding oracleBgpPeeringIpv6 and customerBgpPeeringIpv6 fields to JSON object CrossConnectMappings (``oci network virtual-circuit create --cross-connect-mappings``)

Removed
~~~~~~~
* Dependency on httpsig_cffi package

Updated
~~~~~~~
* Check for service directory import to include 'dist-packages'

2.5.21 - 2019-07-30
---------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Mumbai region (``--region ap-mumbai-1``)

* Support for change of compartments for WAF policy and Certificate resources in WAF Policy Service.

  * ``oci waas waas-policy change-compartment --waas-policy-id  --compartment-id``
  * ``oci waas certificate change-compartment --certificate-id  --compartment-id``

* Support for change of compartments for Customer Premise Equipment (CPE), IPSecConnection, Cross connect group, Cross connect, Remote Peering Connection (RPC) and Virtual Circuit resources in the Networking service.

  * ``oci network cpe change-compartment --cpe-id  --compartment-id``
  * ``oci network ip-sec-connection change-compartment --ip-sec-connection-id  --compartment-id``
  * ``oci network cross-connect-group change-compartment --cross-connect-group-id  --compartment-id``
  * ``oci network cross-conenct change-compartment --cross-connect-id  --compartment-id``
  * ``oci network remote-peering-connection change-compartment --remote-peering-connection-id  --compartment-id``
  * ``oci network virtual-circuit change-compartment --virtual-circuit-id  --compartment-id``

* Support for Events Service

  * ``oci events``
  * An example on using the Events Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/events/examples_and_test_scripts/events_example.sh>`__.

* Support for adding tags to Cross connect group, Cross connect, Remote Peering Connection and Virtual Circuit resources in the Networking Service.

  * ``oci network cross-connect-group create --defined-tags --freeform-tags``
  * ``oci network cross-connect-group update --defined-tags --freeform-tags``
  * ``oci network cross-connect create --defined-tags --freeform-tags``
  * ``oci network cross-connect update --defined-tags --freeform-tags``
  * ``oci network remote-peering-connection create --defined-tags --freeform-tags``
  * ``oci network remote-peering-connection update --defined-tags --freeform-tags``
  * ``oci network virtual-circuit create --defined-tags --freeform-tags``
  * ``oci network virtual-circuit update --defined-tags --freeform-tags``

* Support for moving streams into a different compartment in Streaming service

  * ``oci streaming admin stream change-compartment [OPTIONS]``

2.5.20 - 2019-07-23
-------------------
Added
~~~~~
* Support for moving alarm compartment in Monitoring Service.

  * ``oci monitoring alarm change-compartment --alarm-id --compartment-id``

* Support for Cost Tracking Tag Budget Alert in Budget Service

  * --target-type option for ``oci budgets budget create``
  * --targets option for ``oci budgets budget create``
  * --target-type option for ``oci budgets budget list``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/budget/examples_and_test_scripts/budget_example.sh)>`__.

* Ability to create instance configuration from a running instance.

  * ``oci compute-management instance-configuration create``
  * ``oci compute-management instance-configuration create-from-instance``

* Support for change compartment feature for Autonomous Container Database, Autonomous Database, Autonomous Exadata Infrastructure, and DB Systems as a part of the Database Service

  * ``oci db autonomous-container-database change-compartment``
  * ``oci db autonomous-database change-compartment``
  * ``oci db autonomous-exadata-infrastructure change-compartment``
  * ``oci db system change-compartment``

* Ability to change a compartment for health check monitors.

  * ``oci health-checks ping-monitor change-compartment``
  * ``oci health-checks http-monitor change-compartment``

Changed
~~~~~~~
* Examples have been distributed into subdirectories under the services directory.

  * For example, database examples will now be found under `services/database/examples_and_test_scripts` and so on for other services.
  * `services/core/examples_and_test_scripts` will contain examples for compute, networking, block volume, etc.


2.5.19 - 2019-07-16
-------------------
Added
~~~~~
* Support for moving KMS keys and vaults across compartments.

  * ``oci kms management vault change-compartment --compartment-id``
  * ``oci kms management key change-compartment --compartment-id``

* Support for Service Gateway Transit Routing feature.

  * Ability to associate route table when creating service-gateway (``oci network service-gateway create --route-table-id``)
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/create_service_gateway_example.sh>`__.

* Support for moving compartment tree to a different parent compartment

  * ``oci iam compartment move``

* Support for LB Cookie Session Persistence in LB backend sets

  * ``oci lb backend create --lb-cookie-session-persistence-configuration``

* Support for REST method restrictions in Load Balancer rule sets.

* Support for adding AllowRules to a RuleSet for access control by source IP address.

  * ``oci lb load-balancer create --rule-sets``

* Support for listing a summary of rules for a listener

  * ``oci lb listener-rule list``

* Support for changing the compartment of an instance in the Compute service

  * ``oci compute instance change-compartment``
  * An example can be found here: `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/change-compartment.sh>`__
  * An example using work requests to determine status can be found here: `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/change-compartment-using-work-request-id.sh>`__

* Support for using kms key when copying volume backups

  * ``oci bv backup copy --kms-key-id``

* Support for moving a Topic across compartments:

  * ``oci ons topic change-compartment --topic-id --compartment-id``

* Support for moving a Subscription across compartments

  * ``oci ons subscription change-compartment --subscription-id --compartment-id``

* Support for moving a DNS Zone compartment.

  * ``oci dns zone change-compartment --zone-id --compartment-id``

* Support for moving a DNS Steering Policy compartment.

  * ``oci dns steering-policy change-compartment --steering-policy-id --compartment-id``

* Support for moving Load Balancers between compartments

  * ``oci lb load-balancer change-compartment``

* Support for managing Compartment Resource Quotas

  * ``oci limits quota``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/limits/examples_and_test_scripts/quotas_example.sh>`__.

* Support for Oracle Functions

  * ``oci fn``
  * An example on using Oracle Functions can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/functions/examples_and_test_scripts/functions_example.sh>`__.

Fixed
~~~~~
* Service error for ``oci bv backup copy`` command when `wait-for-state` option is passed.

Changed
~~~~~~~
* Man pages for the commands now display Required, Optional and Global parameters if available.
* Updates for `CLI Command Reference <https://docs.cloud.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/>`__ pages.

2.5.18 - 2019-07-09
-------------------
Added
~~~~~
* Support to managing lb attachments for instance pools

  * ``oci compute-management instance-pool lb-attachment get``
  * ``oci compute-management instance-pool lb-attachment attach``
  * ``oci compute-management instance-pool lb-attachment detach``

* Support for specifying nsgIds and backupNetworkNsgIds parameters for LaunchDbSystemDetails, LaunchDbSystemFromBackupDetails and UpdateDbSystemDetails

  * ``oci db system launch --backup-network-nsg-ids --nsg-ids``
  * ``oci db system launch-from-backup --backup-network-nsg-ids --nsg-ids``
  * ``oci db system launch-from-database --backup-network-nsg-ids --nsg-ids``
  * ``oci db system update --backup-network-nsg-ids --nsg-ids``

* Support for Managing Network Security Group

  * ``oci network nsg create | get | update | delete | list``
  * ``oci network nsg rules add | update | remove | list``

* Support for associating a Vnic with a Network Security Group

  * ``oci network vnic update --nsg-ids``
  * ``oci network nsg vnics list``

* Support for associating primary Vnic with a Network Security Group

  * ``oci compute instance launch --nsg-ids``
  * ``oci compute instance attach-vnic --nsg-ids``

* Support for network security groups in LBaaS

  * ``oci lb network-security-groups update``

* Support for moving VCN compartment in Core Service.

  * ``oci network vcn change-compartment --vcn-id  --compartment-id``

* Support for moving Subnet compartment in Core Service.

  * ``oci network subnet change-compartment --subnet-id  --compartment-id``

* Support for moving RouteTable compartment in Core Service.

  * ``oci network route-table change-compartment --vcn-id  --compartment-id``

* Support for moving SecurityList compartment in Core Service.

  * ``oci network security-list change-compartment --vcn-id  --compartment-id``

* Support for moving Resource Manager Stacks across compartments

  * ``oci resource-manager stack change-compartment --compartment-id, --stack-id``

* Support for Preview Database service for Autonomous Databases

  * ``oci db autonomous-database create --is-preview-version-with-service-terms-accepted [boolean]``

* Support for Preview version list API for Autonomous Databases

  * ``oci db autonomous-db-preview-version list --compartment-id [compartment ID]``

2.5.17 - 2019-07-02
-------------------
Added
~~~~~
* Support for moving instance-pools and instance-configurations across compartments

  * ``oci compute-management instance-configuration change-compartment``
  * ``oci compute-management instance-pool change-compartment``

* Support for moving autoscaling-configurations across compartments

  * ``oci autoscaling configuration change-compartment``

* Support for moving custom images across compartments

  * ``oci compute image change-compartment``

Changed
~~~~~~~
* Updated the Oracle Streaming Service' regional endpoints template for new regions.

2.5.16 - 2019-06-25
-------------------
Added
~~~~~
* Support for moving Nat Gateway across compartments

  * ``oci network nat-gateway change-compartment``

* Support for moving sender compartment in Email Service.

  * ``oci email sender change-compartment --sender-id --compartment-id``

2.5.15 - 2019-06-18
-------------------
Added
~~~~~
* Support for moving block volumes, block volume backups, boot volumes, boot volume backups, volume groups, volume group backups across compartments in the Block Storage Service

  * ``oci bv backup change-compartment``
  * ``oci bv boot-volume change-compartment``
  * ``oci bv boot-volume-backup change-compartment``
  * ``oci bv volume change-compartment``
  * ``oci bv volume-group change-compartment``
  * ``oci bv volume-group-backup change-compartment``

* Support for scheduling and cancelling deletion for KMS keys in the Key Management Service

  * ``oci kms management key schedule-deletion --time-of-deletion``
  * ``oci kms management key cancel-deletion``

* Support for python 3.7 on Windows, Linux, and MacOS

* Support for moving Service Gateway across compartments in the Networking Service

  * ``oci network service-gateway change-compartment``

2.5.14 - 2019-06-11
-------------------
Added
~~~~~
* Support for Autonomous Database (Dedicated) features as part of the Database Service

  * ``oci db autonomous-container-database``
  * ``oci db autonomous-database``
  * ``oci db maintenance-run``
  * ``oci db autonomous-exadata-infrastructure``

* Support for specifying bootVolumeSizeInGBs parameter during creation of instance config in the Compute Management service.

  * ``oci compute-management instance-configuration create --instance-details``

Changed
~~~~~~~~
* \*NIX installer, install.sh, supports more options for non-interactive installations.

  * ``./install.sh --accept-all-defaults --python-install-location <dir> --optional-features [db] --install-dir <dir> --exec-dir <dir> --update-path-and-enable-tab-completion --rc-file-path <file-path> --oci-cli-version <version> --help``

* Windows installer, install.ps1, supports more options for non-interactive installations.

  * ``.\install.ps1 -AcceptAllDefaults -PythonInstallLocation <dir> -OptionalFeatures [db] -UpdatePathAndEnableTabCompletion -OciCliVersion <version>``

* The installer no longer checks for required native dependencies on linux systems.

* The installer no longer requires /dev/tty for non-interactive installations.

2.5.13 - 2019-06-04
-------------------
Added
~~~~~
* Support for delete Tag Namespace and Tag Definition in the Identity Service

  * ``oci iam tag delete``
  * ``oci iam tag-namespace delete``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/identity/examples_and_test_scripts/tagging_example.sh>`__.

* Support for iscsi type volume-attachment for compute resources.

  * ``oci compute volume-attachment attach-iscsi-volume``

* Support for specifying the FAULT_DOMAIN parameter for instances as part of InstanceConfiguration details.

  * ``oci compute-management instance-configuration create``
  * ``oci compute-management instance-configuration launch-compute-instance``

* Support for Auto Scale in the Database service for Autonomous Databases (--is-auto-scaling-enabled for ``oci db autonomous-database``)

Changed
~~~~~~~
* New parameters to handle Tag Definition and Tag Namespace lifecycle state

  * ``oci iam tag-namespace update --wait-for-state --max-wait-seconds --wait-interval-seconds``
  * ``oci iam tag-namespace list --lifecycle-state``
  * ``oci iam tag update --wait-for-state --max-wait-seconds --wait-interval-seconds``
  * ``oci iam tag create --wait-for-state --max-wait-seconds --wait-interval-seconds``

Fixed
~~~~~
* JSON generated for ``oci compute instance launch`` using ``--generate-full-command-json-input`` option.

* ``oci os object restore-status`` now returns accurate restoration time. Earlier for restoration time greater than a day, it did not display the number of days.

* Load balancer service endpoints.

* Filters, sort options for ``oci db database list`` command.

2.5.12 - 2019-05-28
-------------------
Added
~~~~~
* Support to get user UI password creation date in Identity service.

  * ``oci iam ui-password-information get-user --user-id``

* Support for Work Requests Service

  * ``oci work-requests``
  * An example of using the Work Requests Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/work_requests/examples_and_test_scripts/get_work_requests_example.sh>`__.

* Tags returned in File Storage Summary objects

* Change compartment support for File Storage Service.

  * ``oci fs file-system change-compartment --file-system-id --compartment-id``
  * ``oci fs mount-target change-compartment --mount-target-id --compartment-id``

Fixed
~~~~~
* Missing emulated type for volume-attachment. (`Issue 146 <https://github.com/oracle/oci-cli/issues/146>`__)

  * ``oci compute volume-attachment attach --type``

* Fixed metrics example. (`Issue 149 <https://github.com/oracle/oci-cli/issues/149>`_, `Issue 150 <https://github.com/oracle/oci-cli/issues/150>`_)


2.5.11 - 2019-05-21
-------------------
Added
~~~~~
* Improvement for VPN IPSec service usability: support BGP dynamic routing and allow customer to input PSK.

  * ``oci network ip-sec-tunnel get``
  * ``oci network ip-sec-tunnel list``
  * ``oci network ip-sec-tunnel update``
  * ``oci network ip-sec-psk get``
  * ``oci network ip-sec-psk update``

* Support for getting Object Storage namespace of another tenancy by using their compartment ID.

  * ``oci os ns get --compartment-id``
  * An example on getting namespace using compartment ID can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/object_storage/examples_and_test_scripts/object_storage_get_namespace.sh>`__.

Changed
~~~~~~~
* IPSec connection create command: it now includes --tunnel-configuration option.

  * ``oci network ip-sec-connection create --tunnel-configuration``

* Listing for Instance Configs and Pools: they now return defined and freeform tags.

  * ``oci compute-management instance-configuration list --compartment-id``
  * ``oci compute-management instance-pool list --compartment-id``

* Listing for Autoscaling configurations: they now return defined and freeform tags.

  * ``oci autoscaling configuration list --compartment-id``

2.5.10 - 2019-05-14
-------------------
Added
~~~~~
* Support for changing the recovery window for backup in the Database service (``--recovery-windows-in-days``  option for ``oci db database create``)

* Support for LoggingContext option in Key Management Service (``--logging-context`` option for ``oci kms crypto encrypt|decrypt|generate-data-encryption-key``)

  * An example on using Key Management Service LoggingContext option can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/key_management/examples_and_test_scripts/kms_example.sh>`__.
  * ``oci kms crypto encrypt --logging-context``
  * ``oci kms crypto decrypt --logging-context``
  * ``oci kms crypto generate-data-encryption-key --logging-context``

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

  * ``oci network cpe create --customer-reference-name [text]``
  * ``oci network cpe update --customer-reference-name [text]``

* Improve information to IPSecConnection by introducing Customer Reference Name in the VPN Service.

  * ``oci network ipsecconnection create --customer-reference-name [text]``
  * ``oci network ipsecconnection update --customer-reference-name [text]``

* Improve information to RemorePeeringConnection by introducing Provider Service Key Name in the VPN Service.

  * ``oci network remote-peering-connection create --provider-service-key-name [text]``
  * ``oci network remote-peering-connection update --provider-service-key-name [text]``

* Support Autonomous Database to change the License Type in the Database Service.

  * ``oci db autonomous-database update --license-model [LICENSE_INCLUDED|BRING_YOUR_OWN_LICENSE]``

* Support Autonomous Database to change the whitelistips in the Database Service.

  * ``oci db autonomous-database update --whitelisted-ips '[  "1.1.1.1","2.2.2.2/24" ]'``

* Content-type auto option for object storage put and bulk-upload commands.

* Tagging support for create Dynamic Group and update Dynamic Group flow as part of the Identity Service

  * ``oci iam dynamic-group create --defined-tags --freeform-tags``
  * ``oci iam dynamic-group update --defined-tags --freeform-tags``

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

  * ``oci network cross-connect create --customer-reference-name [text]``
  * ``oci network cross-connect update --customer-reference-name [text]``
  * ``oci network cross-connect-group create --customer-reference-name [text]``
  * ``oci network cross-connect-group update --customer-reference-name [text]``

* Improvement that introduces --provider-service-key-name to VirtualCircuit in the FastConnect Service.

  * ``oci network virtual-circuit create --provider-service-key-name [text]``
  * ``oci network virtual-circuit update --provider-service-key-name [text]``

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

  * An example on writing object lifecycle policy can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/object_storage/examples_and_test_scripts/write_object_lifecycle_policy.sh>`__.


2.5.4 - 2019-03-19
------------------
Added
~~~~~
* Support for provisioning a new autonomous database or autonomous data warehouse as a clone of another in the Database service

  * ``oci db autonomous-database create-from-clone``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/database/examples_and_test_scripts/database_example.sh>`__.

* Support for specifying metadata on node pools in the Container Engine for Kubernetes service

  * ``oci ce node-pool create --node-metadata``

2.5.3 - 2019-03-12
------------------
Added
~~~~~
* Support DbSystem timezone on provisioning API.

  * ``oci db system launch --time-zone``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/database/examples_and_test_scripts/database_launch_exadata_sparse_example.sh>`__.

* DbWorkload Type Introduced for Autonomous Database Create Request.

  * ``oci db autonomous-database create --db-workload``
  * ``oci db autonomous-database list --db-workload``

* Support for enabling I/O Resource Management (IORM) feature for Exadata Database Systems

  * ``oci db system get-exadata-iorm-config``
  * ``oci db system update-exadata-iorm-config``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/database/examples_and_test_scripts/database_exadata_iorm_example.sh>`__.

* Support for Tag Default feature as a part of the Identity Service

  * ``oci iam tag-default``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/identity/examples_and_test_scripts/tagging_example.sh>`__.

* Support for email on user accounts in the Identity Service

  * ``oci iam user create --email``
  * ``oci iam user update --email``

* Support for OCI Budget Service.

  * ``oci budgets budget create``
  * ``oci budgets budget delete``
  * ``oci budgets budget get``
  * ``oci budgets budget list``
  * ``oci budgets budget update``
  * ``oci budgets alert-rule create``
  * ``oci budgets alert-rule delete``
  * ``oci budgets alert-rule get``
  * ``oci budgets alert-rule list``
  * ``oci budgets alert-rule update``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/budget/examples_and_test_scripts/budget_example.sh>`__.

2.5.2 - 2019-02-28
------------------
Added
~~~~~
* Support for OCI Monitoring Service

  * ``oci monitoring``
  * An example using monitoring alarms can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/monitoring/examples_and_test_scripts/monitoring_alarm_example.sh>`__.
  * An example using monitoring metrics can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/monitoring/examples_and_test_scripts/monitoring_metrics_example.sh>`__.

* Support for Resource Manager service

  * ``oci resource-manager``
  * An example of using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/resource_manager/examples_and_test_scripts/resource_manager_example.sh>`__

* Support for Notification service

  * ``oci ons``
  * An example of using notification subscriptions can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/ons/examples_and_test_scripts/notification_subscription_example.sh>`__
  * An example of using notification topics can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/ons/examples_and_test_scripts/notification_topic_example.sh>`__

* Support for Auto Scaling Configurations as part of Compute Autoscaling Service

  * ``oci autoscaling configuration create``
  * ``oci autoscaling configuration delete``
  * ``oci autoscaling configuration get``
  * ``oci autoscaling configuration list``
  * ``oci autoscaling configuration update``
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/autoscaling/examples_and_test_scripts/autoscaling_example.sh>`__.

* Support for Auto Scaling Policies as part of Compute Autoscaling Service

  * ``oci autoscaling policy create``
  * ``oci autoscaling policy delete``
  * ``oci autoscaling policy get``
  * ``oci autoscaling policy list``
  * ``oci autoscaling policy update``

* Support to specify fault domains in Database system launch in Database service.

  * ``oci db system launch --fault-domains``
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/database/examples_and_test_scripts/database_launch_dbsystem_example.sh>`__.

* Support for Load Balancers for Instance Pools

  * ``oci compute-management instance-pool attach-lb``
  * ``oci compute-management instance-pool detach-lb``
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/instance_pools_example.sh>`__.

* Support for change Tag Namespace Compartment as a part of the Identity Service

  * ``oci iam tag-namespace change-compartment``
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/identity/examples_and_test_scripts/tagging_example.sh>`__.

* Support for instance launch with agent configuration for enabling monitoring and retrieving agent configuration

  * ``oci compute instance launch --agent-config``
  * ``oci compute instance update --agent-config``
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/compute_agent_enable_disable_example.sh>`__

2.5.1 - 2019-02-21
------------------
Added
~~~~~
* Tagging support for Key Management (``--freeform-tags`` and ``--defined-tags`` option for ``oci kms management vault/key create/update``)

  * An example on using KMS tagging can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/key_management/examples_and_test_scripts/kms_example.sh>`__.

* Support for Oracle Streaming Service. (``oci streaming``)

  * An example on using the Streaming Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/streaming/examples_and_test_scripts/streaming_example.sh>`__.

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

    * ``oci db database get``
    * ``oci db database list``

* Support for OCI DNS Traffic Management

  * ``oci dns steering-policy``
  * ``oci dns steering-policy-attachment``

* Support for Health Check Service (``oci health-checks``)

  * Ability to create and manage http health check
  * Ability to create and manage ping health check
  * Ability to list available vantage points
  * Ability to create on demand http probe

* Support for tagging Approved Senders in the Email Service.

  * ``oci email sender create --defined-tags --freeform-tags``
  * ``oci email sender update --defined-tags --freeform-tags``

* Support for Web Application Acceleration and Security Service (``oci waas``)

  * An example on using the WAAS Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/waas/examples_and_test_scripts/waas_example.sh>`__.

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

  * An example on using the Announcements Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/announcements_service/examples_and_test_scripts/announcements_service_example.sh>`__.

2.4.42 - 2019-01-24
-------------------
Added
~~~~~
* Support for renaming the new database when restoring a database backup to an existing dbsystem (--db-name option for ``oci db database create-from-backup``)

* Support for renaming the new database when launching new dbsystem from a database backup (--db-name option for ``oci db system launch-from-backup``)

  * An example on using --db-name parameter while restoring a database from backup can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/database/examples_and_test_scripts/rename_database_during_backup_restore.sh>`__.

* Support for calling Oracle Cloud Infrastructure services in the ``ca-toronto-1`` region (``--region ca-toronto-1``)

Changed
~~~~~~~
* Upgraded third party module versions for requests, cx_Oracle, pyOpenSSL, and cryptography. This should improve support for Python 3.7.

2.4.41 - 2019-01-14
-------------------
Added
~~~~~
* Support for passing device while attaching volume to instance in Compute service

  * ``oci compute volume-attachment attach --device``

* Support for fetching devices for an instance in Compute service

  * ``oci compute device list-instance``

* Support for Custom Header Rule Sets in the Load Balancer service

  * ``oci lb rule-set``

2.4.40 - 2018-12-13
-------------------
Added
~~~~~
* Support for sparse diskgroup option with Exadata shape in the following command:

  * ``oci db system launch``

* Support for Data Guard on VM DB Shape

* Support create option with-new-db-system along with from-existing-db-system

  * ``oci db data-guard-association create with-new-db-system``

* Support for tagging Zones in the DNS service.

* Block Storage paravirtualized-encryption-in-transit feature

  * Ability to enable encryption-in-transit for paravirtualized volume attachment for both boot volumes and data volumes (``oci compute volume-attachment attach-paravirtualized-volume``)

* Support for resetting idp scim client as part of Identity Service.

  * ``oci iam scim-client-credentials reset-idp-scim-client --identity-provider-id``

* Support for updating user capabilities as part of Identity Service.

  * ``oci iam user update-user-capabilities --user-id``

* Support for listing identity provider groups as part of Identity Service.

  * ``oci iam identity-provider-group list``

Changed
~~~~~~~
* New Attribute ``is-latest-for-major-version`` is included in (``oci db version list``) response

* pyOpenSSL was upgraded to version 17.5.0 and cryptography to version 2.1.4 to address a vulnerability identified on GitHub as CVE-2018-1000808.

2.4.39 - 2018-11-29
-------------------
Added
~~~~~
* Support for fetching bucket statistics in Object Storage getBucket service.

  * ``oci os bucket get --bucket-name --namespace-name --fields``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/object_storage/examples_and_test_scripts/get_bucket_example.sh>`__

2.4.38 - 2018-11-15
-------------------
Added
~~~~~
* VCN Transit Routing (VTR) feature as part of Virtual Cloud Network

  * Ability to associate route table when creating drg-attachment (`oci network drg-attachment create --routeTableId`)
  * Ability to associate route table when creating local-peering-gateway (`oci network local-peering-gateway create --routeTableId`)
  * Ability to associate route table when updating drg-attachment (`oci network drg-attachment update --routeTableId`)
  * Ability to associate route table when updating local-peering-gateway (`oci network local-peering-gateway update --routeTableId`)
  * An example using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/vcn_transit_routing.sh>`__.

2.4.37 - 2018-11-01
-------------------
Added
~~~~~
* Support for tagging as part of FSS

  * ``oci fs file-system create --freeform-tags --defined-tags``
  * ``oci fs snapshot create --freeform-tags --defined-tags``
  * ``oci fs mount-target create --freeform-tags --defined-tags``

* Support for modifying the route table, DHCP options, or security lists associated with a subnet.

* Improvements to access control of compartments by allowing users to only show accessible compartments and list all compartments under the current tenancy.

  * ``oci iam compartment list --access-level``
  * ``oci iam compartment list --compartment-id-in-subtree``

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

  * ``oci db autonomous-data-warehouse generate-wallet``
  * ``oci db autonomous-database generate-wallet``

* Support for creating a standalone backup from an on-premises database as part of the Database service

  * Details can be found `here <https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm>`__.
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/src/oci_cli/scripts/database/dbaas.py>`__.

* Support for Cross Region Backup Copy in Block Storage.

  * ``oci bv backup copy --volume-backup-id --destination-region``

* Support for Cost Tracking Tags as part of Identity Service.

  * ``oci iam tag create --is-cost-tracking``
  * ``oci iam tag update --is-cost-tracking``
  * ``oci iam tag list-cost-tracking``

* Support for Compartment Delete, listing WorkRequests under a compartment and getting details for a work request.

  * ``oci iam compartment delete --compartment-id``
  * ``oci iam work-request list --compartment-id``
  * ``oci iam work-request get --work-request-id``

* Support for Instance Configurations as part of Compute Management service

  * ``oci compute-management instance-configuration create``
  * ``oci compute-management instance-configuration delete``
  * ``oci compute-management instance-configuration get``
  * ``oci compute-management instance-configuration list``
  * ``oci compute-management instance-configuration update``
  * ``oci compute-management instance-configuration launch-compute-instance``

* Support for Instance Pools as part of Compute Management service

  * ``oci compute-management instance-pool create``
  * ``oci compute-management instance-pool terminate``
  * ``oci compute-management instance-pool get``
  * ``oci compute-management instance-pool list``
  * ``oci compute-management instance-pool update``
  * ``oci compute-management instance-pool reset``
  * ``oci compute-management instance-pool softreset``
  * ``oci compute-management instance-pool start``
  * ``oci compute-management instance-pool stop``
  * ``oci compute-management instance-pool list-instances``

Changed
~~~~~~~~
* New Attribute ``dbVersion`` is included in the GET Response for Autonomous Transaction Processing Database and Autonomous Data Warehouse.
* New Attribute ``allConnectionStrings`` is included in the GET Response for Autonomous Transaction Processing Database and Autonomous Data Warehouse.

2.4.34 - 2018-10-04
---------------------
Added
~~~~~~~~
* Support to consume Image Catalog Listings as part of Compute Service

  * ``oci compute pic listing``
  * ``oci compute pic version``
  * ``oci compute pic agreements``
  * ``oci compute pic subscription``

* Support for Cross Region Copy in Object Storage.

  * ``oci os object copy --bucket-name --source-object-name --destination-region --destination-namespace --destination-bucket --destination-object``
  * An example on using the feature can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/object_storage/examples_and_test_scripts/copy_object_example.sh>`__

* Support for Object Lifecycle Management as part of the Object Storage service.

  * ``oci os object-lifecycle-policy put``
  * ``oci os object-lifecycle-policy get``
  * ``oci os object-lifecycle-policy delete``

* Support for network address translation gateway in Networking service

  * ``oci network nat-gateway create``
  * ``oci network nat-gateway delete``
  * ``oci network nat-gateway get``
  * ``oci network nat-gateway list``
  * ``oci network nat-gateway update``

2.4.33 - 2018-09-27
---------------------
Added
~~~~~~~~
* Support for Key Management Service (``oci kms``)

  * Examples on using the Key Management Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/key_management/examples_and_test_scripts/kms_example.sh>`__.
* Support for ``--wait-for-state`` option on multiple commands.
* Improved custom image support by introducing PARAVIRTUALIZED as a launch mode option in the Image Import command.

  * ``oci compute image import --launch-mode PARAVIRTUALIZED``
* Support for creating bucket with ``--kms-key-id``, updating ``--kms-key-id`` of a bucket.
* Support for creating data volume, boot volume, launch instance with ``--kms-key-id``, updating ``--kms-key-id`` for a data volume or boot volume.

2.4.32 - 2018-09-06
---------------------
Added
~~~~~~~~
* Support for updating user custom metadata on an instance in the Compute service after the instance has launched

  * ``oci compute instance update --instance-id --metadata --extended-metadata``

* Ability to increase size of boot and block volumes during creation (from clone or restore from backup) in the Block Storage Service.

  * ``oci bv boot-volume create --size-in-gbs``
  * ``oci bv volume create --size-in-gbs``

Changed
~~~~~~~~
* Updated the Description of Database API to include new character set.
* The default License Type for Autonomous DataWarehouse and Autonomous Transaction Processing will be Bring Your Own License.

2.4.31 - 2018-08-23
---------------------
Added
~~~~~~~~
* Support for Autonomous DataWarehouse and Autonomous Transaction Processing features as a part of the Database Service

  * ``oci db autonomous-data-warehouse``
  * ``oci db autonomous-data-warehouse-backup``
  * ``oci db autonomous-database``
  * ``oci db autonomous-database-backup``

* Ability to increase size of boot and block volumes in the Block Storage Service.

  * ``oci bv boot-volume update --size-in-gbs``
  * ``oci bv volume update --size-in-gbs``

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

  * An example on using the Resource Search Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/resource_search/examples_and_test_scripts/resource_search_example.sh>`__.

* Ability to set the scheduled backup policy on Boot Volume creation in the Block Storage Service. (``oci bv boot-volume create --backup-policy-id``)

2.4.28 - 2018-07-12
---------------------
Added
~~~~~~~~
* Human-friendly Resource, Compartment and User name fields in Events listed by Audit Service (``oci audit event list``).
* Improve access control to file systems by introducing NFS Export option in the File Storage Service.

  * ``oci fs export create --export-options``
  * ``oci fs export update --export-options``

* Support for updating a load balancer.

  * ``oci lb load-balancer update``

* Support for tagging of load balancer resource enabled in the Load Balancer service.

  * ``oci lb load-balancer create --defined-tags --freeform-tags``
  * ``oci lb load-balancer update --defined-tags --freeform-tags``

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
* Support for multiple hostnames per listener in Load Balancer Service. An example can be found on `Github <https://github.com/oracle/oci-cli/blob/master/services/load_balancer/examples_and_test_scripts/create_load_balancer.sh>`__ (``oci lb hostname`` and ``oci lb listener create --hostname-names``)
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
* An example of how to scale existing VM instances using the CLI can be found on `Github <https://github.com/oracle/oci-cli/blob/master/services/core/examples_and_test_scripts/scale_vm_example.sh>`__
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
* Support for Path Route Sets in the Load Balancer Service. An example can be found on `Github <https://github.com/oracle/oci-cli/blob/master/services/load_balancer/examples_and_test_scripts/create_load_balancer.sh>`__ (``oci lb path-route-set``)
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

  * An example on using the Domain Name System Service can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/services/dns/examples_and_test_scripts/dns_example.sh>`__.

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
  * An example of using tagging can be found at https://github.com/oracle/oci-cli/blob/master/services/identity/examples_and_test_scripts/tagging_example.sh

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

  * An example of creating a load balancer can be found a https://github.com/oracle/oci-cli/blob/master/services/load_balancer/examples_and_test_scripts/create_load_balancer.sh

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
