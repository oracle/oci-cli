==========
Change Log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`__.

3.49.4 - 2024-10-29
--------------------
Added
~~~~~
* OKE Control Plane service

  * Support for overriding an existing addon installation

    * ``oci ce cluster install-addon --is-override-existing``

* Network load balancer service

  * Support for L3IP listener feature

    * ``oci nlb listener create --l3-ip-idle-timeout --protocol l3ip``
    * ``oci nlb listener update --l3-ip-idle-timeout --protocol l3ip``

Fixed
~~~~~
* OKE Control Plane service

  * Support for new Open Id Connect Authentication and Open Id Connect Discovery feature

    * ``oci ce cluster create --oidc-ca-certificate``
    * ``oci ce cluster create --oidc-client-id``
    * ``oci ce cluster create --oidc-groups-claim``
    * ``oci ce cluster create --oidc-groups-prefix``
    * ``oci ce cluster create --oidc-issuer-url``
    * ``oci ce cluster create --oidc-required-claims``
    * ``oci ce cluster create --oidc-signing-algorithms``
    * ``oci ce cluster create --oidc-username-claim``
    * ``oci ce cluster create --oidc-username-prefix``
    * ``oci ce cluster create --open-id-connect-auth-enabled``
    * ``oci ce cluster create --open-id-connect-discovery-enabled``

3.49.3 - 2024-10-22
--------------------
Added
~~~~~
* Support for add and remove lock operations added to the following File Storage resources: [export, file-system, filesystem-snapshot, mount-target, outbound-connector, replication]

  * ``oci fs export add --export-id <id> --lock [full|delete]``
  * ``oci fs file-system add --file-system-id <id> --lock [full|delete]``
  * ``oci fs filesystem-snapshot-policy add ----filesystem-snapshot-policy-id <id> --lock [full|delete]``
  * ``oci fs filesystem-snapshot-policy add ----filesystem-snapshot-policy-id <id> --lock [full|delete]``
  * ``oci fs mount-target add --mount-target-id <id> --lock [full|delete]``
  * ``oci fs outbound-connector add --outbound-connector-id <id> --lock [full|delete]``
  * ``oci fs replication add --replication-id <id> --lock [full|delete]``
  * ``oci fs export remove --export-id <id> --lock [full|delete]``
  * ``oci fs file-system remove --file-system-id <id> --lock [full|delete]``
  * ``oci fs filesystem-snapshot-policy remove ----filesystem-snapshot-policy-id <id> --lock [full|delete]``
  * ``oci fs filesystem-snapshot-policy remove ----filesystem-snapshot-policy-id <id> --lock [full|delete]``
  * ``oci fs mount-target remove --mount-target-id <id> --lock [full|delete]``
  * ``oci fs outbound-connector remove --outbound-connector-id <id> --lock [full|delete]``
  * ``oci fs replication remove --replication-id <id> --lock [full|delete]``

* Support for new optional parameters in the Database Service

  * ``oci db autonomous-database create --encryption-key``
  * ``oci db autonomous-database update --encryption-key``

* Support for returning generated token as part of response in Identity Domains Service

  * ``oci identity-domains``

* Support for model backup retention and restore in Data Science Service

  * ``oci data-science model create --backup-setting, --retention-setting``
  * ``oci data-science model update --backup-setting, --retention-setting``
  * ``oci data-science model restore-archived-model-artifact --model-id --restore-model-for-hours-specified``

* Support of Host Capacity Planning for Host IO metrics in Ops Insights Service

  * ``oci opsi host-insights summarize-io-usage-trend --compartment-id --id --analysis-time-interval``

* Cloud Bridge Service

  * Support of creating/updating Amazon Web Services asset-sources

    * ``oci cloud-bridge discovery asset-source create --are-historical-metrics-collected --are-realtime-metrics-collected --is-cost-information-collected --aws-region``
    * ``oci cloud-bridge discovery asset-source update --is-cost-information-collected``

  * Support of creating/updating Amazon Web Services EC2 and EBS assets

    * ``oci cloud-bridge inventory asset create --aws-ec2 --aws-ec2-cost --attached-ebs-volumes-cost``
    * ``oci cloud-bridge inventory asset update --aws-ec2 --aws-ec2-cost --attached-ebs-volumes-cost``
    * ``oci cloud-bridge inventory asset create --aws-ebs``
    * ``oci cloud-bridge inventory asset update --aws-ebs``

  * Support of listing the Amazon Web Services regions which are available for Discovery and Migration

    * ``oci cloud-bridge discovery supported-cloud-regions list``

* Fleet Application Management Service

  * Support for managing onboarding

    * ``oci fleet-apps-management fleet-apps-management-admin onboarding get``
    * ``oci fleet-apps-management fleet-apps-management-admin onboarding enable-latest-policy``
    * ``oci fleet-apps-management fleet-apps-management-admin onboarding manage-settings``
    * ``oci fleet-apps-management fleet-apps-management-admin onboarding update``
    * ``oci fleet-apps-management fleet-apps-management-admin onboarding delete``

  * Support for managing a runbook

    * ``oci fleet-apps-management fleet-apps-management-runbooks runbook create``
    * ``oci fleet-apps-management fleet-apps-management-runbooks runbook publish``
    * ``oci fleet-apps-management fleet-apps-management-runbooks runbook set-default``
    * ``oci fleet-apps-management fleet-apps-management-runbooks runbook update``
    * ``oci fleet-apps-management fleet-apps-management-runbooks runbook delete``
    * ``oci fleet-apps-management fleet-apps-management-runbooks task-record create``
    * ``oci fleet-apps-management fleet-apps-management-runbooks task-record update``
    * ``oci fleet-apps-management fleet-apps-management-runbooks task-record delete``

  * Support for detailed job activity and managing a scheduled job

    * ``oci fleet-apps-management fleet-apps-management-operations resource-collection list-resources``
    * ``oci fleet-apps-management fleet-apps-management-operations step-collection list-steps``
    * ``oci fleet-apps-management fleet-apps-management-operations scheduler-job manage-job-execution``
    * ``oci fleet-apps-management fleet-apps-management-operations scheduler-job manage-job-execution-action-group-based-user-action-details``
    * ``oci fleet-apps-management fleet-apps-management-operations scheduler-job manage-job-execution-step-based-user-action-details``
    * ``oci fleet-apps-management fleet-apps-management-operations managed-entity-aggregation-collection summarize-managed-entity-counts``

  * Support for new optional parameters

    * ``oci fleet-apps-management fleet-apps-management-operations scheduler-job-collection list-scheduler-jobs --sub-state``
    * ``oci fleet-apps-management fleet-apps-management-operations scheduler-definition-collection list-scheduler-definitions --runbook-id``
    * ``oci fleet-apps-management fleet-apps-management-maintenance-window maintenance-window-collection list-maintenance-windows --time-schedule-start-greater-than-or-equal-to``
    * ``oci fleet-apps-management fleet-credential-collection list-fleet-credentials --target``

3.49.2 - 2024-10-15
--------------------
Added
~~~~~
* Container Engine For Kubernetes

  * Support for new Open Id Connect Discovery feature in the OKE Control Plane service

    * ``oci ce cluster create --open-id-connect-discovery-enabled``

  * Support for new Open Id Connect Authentication commands in the OKE Control Plane service

    * ``oci ce cluster create --oidc-ca-certificate``
    * ``oci ce cluster create --oidc-client-id``
    * ``oci ce cluster create --oidc-groups-claim``
    * ``oci ce cluster create --oidc-groups-prefix``
    * ``oci ce cluster create --oidc-issuer-url``
    * ``oci ce cluster create --oidc-required-claims``
    * ``oci ce cluster create --oidc-signing-algorithms``
    * ``oci ce cluster create --oidc-username-claim``
    * ``oci ce cluster create --oidc-username-prefix``
    * ``oci ce cluster create --open-id-connect-auth-enabled``

* DNS Service

  * Support for new DNS security extensions (DNSSEC) parameters in the DNS service.

    * ``oci dns zone create --dnssec-state``
    * ``oci dns zone update --dnssec-state``
    * ``oci dns zone list --dnssec-state``

  * Support for new DNS security extensions (DNSSEC) commands in the DNS service.

    * ``oci dns zone promote-zone-dnssec-key-version``
    * ``oci dns zone stage-zone-dnssec-key-version``

* BlockStorage service

  * Support for new xrc-kms-key-id parameter in Core Service

    * ``oci bv boot-volume create --xrc-kms-key-id``
    * ``oci bv boot-volume create-boot-volume-boot-volume-source-from-boot-volume-replica-details --xrc-kms-key-id``
    * ``oci bv volume create --xrc-kms-key-id``
    * ``oci bv volume create-volume-volume-source-from-block-volume-replica-details --xrc-kms-key-id``
    * ``oci bv volume-backup-policy-assignment create --xrc-kms-key-id``
    * ``oci bv volume-group creat --xrc-kms-key-id``

  * Support for Direct API feature in BlockStorage service

    * ``oci bv volume create-volume-source-from-volume-backup-delta``
    * ``oci bv boot-volume create-boot-volume-source-from-boot-volume-backup-delta``

* Goldengate Service

  * Add support for list deployment environments

    * ``oci goldengate deployment-environment list``

  * Support for defining environment type for deployments in GoldenGate service

    * ``oci goldengate deployment create --environment-type``
    * ``oci goldengate deployment update --environment-type``

3.49.1 - 2024-10-10
--------------------
Added
~~~~~
* Ops Insights service

  * Support for IAM credentials for ADBs

    * ``oci opsi database-insights change-autonomous-database-insight-advanced-features-credential-by-iam``
    * ``oci opsi database-insights change-macs-managed-cloud-database-insight-connection-credential-by-iam``
    * ``oci opsi database-insights enable-autonomous-database-insight-advanced-features-credential-by-iam``
    * ``oci opsi database-insights test-macs-managed-cloud-database-insight-connection-credential-by-iam``

  * Support for public facing enable/disable APIs for ADBs

    * ``oci opsi database-insights enable-autonomous-database``
    * ``oci opsi database-insights create-autonomous-database``

* Support for Maintenance Windows in Stack Monitoring Service

  * ``oci stack-monitoring maintenance-window``

Changed
~~~~~~~
* The password parameter is now optional for below command in the Fusion Application Service

  * ``oci fusion-apps fusion-environment create-fusion-environment-admin-user``

3.49.0 - 2024-10-08
--------------------
Added
~~~~~
* Support for cloud automation tooling update window preference on ExaCC and ExaCS VM Clusters in the Database Service.

  * ``oci db cloud-vm-cluster create``
  * ``oci db cloud-vm-cluster update``
  * ``oci db vm-cluster create``
  * ``oci db vm-cluster update``

* Support for proxy-protocol v2 on oci load balancers in Load Balancing Service

  * ``oci lb load-balancer create``

* Secure Desktops Service

  * Support to create desktop pools with private access to the desktops

    * ``oci desktops desktop-pool create --private-access-details``

  * Support for Shape Flexibility

    * ``oci desktops desktop-pool create --shape-config``

  * Support for using Dedicated VM Host

    * ``oci desktops desktop-pool create --use-dedicated-vm-host``

  * Support for extended control over the desktop lifecycle

     * ``oci desktops desktop-pool create --session-lifecycle-actions``

Changed
~~~~~~~
* [BREAKING] Kubernetes Engine Service

  * Command ``oci ce workload-mapping-summary list-workload-mappings`` has changed to ``oci ce workload-mapping list`` in the Kubernetes Engine Service

    * ``oci ce workload-mapping list``

  * The OKE service is renamed from "OCI Container Engine for Kubernetes" to "OCI Kubernetes Engine."

* Upgraded the cryptography version to (>=3.2.1,<46.0.0)

Fixed
~~~~~
* Github Issue #849(https://github.com/oracle/oci-cli/issues/849) for incorrect endpoint in Zero Trust Packet Routing Service is fixed now

  * ``oci zpr configuration create``
  * ``oci zpr configuration get``
  * ``oci zpr work-request get-zpr-configuration``
  * ``oci zpr work-request get-zpr-policy``
  * ``oci zpr work-request list-zpr-configuration``
  * ``oci zpr work-request list-zpr-configuration-errors``
  * ``oci zpr work-request list-zpr-configuration-logs``
  * ``oci zpr work-request list-zpr-policy``
  * ``oci zpr work-request list-zpr-policy-errors``
  * ``oci zpr work-request list-zpr-policy-logs``
  * ``oci zpr zpr-policy create``
  * ``oci zpr zpr-policy delete``
  * ``oci zpr zpr-policy get``
  * ``oci zpr zpr-policy list``
  * ``oci zpr zpr-policy update``

3.48.2 - 2024-10-01
--------------------
Added
~~~~~
* Support for Security Attribute Service

  * ``oci security-attribute security-attribute bulk-delete``
  * ``oci security-attribute security-attribute bulk-edit``
  * ``oci security-attribute security-attribute create``
  * ``oci security-attribute security-attribute delete``
  * ``oci security-attribute security-attribute get``
  * ``oci security-attribute security-attribute list``
  * ``oci security-attribute security-attribute update``
  * ``oci security-attribute security-attribute-namespace cascade-delete``
  * ``oci security-attribute security-attribute-namespace change-compartment``
  * ``oci security-attribute security-attribute-namespace create``
  * ``oci security-attribute security-attribute-namespace delete``
  * ``oci security-attribute security-attribute-namespace get``
  * ``oci security-attribute security-attribute-namespace list``
  * ``oci security-attribute security-attribute-namespace update``
  * ``oci security-attribute work-request get``
  * ``oci security-attribute work-request list``
  * ``oci security-attribute work-request list-errors``
  * ``oci security-attribute work-request list-logs``

* Support for Zero Trust Packet Routing Service

  * ``oci zpr configuration create``
  * ``oci zpr configuration get``
  * ``oci zpr work-request get-zpr-configuration``
  * ``oci zpr work-request get-zpr-policy``
  * ``oci zpr work-request list-zpr-configuration``
  * ``oci zpr work-request list-zpr-configuration-errors``
  * ``oci zpr work-request list-zpr-configuration-logs``
  * ``oci zpr work-request list-zpr-policy``
  * ``oci zpr work-request list-zpr-policy-errors``
  * ``oci zpr work-request list-zpr-policy-logs``
  * ``oci zpr zpr-policy create``
  * ``oci zpr zpr-policy delete``
  * ``oci zpr zpr-policy get``
  * ``oci zpr zpr-policy list``
  * ``oci zpr zpr-policy update``

* Support for securityAttributes feature for Network Load Balancer Service

  * ``oci nlb network-load-balancer create --security-attributes``
  * ``oci nlb network-load-balancer update --security-attributes``

* Support for OIC Gen3 Disaster Recovery for OIC Gen3 Disaster Recovery Service

  * ``oci integration integration-instance create --is-disaster-recovery-enabled``
  * ``oci integration integration-instance disaster-recovery-failover --integration-instance-id, -? | -h | --help``

* Support for Zero-Trust Packet Routing v1 securityAttributes for Core Service

  * ``oci network vcn update --security-attributes``
  * ``oci network vcn create --security-attributes``
  * ``oci network vnic update --security-attributes``

* Support for Zero-Trust Packet Routing v1 securityAttributes for Database Service

  * ``oci db autonomous-database create``
  * ``oci db autonomous-database create-adb-cross-region-data-guard-details``
  * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details``
  * ``oci db autonomous-database create-cross-tenancy-disaster-recovery-details``
  * ``oci db autonomous-database create-from-backup-id``
  * ``oci db autonomous-database create-from-backup-timestamp``
  * ``oci db autonomous-database create-from-clone``
  * ``oci db autonomous-database create-refreshable-clone``
  * ``oci db autonomous-database update``
  * ``oci db cloud-autonomous-vm-cluster create``
  * ``oci db cloud-autonomous-vm-cluster update``
  * ``oci db cloud-vm-cluster create``
  * ``oci db cloud-vm-cluster update``
  * ``oci db exadb-vm-cluster create``
  * ``oci db exadb-vm-cluster update``
  * ``oci db system launch``
  * ``oci db system launch-from-backup``
  * ``oci db system launch-from-database``
  * ``oci db system launch-from-db-system``
  * ``oci db system update``

* Support to read ssh-key from a file located on the local filesystem for database-migration create-oracle-connection command in the Database Migration Service

  * ``oci database-migration connection create-oracle-connection --sshkey-file``

3.48.1 - 2024-09-24
--------------------
Added
~~~~~
* Generative AI Agent service

  * Generative AI Agent Service Public Release in OCI CLI

    * ``oci generative-ai-agent agent change-compartment``
    * ``oci generative-ai-agent agent create``
    * ``oci generative-ai-agent agent delete``
    * ``oci generative-ai-agent agent get``
    * ``oci generative-ai-agent agent list``
    * ``oci generative-ai-agent agent update``
    * ``oci generative-ai-agent agent-endpoint change-compartment``
    * ``oci generative-ai-agent agent-endpoint create``
    * ``oci generative-ai-agent agent-endpoint delete``
    * ``oci generative-ai-agent agent-endpoint get``
    * ``oci generative-ai-agent agent-endpoint list``
    * ``oci generative-ai-agent agent-endpoint update``
    * ``oci generative-ai-agent data-ingestion-job create``
    * ``oci generative-ai-agent data-ingestion-job delete``
    * ``oci generative-ai-agent data-ingestion-job get``
    * ``oci generative-ai-agent data-ingestion-job get-data-ingestion-job-log-content``
    * ``oci generative-ai-agent data-ingestion-job list``
    * ``oci generative-ai-agent data-source create``
    * ``oci generative-ai-agent data-source create-data-source-oci-object-storage-data-source-config``
    * ``oci generative-ai-agent data-source delete``
    * ``oci generative-ai-agent data-source get``
    * ``oci generative-ai-agent data-source list``
    * ``oci generative-ai-agent data-source update``
    * ``oci generative-ai-agent data-source update-data-source-oci-object-storage-data-source-config``
    * ``oci generative-ai-agent knowledge-base change-compartment``
    * ``oci generative-ai-agent knowledge-base create``
    * ``oci generative-ai-agent knowledge-base create-knowledge-base-default-index-config``
    * ``oci generative-ai-agent knowledge-base create-knowledge-base-oci-database-config``
    * ``oci generative-ai-agent knowledge-base create-knowledge-base-oci-open-search-index-config``
    * ``oci generative-ai-agent knowledge-base delete``
    * ``oci generative-ai-agent knowledge-base get``
    * ``oci generative-ai-agent knowledge-base list``
    * ``oci generative-ai-agent knowledge-base update``
    * ``oci generative-ai-agent knowledge-base update-knowledge-base-default-index-config``
    * ``oci generative-ai-agent knowledge-base update-knowledge-base-oci-database-config``
    * ``oci generative-ai-agent knowledge-base update-knowledge-base-oci-open-search-index-config``
    * ``oci generative-ai-agent work-request cancel``
    * ``oci generative-ai-agent work-request get``
    * ``oci generative-ai-agent work-request list``
    * ``oci generative-ai-agent work-request-error list``
    * ``oci generative-ai-agent work-request-log-entry list-work-request-logs``

* Generative AI Agent Client service

  * Generative AI Agent Client Service Public Release in OCI CLI

    * ``oci generative-ai-agent-runtime session chat``
    * ``oci generative-ai-agent-runtime session create``
    * ``oci generative-ai-agent-runtime session delete``
    * ``oci generative-ai-agent-runtime session get``
    * ``oci generative-ai-agent-runtime session update``

* Monitoring service

  * Support for new optional parameters in the alarm-suppression and alarm-suppression-collection commands

    * ``oci monitoring alarm-suppression create --level --suppression-conditions``
    * ``oci monitoring alarm-suppression-collection list-alarm-suppressions --compartment-id --compartment-id-in-subtree --level --target-type --is-all-suppressions``

* Ops Insights service

  * Support for ExaCC via Management agent

    * ``oci opsi database-insights change-macs-managed-cloud-database-insight-connection-credential-by-vault``
    * ``oci opsi database-insights create-macs-managed-cloud-database-insight``
    * ``oci opsi database-insights enable-macs-managed-cloud-database-insight``
    * ``oci opsi database-insights test-macs-managed-cloud-database-insight-connection-credential-by-vault``
    * ``oci opsi database-insights update-macs-managed-cloud-database-insight``
    * ``oci opsi exadata-insights add-macs-managed-cloud-exadata-insight-members``
    * ``oci opsi exadata-insights create-macs-managed-cloud-exadata-insight``
    * ``oci opsi exadata-insights enable-macs-managed-cloud-exadata-insight``
    * ``oci opsi exadata-insights update-macs-managed-cloud-exadata-insight``
    * ``oci opsi host-insights update-macs-managed-database-host-insight``

* Fusion service

  * Support for optional parameter --is-data-masking-opted in create-refresh-activity

    * ``oci fusion-apps create-refresh-activity-details create-refresh-activity --is-data-masking-opted``

* Integration service

  * Support for OIC Gen3 configure custom endpoint

    * ``oci integration integration-instance --add-oracle-managed-custom-endpoint``
    * ``oci integration integration-instance remove``

* Database service

  * Support for assigning key versions for the database and pluggable database

    * ``oci db database set-oci-db-key-version --database-id --kms-key-version-id``
    * ``oci db pluggable-database set-oci-pdb-key-version --pluggable-database-id --kms-key-version-id``

  * Support for listing autonomous database with lifecyclestate

    * ``oci db autonomous-database list --lifecycle-state-not-equal-to``

  * Support for undelete autonomous database

    * ``oci db autonomous-database create-autonomous-database-undelete-autonomous-database-details``

* Analytics service

  * Support for opting for different update channel schedules, "regular" or "early"

    * ``oci analytics analytics-instance create --update-channel regular``
    * ``oci analytics analytics-instance update --update-channel early``

* Data Safe service

  * Support for appending and deleting allowed SQLs from SQL Firewall policy

    * ``oci data-safe sql-firewall-allowed-sql get--sql-firewall-allowed-sql-id``
    * ``oci data-safe sql-firewall-allowed-sql delete --sql-firewall-allowed-sql-id``
    * ``oci data-safe sql-firewall-allowed-sql bulk-create-sql-firewall-allowed-sqls-list-selection-mode--log-type``
    * ``oci data-safe sql-firewall-allowed-sql bulk-create --log-type --selection —sql-firewall-policy-id``
    * ``oci data-safe sql-firewall-allowed-sql bulk-create-sql-firewall-allowed-sqls-list-selection-mode --log-type, --selection-items, --sql-firewall-policy-id``
    * ``oci data-safe sql-firewall-allowed-sql bulk-create-sql-firewall-allowed-sqls-scim-query-selection-mode --log-type, --selection-scim-query, --sql-firewall-policy-id``

3.48.0 - 2024-09-17
--------------------
Added
~~~~~
* Support Dedicated AI Cluster Unit Shape LARGE_GENERIC_4 in the Generative AI Service Management

  * ``oci generative-ai dedicated-ai-cluster``

* Support for allowing the operator to provide a ticket number when creating access request in the Lockbox service

  * ``oci oma access-request create --ticket-number``

* Support for release 3.1 of Capacity Management Service

  * ``oci capacity-management occ-handover-resource-block-collection``
  * ``oci capacity-management occ-customer``
  * ``oci capacity-management occ-customer-group``

* Support for Text to Speech in Speech service

  * ``oci speech synthesize-speech``
  * ``oci speech voice list``

* Fleet Software Update service

  * Support to create DB and GI Collections major version 23.

    * ``oci fleet-software-update fsu-collection create-db --source-major-version DB_23``
    * ``oci fleet-software-update fsu-collection create-gi --source-major-version GI_23``

  * Support to create DB and GI Collections major version 23.

    * ``oci fleet-software-update fsu-cycle create-patch --goal-version-details { "version" : "23.4.0.0" }``

Changed
~~~~~~~
* Capacity Management Service

  * [BREAKING] Optional parameter ``--occ-customer-group-id`` has now been made required in the following commands

    * ``oci capacity-management occ-overview-collection list-internal-namespace-occ-overviews``
    * ``oci capacity-management occ-availability-catalog-collection list-internal``

3.47.0 - 2024-08-27
--------------------

Changed
~~~~~~~
* [BREAKING] Document Understanding Service

  * Support for the accepted value INSURANCE_CLAIM is removed and HEALTH_INSURANCE_ID is added in the documentType parameter

     * ``oci ai-document analyze-document-result analyze-document --document-type health_insurance_id``

   * The field tenancyId of a complex type parameter is removed in the following commands

     * ``oci ai-document analyze-document-result analyze-document``
     * ``oci ai-document analyze-document-result analyze-document-inline-document-details``
     * ``oci ai-document analyze-document-result analyze-document-object-storage-document-details``
     * ``oci ai-document processor-job create``
     * ``oci ai-document processor-job create-processor-job-general-processor-config``
     * ``oci ai-document processor-job create-processor-job-inline-document-content``
     * ``oci ai-document processor-job create-processor-job-object-storage-locations``
  
* Vault Key Management Service

  * Support for Cross-Region Replication for Virtual Vaults in Key Management Service
 
    * ``oci kms management vault get`` 

* Oracle Database Autonomous Recovery Service

  * Support for new optional parameter in ZRCV cloud service

    * ``oci recovery protected-database create --subscription-id``
    * ``oci recovery protection-policy create --must-enforce-cloud-locality``

* Oracle Cloud Vmware Solution Service

  * Support for VMware Major and Minor Version Upgrade in Oracle Cloud VMware Solution

    * ``oci ocvs sddc vmware-versions --version-to-upgrade ``

* Database Service

  * Support for provisioning Developer Autonomous Database.

    * ``oci db autonomous-database create --is-dev-tier <boolean>``

  * Support for specifying and upgrading a Developer Autonomous Database to Paid Autonomous Database

    * ``oci db autonomous-database update --is-dev-tier <boolean>``

* Load Balancing Service
  
  * Support for new optional parameter enabling inclusion of the Request Id of a request to the load balancer in a header attached to the request forwarded by the load balancer to one of its servers and in the response from the load balancer.

    * ``oci lb load-balancer create --is-request-id-enabled``
    * ``oci lb load-balancer update --is-request-id-enabled``

  * Support for new optional parameter specifying the name of the header used to contain the Request Id.

    * ``oci lb load-balancer create --request-id-header``
    * ``oci lb load-balancer update --request-id-header``

Added
~~~~~~~

* Delegate Access Control Service

  * Support for the Delegate Access Control service

    * ``oci delegate-access-control delegated-resource-access-request``
    * ``oci delegate-access-control delegation-control``
    * ``oci delegate-access-control delegation-subscription``
    * ``oci delegate-access-control service-provider``
    * ``oci delegate-access-control service-provider-action``
    * ``oci delegate-access-control work-request``

* Object Storage Service

  * Support for Object Storage Private Endpoints

    * ``oci os private-endpoint`` 

* Database Management Service

  * Support for SQL Watch

    * ``oci database-management managed-database enable-external-container-database-management-feature``
    * ``oci database-management managed-database enable-external-pluggable-database-management-feature``
    * ``oci database-management managed-database enable-external-non-container-database-management-feature``
    * ``oci database-management managed-database modify-database-management-feature``
    * ``oci database-management managed-database modify-pluggable-database-management-feature``

  * Support for advanced Database Management features for ADB

    * ``oci database-management managed-database enable-autonomous-database-management-feature-autonomous-database-diagnostics-and-management-feature-details``

* MySQL Database Service

  * Support for Customer Email Notification in HeatWave Service

    * ``oci mysql db-system clone --customer-contacts``
    * ``oci mysql db-system create --customer-contacts``
    * ``oci mysql db-system import --customer-contacts``
    * ``oci mysql db-system update --customer-contacts``

* File Storage Service

  * Support for upgrade and downgrade shapes of High Performance Mount Targets

    * ``oci fs mount-target upgrade-shape``
    * ``oci fs mount-target schedule-downgrade-shape``
    * ``oci fs mount-target cancel-downgrade-shape``

* Database Service

  * Support to change compartment of scheduling policy

    * ``oci db scheduling-policy change-compartment --compartment-id | -c, --scheduling-policy-id, -? | -h | --help``

  * Support to create a new scheduling policy

    * ``oci db scheduling-policy create --cadence, --compartment-id | -c, --display-name, --cadence-start-month, --defined-tags, --freeform-tags, -? | -h | --help ``

  * Support to delete a scheduling policy

    * ``oci db scheduling-policy delete --scheduling-policy-id, --force, -? | -h | --help``

  * Support to get a scheduling policy

    * ``oci db scheduling-policy get --scheduling-policy-id, -? | -h | --help``

  * Support to list scheduling policy

    * ``oci db scheduling-policy list --compartment-id | -c, --all, --display-name, -? | -h | --help``

  * Support to update a scheduling policy

    * ``oci db scheduling-policy update --scheduling-policy-id, --cadence, --cadence-start-month, --display-name, --defined-tags, --force, --freeform-tags, -? | -h | --help``

  * Support to create a scheduling window based on scheduling policy

    * ``oci db scheduling-window create --scheduling-policy-id, --window-preference, --compartment-id | -c, --defined-tags, --freeform-tags, -? | -h | --help``

  * Support to delete a scheduling window

    * ``oci db scheduling-window delete --scheduling-policy-id, --scheduling-window-id, --force, -? | -h | --help``

  * Support to get a scheduling window

    * ``oci db scheduling-window get --scheduling-policy-id, --scheduling-window-id, -? | -h | --help``

  * Support to list scheduling window

    * ``oci db scheduling-window list --scheduling-policy-id, --all, --compartment-id | -c, --display-name, -? | -h | --help``

  * Support to update a scheduling window

    * ``oci db scheduling-window update --scheduling-policy-id, --scheduling-window-id, --defined-tags, --force, --freeform-tags, -? | -h | --help, --window-preference``

  * Support for the Domain parameter in BaseDB Create DataGuard CLI 

    * ``oci db data-guard-association create with-new-db-system``

  * Support for scheduling plan, scheduled action, execution window and execution action as part of granular maintenance scheduling support for Exadata Infrastructure Components

    * ``oci db action-param-values-summary list-params-for-action-type``
    * ``oci db execution-action create``
    * ``oci db execution-action delete``
    * ``oci db execution-action get``
    * ``oci db execution-action list``
    * ``oci db execution-action move-execution-action-member``
    * ``oci db execution-action update``
    * ``oci db execution-window create``
    * ``oci db execution-window delete``
    * ``oci db execution-window get``
    * ``oci db execution-window list``
    * ``oci db execution-window reorder-execution-actions``
    * ``oci db execution-window update``
    * ``oci db execution-window cancel``
    * ``oci db maintenance-run cancel``
    * ``oci db recommended-scheduled-action-summary list-recommended-scheduled-actions``
    * ``oci db scheduled-action create``
    * ``oci db scheduled-action delete``
    * ``oci db scheduled-action get``
    * ``oci db scheduled-action list``
    * ``oci db scheduled-action update``
    * ``oci db scheduled-action update``
    * ``oci db scheduling-plan change-compartment``
    * ``oci db scheduling-plan create``
    * ``oci db scheduling-plan delete``
    * ``oci db scheduling-plan cascading-delete``
    * ``oci db scheduling-plan get``
    * ``oci db scheduling-plan list``
    * ``oci db scheduling-plan reorder-scheduled-actions``

* Oracle Database Autonomous Recovery Service

  * Support for changing Protected Database Subscription in ZRCV cloud service

    * ``oci recovery protected-database change-protected-database-subscription --protected-database-id, -? | -h | --help, --is-default, --subscription-id``

* Web Application Firewall service

  * Support for the DYNAMIC body variant in a RETURN_HTTP_RESPONSE action.

    * ``oci waf web-app-firewall-policy create --actions [complex type]``
    * ``oci waf web-app-firewall-policy update --actions [complex type]``

* Announcements Service

  * Support for listing all active service summary in OCI

    * ``oci announce service list --compartment-id <root_compartment_id>``

3.46.0 - 2024-08-20
--------------------
Removed
~~~~~
* [BREAKING] Disaster Recovery service

  * Removed optional parameter --dr-plan-execution-type from list command

    * ``oci disaster-recovery dr-plan-execution list``

Added
~~~~~
* Database Service

  * Support for creating Maintenance Run Using Autonomous Database Software Image in the Database service

    * ``oci db maintenance-run create --database-software-image-id``

* Fleet Application Management Service

  * Support for the Fleet Application Management service

    * ``oci fleet-apps-management``

* Redis Service

  * Support for list cluster nodes command in the OCI Cache service

    * ``oci redis node-summary list-redis-cluster-nodes``

  * Support new parameters cluster-mode and shard-count for sharding

    * ``oci redis redis-cluster create --cluster-mode, --shard-count``
    * ``oci redis redis-cluster update --shard-count``

* Integration Service

  * Support for Extend Data Retention Period for OIC Instance

    * ``oci integration integration-instance extend-data-retention --data-retention-period, --integration-instance-id``

* Analytics Service

  * Support for Identity Domains

    * ``oci analytics analytics-instance create --domain-id ocid --admin-user user``

  * Support for feature set in analytics-instance

    * ``oci analytics analytics-instance create --feature-bundle feature_set``

* Database Management Service

  * Support for SQL Watch and DB Lifecycle Management

    * ``oci database-management managed-database enable-external-container-database-management-feature``
    * ``oci database-management managed-database enable-external-pluggable-database-management-feature``
    * ``oci database-management managed-database enable-external-non-container-database-management-feature``
    * ``oci database-management managed-database modify-database-management-feature``
    * ``oci database-management managed-database modify-pluggable-database-management-feature``

* Mysql Database Service

  * Support for automatically increasing storage in the MySQL Database service

    * ``oci mysql db-system clone --is-auto-expand-storage-enabled --max-storage-size-in-gbs``
    * ``oci mysql db-system create --is-auto-expand-storage-enabled --max-storage-size-in-gbs``
    * ``oci mysql db-system import --is-auto-expand-storage-enabled --max-storage-size-in-gbs``
    * ``oci mysql db-system update --is-auto-expand-storage-enabled --max-storage-size-in-gbs``

3.45.2 - 2024-08-13
--------------------
Added
~~~~~
* Support for idle timeout feature for Network Load Balancer Service

  * ``oci nlb listener create --tcp-idle-timeout, --udp-idle-timeout``
  * ``oci nlb listener update --tcp-idle-timeout, --udp-idle-timeout``

* Support for viewing subscription level limits in Limits Service

  * ``oci limits definition list --subscription-id``
  * ``oci limits resource-availability get --subscription-id``
  * ``oci limits service list --subscription-id``
  * ``oci limits value list --subscription-id``

* Support for OIC Instance Creation for Healthcare Feature in Oracle Integration Service

  * ``oci integration integration-instance create --integration-instance-type healthcare``

3.45.1 - 2024-08-06
--------------------
Added
~~~~~
* Java Management Service Fleets

  * Support for new commands

    * ``oci jms agent-installer-summary``
    * ``oci jms fleet request-deployed-application-migration-analyses``
    * ``oci jms jms-plugin``

  * Add new options to existing commands

    * ``oci jms crypto-analysis-result list --finding-count, --finding-count-greater-than, --host-name, --non-compliant-finding-count, --non-compliant-finding-count-greater-than``
    * ``oci jms fleet-agent-configuration update --is-collecting-managed-instance-metrics-enabled, --is-collecting-usernames-enabled``
    * ``oci jms java-migration-analysis-result list --application-name, --host-name``
    * ``oci jms library-usage summarize --cvss-score-greater-than, --cvss-score-less-than``
    * ``oci jms performance-tuning-analysis-result list --host-name``
    * ``oci jms work-request list --operation-type, --status``

* Support for a new optional parameter "compartmentId" in  Java Management Service Downloads

  * ``oci jms-java-downloads download-url generate-artifact --compartment-id``

* Big Data Service

  * Support for new commands

    * ``oci bds instance create-resource-principal-configuration``
    * ``oci bds instance force-refresh-resource-principal``
    * ``oci bds instance get-resource-principal-configuration``
    * ``oci bds instance list-resource-principal-configurations``
    * ``oci bds instance update-resource-principal-configuration``
    * ``oci bds resource-principal-configuration remove``
    * ``oci bds instance install-patch-downtime-based-odh-patching-config``

* Support for new optional parameters in the OS Management Hub service

  * ``oci os-management-hub software-source create-custom-swsrc --is-latest-content-only``
  * ``oci os-management-hub software-source create-versioned-custom-swsrc --is-latest-content-only``
  * ``oci os-management-hub software-source update-custom-swsrc --is-latest-content-only``

* Devops Service

  * Support for pull requests and merge in Source Control Management Service

    * ``oci devops pull-request-comment``
    * ``oci devops pull-request``
    * ``oci devops protected-branch``
    * ``oci devops project get-notification-preference``
    * ``oci devops project get-project-settings``
    * ``oci devops project update-project-settings``
    * ``oci devops project update-notification-preference``
    * ``oci devops project delete-project-settings``
    * ``oci devops project list-project-analytics-authors``
    * ``oci devops project summarize-project-analytics``
    * ``oci devops repository get-repository-notification-preference``
    * ``oci devops repository get-repository-settings``
    * ``oci devops repository update-repository-settings``
    * ``oci devops repository update-repository-notification-preference``
    * ``oci devops repository delete-repository-settings``
    * ``oci devops repository create-or-update-git-tag-details``
    * ``oci devops repository create-or-update-git-branch-details``
    * ``oci devops repository delete-git-ref``
    * ``oci devops repository list-pull-request-authors``
    * ``oci devops repository list-repository-analytics-authors``
    * ``oci devops repository summarize-repository-analytics``
    * ``oci devops repository sync``
    * ``oci devops repository list-fork-sync-statuses``
    * ``oci devops deployment service``

  * Support for new optional parameter/flag

    * ``oci devops repository create --parent-repository-id``
    * ``oci devops repository get-commit-diff --target-repository-id`
    * ``oci devops repository list-commit-diffs --target-repository-id``

* Support for new optional parameter --file-system-configuration-details in vm cluster in db service

  * ``oci db vm-cluster create --file-system-configuration-details``
  * ``oci db vm-cluster update --file-system-configuration-details``

3.45.0 - 2024-07-30
--------------------
Added
~~~~~
* Identity Domains Service

  * Support for new commands

    * ``oci identity-domains social-identity-provider create``
    * ``oci identity-domains social-identity-provider delete``
    * ``oci identity-domains social-identity-provider get``
    * ``oci identity-domains social-identity-provider patch``
    * ``oci identity-domains social-identity-provider put``
    * ``oci identity-domains social-identity-providers list``
    * ``oci identity-domains social-identity-providers search``

* Stack Monitoring

  * Support for baselineable metric for imported resources and metric extension

    * ``oci stack-monitoring baselineable-metric update``
    * ``oci stack-monitoring baselineable-metric list``
    * ``oci stack-monitoring baselineable-metric create``

* Database Migration

  * Support GoldenGate Suspend Phase / Parameter File Update

    * ``oci database-migration job create-parameter-file-version``
    * ``oci database-migration job delete-parameter-file-version``
    * ``oci database-migration job get-parameter-file-version``
    * ``oci database-migration job list-parameter-file-versions``
    * ``oci database-migration job make-current-parameter-file-version``
    * ``oci database-migration job suspend``

* Exadata Fleet Update Service

  * Support for Diagnostics collection preferences and VMCluster and CloudVMCluster custom GI images

    * ``oci fleet-software-update fsu-cycle create --diagnostics-collection``

* Speech Service

  * Support for Realtime Speech in the Speech Service

    * ``oci speech realtime-session-token create``

  * Support for Customization in the Speech Service

    * ``oci speech customization``

* Core Service

  * Support for obtaining compute instance maintenance events in Core services

    * ``oci compute instance-maintenance-event get``
    * ``oci compute instance-maintenance-event list``
    * ``oci compute instance-maintenance-event update``

* Data Safe Service

  * Support for creating custom alert policies

    * ``oci data-safe alert-policy change-compartment``
    * ``oci data-safe alert-policy create``
    * ``oci data-safe alert-policy delete``
    * ``oci data-safe alert-policy update``
    * ``oci data-safe alert-policy-rule create``
    * ``oci data-safe alert-policy-rule delete``
    * ``oci data-safe alert-policy-rule get``
    * ``oci data-safe alert-policy-rule update``

Changed
~~~~~~~
* [BREAKING] Network Firewall Service

  * The following commands from network-firewall service have been deprecated and unavailable to use

    * ``oci network-firewall application create-application-create-icmp-application-details``
    * ``oci network-firewall application create-application-create-icmp6-application-details``
    * ``oci network-firewall application create-service-create-udp-service-details``
    * ``oci network-firewall application create-service-create-tcp-service-details``
    * ``oci network-firewall mapped-secret create-mapped-secret-create-vault-mapped-secret-details``
    * ``oci network-firewall decryption-profile create-decryption-profile-create-ssl-inbound-inspection-profile-details``
    * ``oci network-firewall decryption-profile create-decryption-profile-create-ssl-forward-proxy-profile-details``
    * ``oci network-firewall application update-application-update-icmp-application-details``
    * ``oci network-firewall application update-application-update-icmp6-application-details``
    * ``oci network-firewall application update-service-update-udp-service-details``
    * ``oci network-firewall application update-service-update-tcp-service-details``
    * ``oci network-firewall mapped-secret update-mapped-secret-update-vault-mapped-secret-details``
    * ``oci network-firewall decryption-profile update-decryption-profile-update-ssl-inbound-inspection-profile-details``
    * ``oci network-firewall decryption-profile update-decryption-profile-update-ssl-forward-proxy-profile-details``

* Data Safe Service

  * Added additional attributes for existing APIs

    * ``oci data-safe masking-policy``
    * ``oci data-safe work-request list``
    * ``oci data-safe target-alert-policy-association-summary list-target-alert-policy-associations``

3.44.4 - 2024-07-23
--------------------
Added
~~~~~
* Database Service

  * Support for new optional parameters in the database APIs

    * ``oci db autonomous-database create --byol-compute-count-limit``
    * ``oci db autonomous-database update --byol-compute-count-limit``

  * Support for the subscription ID attribute in Cloud Exadata Infrastructure and Cloud VM Cluster in Database service

    * ``oci db cloud-exa-infra create --subscription-id``
    * ``oci db cloud-vm-cluster create --subscription-id``
    * ``oci db cloud-exa-infra change-cloud-exadata-infrastructure-subscription --cloud-exadata-infrastructure-id --is-default --subscription-id``
    * ``oci db cloud-vm-cluster change-cloud-vm-cluster-subscription --cloud-vm-cluster-id --is-default --subscription-id``

  * Support for ``subscriptionId`` in

    * ``oci db autonomous-database create --subscription-id``

  * Update action API

    * ``oci db autonomous-database change-autonomous-database-subscription --autonomous-database-id``

* Application Performance Monitoring Synthetic Service

  * Support for the sql monitor creation and updation

    * ``oci apm-synthetics monitor create-sql-monitor``
    * ``oci apm-synthetics monitor update-sql-monitor``

  * Support for the ftp monitor creation and updation

    * ``oci apm-synthetics monitor create-ftp-monitor``
    * ``oci apm-synthetics monitor update-ftp-monitor``

* Data Safe Service

  * Support for listing discovered sensitive types and discovered sensitive schemas in sensitive data model

    * ``oci data-safe sensitive-data-model-sensitive-type-collection list-sensitive-data-model-sensitive-types --sensitive-data-model-id``

  * Support for creating and updating sensitive data model with only table level scope

    * ``oci data-safe sensitive-data-model create --tables-for-discovery``
    * ``oci data-safe sensitive-data-model update --tables-for-discovery``

  * Support for creating discovery job with table level scope

    * ``oci data-safe discovery-job create --tables-for-discovery``

  * Support for filtering reports with the time of generation

    * ``oci data-safe report-summary list-reports --time-generated-greater-than-or-equal-to, --time-generated-less-than``

  * Support for creating and updating schedule for user assessment and security assessment

    * ``oci data-safe security-assessment create --is-assessment-scheduled``
    * ``oci data-safe security-assessment update --is-assessment-scheduled``
    * ``oci data-safe user-assessment create --is-assessment-scheduled``
    * ``oci data-safe user-assessment update --is-assessment-scheduled``

  * Support for listing findings in security assessment

    * ``oci data-safe security-assessment list-findings --target-id``

  * Support for unsetting security and user assessment baseline with target ids

    * ``oci data-safe security-assessment unset-security-assessment-baseline --target-ids``
    * ``oci data-safe user-assessment unset-user-assessment-baseline --target-ids``

* Support for MySQL Heatwave database systems within the Ops Insights service.

  * ``oci opsi database-insights create-mds-my-sql-database``
  * ``oci opsi database-insights enable-mds-my-sql-database``
  * ``oci opsi database-insights update-mds-my-sql-database``

3.44.3 - 2024-07-16
-------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the me-abudhabi-2 region

3.44.2 - 2024-07-09
-------------------
Added
~~~~~
* Database Service

  * Support for create new DB with OKV

    * ``oci db database create --key-store-id``

  * Support for confirm key store details are correct

    * ``oci db key-store confirm-key-store-details-are-correct --key-store-id``

3.44.1 - 2024-07-02
-------------------
Added
~~~~~
* OCI Operations Insights Service

  * Support in OPSI Host Capacity Planning to analyze disabled/deleted resources

    * ``oci opsi host-insights list-host-configurations --status``
    * ``oci opsi host-insights list-hosted-entities --status``
    * ``oci opsi host-insights summarize-host-insight-disk-statistics --status``
    * ``oci opsi host-insights summarize-host-insight-network-usage-trend --status``
    * ``oci opsi host-insights summarize-host-insight-resource-capacity-trend --status``
    * ``oci opsi host-insights summarize-host-insight-resource-forecast-trend --status``
    * ``oci opsi host-insights summarize-host-insight-resource-statistics --status``
    * ``oci opsi host-insights summarize-host-insight-resource-usage --status``
    * ``oci opsi host-insights summarize-host-insight-resource-usage-trend --status``
    * ``oci opsi host-insights summarize-host-insight-resource-utilization-insight --status``
    * ``oci opsi host-insights summarize-host-insight-storage-usage-trend --status``
    * ``oci opsi host-insights summarize-host-insight-top-processes-usage --status``
    * ``oci opsi host-insights summarize-host-insight-top-processes-usage-trend --status``

* OCI File Storage Service

  * Support for deleting file system by first detaching child file system

    * ``oci fs file-system delete --can-detach-child-file-system``

  * Support for determining whether the file system is attached to its parent file system

    * ``oci fs file-system create --clone-attach-status``

  * Support for detaching a file sys from parent file system

    * ``oci fs file-system detach --file-system-id``

* OCI Database Migration Service

  * Support for dynamic list of ZDM parameters for Oracle<>Oracle migrations

    * ``oci database-migration migration-parameter-summary list-migration-parameters``

* OCI Exadata Database Service

  * Support for managing Exascale Database Storage Vault resources

    * ``oci db exascale-db-storage-vault``

  * Support for managing VM Cluster resources on Exascale Infrastructure

    * ``oci db exadb-vm-cluster``

  * Support for getting available updates and updating histories for a Exadb VM cluster

    * ``oci db exadb-vm-cluster get-update``
    * ``oci db exadb-vm-cluster list-updates``
    * ``oci db exadb-vm-cluster get-update-history``
    * ``oci db exadb-vm-cluster list-update-histories``

  * Support for getting a list of supported minor GI versions for VM Cluster

    * ``oci db gi-minor-version-summary list-gi-version-minor-versions``

  * Support for getting a list of supported GI versions for VM Cluster

    * ``oci db gi-version list``

  * Support for getting a list of backups based on shape-family

    * ``oci db backup list``

  * Support for new optional parameter is-thin-clone for Pluggable Database resource

    * ``oci db pluggable-database create-local-clone``
    * ``oci db pluggable-database create-remote-clone``


3.44.0 - 2024-06-25
--------------------
Changed
~~~~~~~
* [BREAKING] OCI Database Migration Service

  * Deprecation of Agent resource for `database-migration`. Following commands have changed:

    * ``oci database-migration agent``
    * ``oci database-migration agent-image-summary``
    * ``oci database-migration agent-summary``
    * ``oci database-migration migration create-migration-aws-s3-data-transfer-medium-details``
    * ``oci database-migration migration create-migration-db-link-data-transfer-medium-details``
    * ``oci database-migration migration create-migration-nfs-data-transfer-medium-details``
    * ``oci database-migration migration create-migration-object-storage-data-transfer-medium-details``
    * ``oci database-migration migration update-migration-aws-s3-data-transfer-medium-details``
    * ``oci database-migration migration update-migration-db-link-data-transfer-medium-details``
    * ``oci database-migration migration update-migration-nfs-data-transfer-medium-details``
    * ``oci database-migration migration update-migration-object-storage-data-transfer-medium-details``
    * ``oci database-migration connection create``
    * ``oci database-migration connection update``
    * ``oci database-migration migration add``
    * ``oci database-migration migration clone``
    * ``oci database-migration migration create``
    * ``oci database-migration migration remove``
    * ``oci database-migration migration update``
    * ``oci database-migration migration-object-type-summary list``

Added
~~~~~
* OCI Database Migration Service

  * Support for MySQL to MySQL homogeneous migration

    * ``oci database-migration connection create-mysql-connection``
    * ``oci database-migration connection create-oracle-connection``
    * ``oci database-migration connection update-mysql-connection``
    * ``oci database-migration connection update-oracle-connection``
    * ``oci database-migration migration add-mysql-objects``
    * ``oci database-migration migration add-oracle-objects``
    * ``oci database-migration migration clone-mysql-migration``
    * ``oci database-migration migration clone-oracle-migration``
    * ``oci database-migration migration create-mysql-migration``
    * ``oci database-migration migration create-oracle-migration``
    * ``oci database-migration migration remove-mysql-objects``
    * ``oci database-migration migration remove-oracle-objects``
    * ``oci database-migration migration update-mysql-migration``
    * ``oci database-migration migration update-oracle-migration``

* Support for manual cross-region backup copy in the HeatWave MySQL Service

  * ``oci mysql backup copy``

3.43.2 - 2024-06-18
--------------------
Added
~~~~~
* OCI AI Document Service

  * Support for new document type ``INSURANCE_CLAIM`` as shown:

    * ``oci ai-document analyze-document-result analyze-document --document-type INSURANCE_CLAIM``
    * ``oci ai-document analyze-document-result analyze-document-inline-document-details --document-type INSURANCE_CLAIM``
    * ``oci ai-document analyze-document-result analyze-document-object-storage-document-details --document-type INSURANCE_CLAIM``
    * ``oci ai-document processor-job create-processor-job-general-processor-config --processor-config-document-type INSURANCE_CLAIM``

* OCI Database Service

  * Support for adding whitelisted ips for private endpoint enabled databases.

    * ``oci db autonomous-database create --whitelisted-ips``
    * ``oci db autonomous-database update --whitelisted-ips``

* OCI Stack Monitoring Service

  * Support for Microsoft IIS resource type when declaring discovery details.

    * ``oci stack-monitoring discovery-job create --discovery-details``

* Security Enhancement: Improved security for API key management.

3.43.1 - 2024-06-11
--------------------
Added
~~~~~
* Globally Distributed Database Service

  * Support for new command

    * ``oci gdd private-endpoint reinstate-proxy-instance``

  * Support for new optional parameter

    * ``oci gdd private-endpoint get --if-none-match``
    * ``oci gdd sharded-database create-sharded-database-create-dedicated-sharded-database --replication-factor, --replication-method, --replication-unit``
    * ``oci gdd sharded-database generate-gsm-certificate-signing-request --ca-bundle-id``
    * ``oci gdd sharded-database get --if-none-match``

* Fusion Applications Environment Management Service

  * Support for data dump initiation and extract in the Fusion Application Service

    * ``oci fusion-apps fusion-environment initiate-extract``
    * ``oci fusion-apps fusion-environment generate-extract-details``

* Support for new Action end point in the Application Performance Monitoring Configuration Service

  * ``oci apm-config test span-enrichment-group``

* Support for new optional parameters in the Create/Update Alarms API in OCI Monitoring Service.

  * ``oci monitoring alarm create --alarm-summary, --evaluation-slack-duration, --notification-title``
  * ``oci monitoring alarm update --alarm-summary, --evaluation-slack-duration, --notification-title``

* Support for addition of create date timestamp in Oracle Queue Service

  * ``oci queue messages get-messages``

3.43.0 - 2024-06-04
--------------------
Changed
~~~~~~~
* Generative AI Service Inference

  * [BREAKING] Optional parameter ``--chat-request`` has now been made required in the following commands

    * ``oci generative-ai-inference chat-result chat``
    * ``oci generative-ai-inference chat-result chat-dedicated-serving-mode``
    * ``oci generative-ai-inference chat-result chat-on-demand-serving-mode``

  * Complex parameters --chat-request, --chat-request-chat-history has been updated in the following command

    * ``oci generative-ai-inference chat-result chat-cohere-chat-request``

* Generative AI Service Management

  * Added support of dedicated AI cluster unit shape SMALL_COHERE_V2, LARGE_COHERE_V2, LARGE_COHERE_V2_2 and LARGE_GENERIC in the following command
 
     * ``oci generative-ai dedicated-ai-cluster create`` 

Added
~~~~~
* Database Service

  * Support for creating cross tenancy autonomous data guard

    ``oci db autonomous-database create-cross-tenancy-disaster-recovery-details``

  * Support for listing autonomous database peers

    ``oci db autonomous-database list-autonomous-database-peers``

* GoldenGate Service

  * Support for add/remove lock for resources

    ``oci goldengate connection add-lock``
    ``oci goldengate connection remove-lock``
    ``oci goldengate deployment add-lock``
    ``oci goldengate deployment remove-lock``
    ``oci goldengate deployment-backup add-lock``
    ``oci goldengate deployment-backup remove-lock``

  * Support for creating/updating new connection types

    ``oci goldengate connection create-db2-connection``
    ``oci goldengate connection update-db2-connection``
    ``oci goldengate deployment generate-log-reader-component-library-url``

3.42.0 - 2024-05-28
--------------------
Changed
~~~~~
* [BREAKING] Capacity Management Service

  * Optional parameter --resource-type accepts only 2 values CAPACITY_CONSTRAINT, SERVER_HW
  * Optional parameter --workload-type accepts only 3 values GENERIC, ROW, US_PROD

    * ``oci capacity-management occ-availability-collection list``
    * ``oci capacity-management occ-availability-catalog-collection list-internal``

Added
~~~~~~~
* Control Center service

  * Support for Demand Signal features

    * ``oci demand-signal occ-demand-signal-collection list-occ-demand-signals``
    * ``oci demand-signal occ-demand-signal change-compartment``
    * ``oci demand-signal occ-demand-signal create``
    * ``oci demand-signal occ-demand-signal delete``
    * ``oci demand-signal occ-demand-signal get``
    * ``oci demand-signal occ-demand-signal update``
    * ``oci demand-signal occ-demand-signal patch``

  * Support for Capacity Management features

    * ``oci capacity-management occ-capacity-request patch-internal``
    * ``oci capacity-management occ-overview-collection list-internal-namespace-occ-overviews``
    * ``oci capacity-management occ-overview-collection list``

* Database Management service

  * Support for Standby Database Monitoring

    * ``oci database-management peer-database-metrics get``
    * ``oci database-management dataguard-performance-metrics get``

* Database service

  * Support for External Database Connector

    * ``oci db external-db-connector create-macs-connector --connection-credentials``
    * ``oci db external-db-connector update-macs-connector --connection-credentials``

* Java Management Service

  * Support for tagging related optional parameters in Downloads API

    * ``oci jms-java-downloads java-download-report create --defined-tags, --freeform-tags``
    * ``oci jms-java-downloads java-license-acceptance-record create --defined-tags, --freeform-tags``
    * ``oci jms-java-downloads java-license-acceptance-record update --defined-tags, --freeform-tags``

3.41.0 - 2024-05-21
--------------------
Added
~~~~~
* Data Science Service

  * Support for Nested Resource Principal

    * ``oci data-science job-run create --opc-parent-rpt-url``
    * ``oci data-science model-deployment create --opc-parent-rpt-url``
    * ``oci data-science pipeline-run create --opc-parent-rpt-url``

  * Support for ML Pipelines v2

    * ``oci data-science pipeline update --infrastructure-configuration-details``
    * ``oci data-science pipeline-run cancel --terminate-gracefully``

* Support for managing Schedules in new Resource Scheduler Service

  * ``oci resource-scheduler``

* Support for backup and replacement of MASTER, UTILITY and EDGE NODES in Big Data Service

  * ``oci bds instance backup-node``
  * ``oci bds instance create-node-backup-configuration``
  * ``oci bds instance create-node-replace-configuration``
  * ``oci bds instance get-node-backup``
  * ``oci bds instance get-node-backup-configuration``
  * ``oci bds instance get-node-replace-configuration``
  * ``oci bds instance list-node-backup-configurations``
  * ``oci bds instance list-node-backups``
  * ``oci bds instance list-node-replace-configurations``
  * ``oci bds instance replace-node``
  * ``oci bds instance update-node-backup-configuration``
  * ``oci bds instance update-node-replace-configuration``
  * ``oci bds node-backup delete``
  * ``oci bds node-backup-configuration delete``
  * ``oci bds node-replace-configuration remove``

3.40.3 - 2024-05-14
--------------------
Added
~~~~~
* Support for new optional parameter --file-system-configuration-details in vm cluster for Database Service

  * ``oci db vm-cluster create --file-system-configuration-details``
  * ``oci db vm-cluster update --file-system-configuration-details``

* Support for PPv2 ( Proxy protocol version 2) feature for Network Load Balancer

  * ``oci nlb listener create --is-ppv2-enabled``
  * ``oci nlb listener update --is-ppv2-enabled``

* Support for the Marketplace Private Offer Service

  * ``oci marketplace-private-offer``

* Support for new commands in Marketplace Publisher Service

  * ``oci marketplace-publisher attachment``
  * ``oci marketplace-publisher offer``

* OCI Email Service

  * Support for Custom Return Path for Sent Emails in Email Delivery Service

    * ``oci email email-return-path``

  * Support for new optional parameter --domain-verification-id in email domain

    * ``oci email domain create --domain-verification-id``
    * ``oci email domain update --domain-verification-id``

* Support for Session Resumption in Load Balancing service

  * ``oci lb listener create --ssl-session-resumption``
  * ``oci lb listener update --ssl-session-resumption``

3.40.2 - 2024-05-07
--------------------
Added
~~~~~
* OCI Virtual Cloud Network Service

  * Support for new ip inventory and notification feature

    * ``oci network ipam list-ip-inventory``
    * ``oci network ipam get-resource-ip-inventory``
    * ``oci network ipam get-subnet-cidr-utilization``
    * ``oci network ipam get-subnet-ip-inventory``
    * ``oci network ipam get-vcn-overlap``

* OCI Load Balancer Service

  * Support for accidental delete protection preventing deletion of a load-balancer and its listeners or backends if they are configured to accept traffic

    * ``oci lb load-balancer create --is-delete-protection-enabled``
    * ``oci lb load-balancer update --is-delete-protection-enabled``

  * Support for new optional parameter limiting the number of simultaneous connections a load-balancer can make to its backends or listeners

    * ``oci lb backend create --max-connections``
    * ``oci lb backend update --max-connections``
    * ``oci lb backend-set create --backend-max-connections``
    * ``oci lb backend-set update --backend-max-connections``

* OCI Big Data Service

  * Support for new optional parameter for os patching configs

    * ``oci bds instance install-os-patch --patching-configs``

  * Support for new commands for os patching configs

    * ``oci bds instance install-os-patch-batching-based-patching-configs``
    * ``oci bds instance install-os-patch-downtime-based-patching-configs``

* OCI Disaster Recovery Cloud Service

  * Support for user-defined pause group in disaster recovery plan

    * ``oci disaster-recovery dr-plan update``

* OCI Database Service

  * Support for new optional parameter when creating/updating cloud vm clusters

    * ``oci db cloud-vm-cluster create --file-system-configuration-details``
    * ``oci db cloud-vm-cluster update --file-system-configuration-details``

Changed
~~~~~~~

* Upgraded the prompt-toolkit version to (>=3.0.38, <=3.0.43) for Python 3.7 and above

3.40.1 - 2024-04-30
--------------------
Added
~~~~~
* Database Service

  * Support for enabling unified auditing for DBHome

    * ``oci db db-home``

  * Support to create Grid Infrastructure type of custom software images

    * ``oci db database-software-image create --display-name, --compartment-id, --image-type "grid_image"``

  * Support to list custom software images greater than a given patchSet version, to find the images available for use in patching.

    * ``oci db database-software-image list --compartment-id, --image-type, --image-shape-family, --patch-set-greater-than-or-equal-to``

  * Support Cloud VM cluster in-place patching using custom Grid Infrastructure image

    * ``oci db cloud-vm-cluster update --cloud-vm-cluster-id, --gi-image-id, --update-action``

  * Support VM cluster in-place patching using custom Grid Infrastructure image

    * ``oci db vm-cluster update --vm-cluster-id, --gi-image-id, --update-action``

* Oracle Database Autonomous Recovery Service

  * Support for  Cancel Protected Database

    * ``oci recovery protected-database cancel-protected-database-deletion [options]``

  * Support for  Schedule Protected Database

    * ``oci recovery protected-database schedule-protected-database-deletion [options]``

  * Support for Network Security Group for RSS

    * ``oci recovery recovery-subnet create --nsg-ids  [options]``
    * ``oci recovery recovery-subnet update --nsg-ids  [options]``

* Data Catalog

  * Support for lineage metadata import

    * ``oci data-catalog data-asset import-lineage``

* Database Management Service

  * Support for monitoring ExaCC databases

    * ``oci database-management managed-database enable-database-management-feature-database-diagnostics-and-management-feature-details``
    * ``oci database-management managed-database enable-external-container-database-management-feature-external-database-diagnostics-and-management-feature-details``
    * ``oci database-management managed-database enable-external-non-container-database-management-feature-external-database-diagnostics-and-management-feature-details``

* Data Safe Service

  * Support for generate, list, get, delete and change compartment for pre-masking check before actual masking

    * ``oci data-safe masking-policy-health-report change-compartment --compartment-id | -c, --masking-policy-health-report-id, -? | -h | --help``
    * ``oci data-safe masking-policy-health-report delete --masking-policy-health-report-id, --force, -? | -h | --help``
    * ``oci data-safe masking-policy-health-report generate-health-report --masking-policy-id, --check-type, --compartment-id | -c, --defined-tags, --freeform-tags, -? | -h | --help, --tablespace, --target-id``
    * ``oci data-safe masking-policy-health-report get --masking-policy-health-report-id, -? | -h | --help``
    * ``oci data-safe masking-policy-health-report list --compartment-id | -c, --access-level, --all, --compartment-id-in-subtree, --display-name, -? | -h | --help, --masking-policy-health-report-id, --masking-policy-id, --target-id``
    * ``oci data-safe masking-policy-health-report list-masking-policy-health-report-logs --masking-policy-health-report-id, --all, -? | -h | --help, --message-type``

* Data Integration Service

  * Support for workspace properties in create/update workspace

    * ``oci data-integration workspace create``
    * ``oci data-integration workspace update``

3.40.0 - 2024-04-23
--------------------
Added
~~~~~
* Support for the new Cluster Placement Groups service

  * ``oci cpg``

* Support for new optional parameter domainId in ApproverInfo while managing ApprovalTemplate in Managed Access Service

    * ``oci oma approval-template create --approver-levels``
    * ``oci oma approval-template update --approver-levels``

* Cloud Guard And Security Zones Service

  * New resource adhocquery

    * ``oci cloud-guard adhoc-query create``
    * ``oci cloud-guard adhoc-query delete``
    * ``oci cloud-guard adhoc-query get``
    * ``oci cloud-guard adhoc-query list``
    * ``oci cloud-guard adhoc-query-result-collection get-adhoc-query-result-content``
    * ``oci cloud-guard adhoc-query-result-collection list-adhoc-query-results``

  * New resource savedQuery

    * ``oci cloud-guard saved-query change-compartment``
    * ``oci cloud-guard saved-query create``
    * ``oci cloud-guard saved-query delete``
    * ``oci cloud-guard saved-query get``
    * ``oci cloud-guard saved-query list``
    * ``oci cloud-guard saved-query update``

  * Support for the new enum scheduledQuery for parameter feedprovider in data source resource

    * ``oci cloud-guard data-source create-data-source-scheduled-query-data-source-obj-details``
    * ``oci cloud-guard data-source update-data-source-scheduled-query-data-source-obj-details``

* Core Services

  * Support for new optional parameters in the instance launch APIs

    * ``oci compute instance launch --cluster-placement-group-id``
    * ``oci compute instance launch-instance-generic-bm-launch-instance-platform-config --cluster-placement-group-id``

  * Support for assigning cluster placement group to boot volume creation in block storage.

    * ``oci bv boot-volume create --cluster-placement-group-id``

  * Support for assigning cluster placement group to boot volume creation from boot volume replica in block storage.

    * ``oci bv boot-volume create-boot-volume-boot-volume-source-from-boot-volume-replica-details --cluster-placement-group-id``

  * Support for assigning cluster placement group to block volume creation in block storage.

    * ``oci bv volume create --cluster-placement-group-id``

  * Support for assigning cluster placement group to block volume creation from block volume replica in block storage.

    * ``oci bv volume create-volume-volume-source-from-block-volume-replica-details --cluster-placement-group-id``

  * Support for listing volumes by cluster placement group in block storage.

    * ``oci bv volume list --cluster-placement-group-id``

  * Support for assigning cluster placement group to volumes after restoring from a volume group clone, backup, or replica in block storage.

    * ``oci bv volume-group create --cluster-placement-group-id``

* OS Management Hub Service

  * Support for events

    * ``oci os-management-hub event``

  * Support for installing windows updates for all instances in a compartment

    * ``oci os-management-hub install-all-windows-updates-in-compartment``

  * Support for moving resources to different compartments

    * ``oci os-management-hub lifecycle-environment change-compartment``
    * ``oci os-management-hub managed-instance-group change-compartment``
    * ``oci os-management-hub management-station change-compartment``
    * ``oci os-management-hub profile change-compartment``
    * ``oci os-management-hub scheduled-job change-compartment``
    * ``oci os-management-hub software-source change-compartment``

  * Support for new commands for managed instances

    * ``oci os-management-hub managed-instance attach-profile``
    * ``oci os-management-hub managed-instance detach-profile``
    * ``oci os-management-hub managed-instance delete``
    * ``oci os-management-hub managed-instance install-windows-updates``
    * ``oci os-management-hub managed-instance list-available-windows-updates``
    * ``oci os-management-hub managed-instance list-installed-windows-updates``

  * Support for new commands for managed instance groups

    * ``oci os-management-hub managed-instance-group install-windows-updates``
    * ``oci os-management-hub managed-instance-group switch-module-stream``

  * Support for new commands for management station

    * ``oci os-management-hub management-station refresh-management-station-config``

  * Support for new commands for software sources

    * ``oci os-management-hub software-source add-packages``
    * ``oci os-management-hub software-source get-software-package-by-name``
    * ``oci os-management-hub software-source list-all-software-packages``
    * ``oci os-management-hub software-source list-software-sources-with-package``
    * ``oci os-management-hub software-source replicate-vendor-swsrc``
    * ``oci os-management-hub software-source update-versioned-custom-swsrc``

  * Support for new commands for windows updates

    * ``oci os-management-hub windows-update get``
    * ``oci os-management-hub windows-update list-windows-updates``

Changed
~~~~~~~
* [BREAKING] OS Management Hub Service

  * Optional parameter ``--vulnerability-type`` has now been made required in the following command

    * ``oci os-management-hub managed-instance get-content``

  * Optional parameter ``--managed-instances`` has now been made required in the following commands

    * ``oci os-management-hub managed-instance-group attach-managed-instances``
    * ``oci os-management-hub managed-instance-group detach-managed-instances``

  * Optional parameter ``--software-sources`` has now been made required in the following commands

    * ``oci os-management-hub managed-instance-group attach-software-sources``
    * ``oci os-management-hub managed-instance-group detach-software-sources``

  * Optional parameter ``--module-name`` has now been made required in the following commands

    * ``oci os-management-hub managed-instance-group disable-module-stream``
    * ``oci os-management-hub managed-instance-group enable-module-stream``
    * ``oci os-management-hub managed-instance-group install-module-profile``

  * Optional parameter ``--package-names`` has now been made required in the following commands

    * ``oci os-management-hub managed-instance-group install-packages``
    * ``oci os-management-hub managed-instance-group remove-packages``

3.39.1 - 2024-04-16
--------------------
Added
~~~~~
* Database Service

  * New Autonomous Database Software Image Introduced

    * ``oci db autonomous-database-software-image``

  * Support for Autonomous Database Software Image

    * ``oci db autonomous-database-software-image change-compartment --autonomous-database-software-image-id``
    * ``oci db autonomous-database-software-image create``
    * ``oci db autonomous-database-software-image delete``
    * ``oci db autonomous-database-software-image get --autonomous-database-software-image-id``
    * ``oci db autonomous-database-software-image list``
    * ``oci db autonomous-database-software-image update --autonomous-database-software-image-id``

  * Support for optional parameter --database-software-image-id

    * ``oci db autonomous-container-database create --database-software-image-id``

* Database Migration Service

  * Support for AWS_S3 with object_storage_bucket migrations

    * ``oci database-migration migration create-migration-aws-s3-data-transfer-medium-details``
    * ``oci database-migration migration update-migration-aws-s3-data-transfer-medium-details``

* Generative AI Interface Service

  * Support for Chat Results

    * ``oci generative-ai-inference chat-result chat``
    * ``oci generative-ai-inference chat-result chat-cohere-chat-request``
    * ``oci generative-ai-inference chat-result chat-dedicated-serving-mode``
    * ``oci generative-ai-inference chat-result chat-generic-chat-request``
    * ``oci generative-ai-inference chat-result chat-on-demand-serving-mode``

* Network Load Balancer Service

  * Addition of optional parameter --is-fail-open in backend-set and health-checker update commands

    * ``oci nlb backend-set update``
    * ``oci nlb health-checker update``

* Redis Service

  * Support for new optional parameters --nsg-ids in redis cluster commands

    * ``oci redis redis-cluster create --nsg-ids``
    * ``oci redis redis-cluster update --nsg-ids``

* Generative AI Service

  * Support Dedicated AI Cluster Unit Shape LARGE_COHERE_V2 in the Generative AI Service Management

    * ``oci generative-ai dedicated-ai-cluster``

* Usage Service

  * Support for Usage Statements in email recipient groups

    * ``oci usage-api email-recipients-group create``
    * ``oci usage-api email-recipients-group delete``
    * ``oci usage-api email-recipients-group get``
    * ``oci usage-api email-recipients-group list``
    * ``oci usage-api email-recipients-group update``

* AI Language Service

  * Support for extracting entities from healthcare records

    * ``oci ai language batch-detect-health-entities --documents --endpoint-id --is-detect-assertions --is-detect-relationships``
    * ``oci ai language batch-detect-pii-entities``

* Process Automation Service

  * Support for the Oracle Process Automation instance start and stop operation

    * ``oci opa opa-instance start --opa-instance-id``
    * ``oci opa opa-instance stop --opa-instance-id``

3.39.0 - 2024-04-09
--------------------
Removed
~~~~~

* [BREAKING] Application Migration Service removed

  * ``oci application-migration``

Added
~~~~~
* Support for oke workload resource principal signer auth using --auth oke_workload_identity option

* OCI Network Load Balancer Service

  * Support for the Domain Name System based backend health check

    * ``oci nlb health-checker update --dns``

  * Support for Fail Open in Network Load Balancer service

    * ``oci nlb backend-set create --is-fail-open``
    * ``oci nlb backend-set update --is-fail-open``

  * New NLB feature with Instant FailOver

    * ``oci nlb backend-set create  --is-instant-failover-enabled'``
    * ``oci nlb backend-set update  --is-instant-failover-enabled'``

* Stack Monitoring Service

  * Support for adding/updating source type and resource category for resource types in the Stack Monitoring Service

    * ``oci stack-monitoring resource-type create --resource-category, --source-type``
    * ``oci stack-monitoring resource-type create-system-format-resource-type --resource-category, --source-type``
    * ``oci stack-monitoring resource-type update --resource-category, --source-type``
    * ``oci stack-monitoring resource-type update-system-format-resource-type --resource-category, --source-type``

  * Support for searching resources based on resource category,  sourceType, multiple compartments, multiple lifecycle states in the Stack Monitoring Service

    * ``oci stack-monitoring resource search --compartment-ids, --lifecycle-states, --resource-category, --source-type``

  * Support for filtering listed resources based on lifecycle status in the Stack Monitoring Service

    * ``oci stack-monitoring resource list --status``

  * Support for creating tasks with new config parameters in the Stack Monitoring Service

    * ``oci stack-monitoring resource-task import-telemetry-resources --console-path-prefix, --external-id-mapping, --up-status-mappings, --resource-name-filter, --resource-name-mapping, --resource-type-filter, --resource-type-mapping, --service-base-url, --use-metrics-for-status``

* Support for setting nested resource principal parent URL in the Oracle Cloud Infrastructure Data Flow service

  * ``oci data-flow run create --opc-parent-rpt-url``
  * ``oci data-flow run submit --opc-parent-rpt-url``

3.38.1 - 2024-04-02
-------------------
Added
~~~~~

* OCI Network Load Balancer Service

  * Support for assigned private Ip by adding new optional parameters in the Network Load Balancer Service for creation and update
  * ``oci nlb network-load-balancer create --assigned-ipv6, --assigned-private-ipv4``
  * ``oci nlb network-load-balancer update --assigned-ipv6``

  * LBaaS Support for TLSv1.3

* OCI Email-Delivery Service

  * Support for Configuration API in Email-Delivery Service
  * Support for sending mails via Https for Email Delivery Service

* OCI Cloud Guard service

  * Support for the status field in creating data source resource of Cloud Guard Service
  * ``oci cloud-guard data-source create --status``
  * ``oci cloud-guard data-source create-data-source-logging-query-data-source-details --status``

Removed ~~~~~

* [BREAKING] Commands removed

  * ``oci devops code-search list-results``
  * ``oci devops project delete-project-settings``
  * ``oci devops project get-notification-preference``
  * ``oci devops project get-project-settings``
  * ``oci devops project list-project-analytics-authors``
  * ``oci devops project summarize-project-analytics``
  * ``oci devops project update-notification-preference``
  * ``oci devops project update-project-settings``
  * ``oci devops protected-branch create-or-update``
  * ``oci devops protected-branch delete``
  * ``oci devops protected-branch list-protected-branches``
  * ``oci devops pull-request create``
  * ``oci devops pull-request create-pull-request-attachment``
  * ``oci devops pull-request decline``
  * ``oci devops pull-request delete``
  * ``oci devops pull-request delete-pull-request-attachment``
  * ``oci devops pull-request execute-merge-pull-request``
  * ``oci devops pull-request get``
  * ``oci devops pull-request get-pull-request-attachment``
  * ``oci devops pull-request get-pull-request-attachment-content``
  * ``oci devops pull-request get-pull-request-change-summary-metrics``
  * ``oci devops pull-request get-pull-request-notification-preference``
  * ``oci devops pull-request list-build-run-snapshots``
  * ``oci devops pull-request list-pull-request-activities``
  * ``oci devops pull-request list-pull-request-attachments``
  * ``oci devops pull-request list-pull-request-commits``
  * ``oci devops pull-request list-pull-request-file-changes``
  * ``oci devops pull-request list-pull-requests``
  * ``oci devops pull-request patch``
  * ``oci devops pull-request reopen``
  * ``oci devops pull-request review``
  * ``oci devops pull-request unsubscribe``
  * ``oci devops pull-request update``
  * ``oci devops pull-request update-pull-request-notification-preference``
  * ``oci devops pull-request validate-merge-pull-request``
  * ``oci devops pull-request-comment create-pull-request-comment``
  * ``oci devops pull-request-comment delete-pull-request-comment``
  * ``oci devops pull-request-comment get-pull-request-comment``
  * ``oci devops pull-request-comment like-pull-request-comment``
  * ``oci devops pull-request-comment list-pull-request-comments``
  * ``oci devops pull-request-comment unlike-pull-request-comment``
  * ``oci devops pull-request-comment update-pull-request-comment``
  * ``oci devops repository create-or-update-git-branch-details``
  * ``oci devops repository create-or-update-git-tag-details``
  * ``oci devops repository delete-git-ref``
  * ``oci devops repository delete-repository-settings``
  * ``oci devops repository get-repository-notification-preference``
  * ``oci devops repository get-repository-settings``
  * ``oci devops repository list-fork-sync-statuses``
  * ``oci devops repository list-pull-request-authors``
  * ``oci devops repository list-repository-analytics-authors``
  * ``oci devops repository list-repository-build-run-snapshots``
  * ``oci devops repository summarize-repository-analytics``
  * ``oci devops repository sync``
  * ``oci devops repository update-repository-notification-preference``
  * ``oci devops repository update-repository-settings``
  * ``oci devops repository-private-access change-compartment``
  * ``oci devops repository-private-access create``
  * ``oci devops repository-private-access delete``
  * ``oci devops repository-private-access get``
  * ``oci devops repository-private-access list``
  * ``oci devops repository-private-access list-private-projects``
  * ``oci devops repository-private-access recover``
  * ``oci devops repository-private-access update``
      

3.38.0 - 2024-03-26
-------------------
Added
~~~~~

* OCI Network Load Balancer Service

  * Support for symmetric hashing when creating or updating network load balancers.

    * ``oci nlb network-load-balancer create --is-symmetric-hash-enabled``
    * ``oci nlb network-load-balancer update --is-symmetric-hash-enabled``

* OCI Monitoring Service

  * Support for new optional parameters in the create or update alarms commands.

    * ``oci monitoring alarm create --overrides --rule-name --notification-version``
    * ``oci monitoring alarm update --overrides --rule-name --notification-version``

* OCI Database Management Service

  * Support for new command to retrieve fleet health metrics for MySQL HeatWave clusters.

    * ``oci database-management managed-my-sql-databases heat-wave-fleet-metrics``

  * Support for new optional parameter when retrieving MySQL fleet metrics.

    * ``oci database-management managed-my-sql-databases my-sql-fleet-metrics --is-heat-wave-enabled``

* OCI Database Service

  * Support for creating and updating a refreshable clone with auto-refresh for an autonomous database.

    * ``oci db autonomous-database create-refreshable-clone --auto-refresh-point-lag-in-seconds``
    * ``oci db autonomous-database update --auto-refresh-point-lag-in-seconds``

* OCI Logging Service

  * Support for new logging agent-configuration commands.

    * ``oci logging agent-configuration create-unified-agent-configuration-unified-agent-monitoring-configuration-details``
    * ``oci logging agent-configuration update-unified-agent-configuration-unified-agent-monitoring-configuration-details``

  * Support for new optional parameters in the following commands

    * ``oci logging agent-configuration create-log-configuration --service-configuration-filter``
    * ``oci logging agent-configuration update-log-configuration --service-configuration-filter``

* OCI Devops Deployment Service

  * Support for new groups of commands.

    * ``oci devops code-search``
    * ``oci devops protected-branch``
    * ``oci devops pull-request``
    * ``oci devops pull-request-comment``
    * ``oci devops repository-private-access``

  * Support for new commands in the ``deploy-artifact`` group.

    * ``oci devops deploy-artifact create-helm-command-spec``
    * ``oci devops deploy-artifact update-helm-command-spec``

  * Support for new commands in the ``project`` group.

    * ``oci devops project get-project-settings``
    * ``oci devops project update-project-settings``
    * ``oci devops project delete-project-settings``
    * ``oci devops project get-notification-preference``
    * ``oci devops project update-notification-preference``
    * ``oci devops project list-project-analytics-authors``
    * ``oci devops project summarize-project-analytics``

  * Support for new commands in the ``repository`` group.

    * ``oci devops repository create-or-update-git-branch-details``
    * ``oci devops repository create-or-update-git-tag-details``
    * ``oci devops repository delete-git-ref``
    * ``oci devops repository delete-repository-settings``
    * ``oci devops repository get-repository-settings``
    * ``oci devops repository get-repository-notification-preference``
    * ``oci devops repository list-fork-sync-statuses``
    * ``oci devops repository list-pull-request-authors``
    * ``oci devops repository list-repository-analytics-authors``
    * ``oci devops repository list-repository-build-run-snapshots``
    * ``oci devops repository summarize-repository-analytics``
    * ``oci devops repository sync``
    * ``oci devops repository update-repository-notification-preference``
    * ``oci devops repository update-repository-settings``

  * Support for new parameters in the following commands.

    * ``oci devops repository create --parent-repository-id``
    * ``oci devops repository get-commit-diff --target-repository-id``
    * ``oci devops repository list-commit-diffs --target-repository-id``
    * ``oci devops deploy-stage create-deploy-oke-stage --oke-environment-details``
    * ``oci devops deploy-stage update-deploy-oke-stage --oke-environment-details``
    * ``oci devops deploy-stage create-oke-helm-chart-stage --oke-environment-details --helm-command-artifact-ids --purpose --is-uninstall-on-stage-delete``
    * ``oci devops deploy-stage update-oke-helm-chart-stage --oke-environment-details --helm-command-artifact-ids --purpose --is-uninstall-on-stage-delete``


Changed
~~~~~~~

* [BREAKING] Optional parameters ``--description`` and ``--display-name`` have now been made required in the following commands in OCI Logging Service.

  * ``oci logging agent-configuration create``
  * ``oci logging agent-configuration create-log-configuration``


3.37.14 - 2024-03-19
--------------------
Added
~~~~~
* The AI Language service

  * Support for async jobs and document translation

    * ``oci ai language job create --compartment-id --input-location --model-metadata-details --output-location --description, --display-name --input-configuration``
    * ``oci ai language job update --job-id --description --display-name``
    * ``oci ai language job list --compartment-id  --all --display-name --id``
    * ``oci ai language job get --job-id``
    * ``oci ai language job delete --job-id``
    * ``oci ai language job cancel --job-id``
    * ``oci ai language job change-compartment --compartment-id --job-id``

* Application Performance Monitoring Trace service

  * Support for attribute management for trace and synthetic

    * ``oci apm-traces attributes activate ``
    * ``oci apm-traces attributes deactivate ``
    * ``oci apm-traces attributes auto-activate-status ``
    * ``oci apm-traces attributes pin ``
    * ``oci apm-traces attributes unpin ``
    * ``oci apm-traces attributes update-auto-activate ``
    * ``oci apm-traces attributes update-notes ``
    * ``oci apm-traces attributes update-attribute ``

  * Support for new optional parameters in the get trace and get span

    * ``oci apm-traces trace trace get --time-trace-started-gte --time-trace-started-lt --trace-namespace ``
    * ``oci apm-traces trace span get --time-trace-started-gte --time-trace-started-lt --trace-namespace ``

3.37.13 - 2024-03-12
--------------------
Added
~~~~~
* Database Service

  * Support for New Dev License Type in Oracle Autonomous Database (on Dedicated Infrastructure)

    * ``oci db autonomous-database create --is-dev-tier``
    * ``oci db autonomous-database create-adb-cross-region-data-guard-details --is-dev-tier``
    * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details --is-dev-tier``
    * ``oci db autonomous-database create-autonomous-database-create-cross-tenancy-disaster-recovery-details --is-dev-tier``
    * ``oci db autonomous-database create-from-backup-id --is-dev-tier``
    * ``oci db autonomous-database create-from-backup-timestamp --is-dev-tier``
    * ``oci db autonomous-database create-from-clone --is-dev-tier``
    * ``oci db autonomous-database create-refreshable-clone --is-dev-tier``
    * ``oci db autonomous-database create-virtual-clone --is-dev-tier``
    * ``oci db autonomous-database update --is-dev-tier``

  * Support for new optional parameters to create Autonomous Container Database

    * ``oci db autonomous-container-database create --db-split-threshold --distribution-affinity --net-services-architecture --vm-failover-reservation``

* Support for Autoscaling in the Data Science Model Deployment service

3.37.12 - 2024-03-05
--------------------
Added
~~~~~
* Support for server streaming events in the Generative AI Inference Service when `inference-request-is-stream` is set to true

  * ``oci generative-ai-inference generate-text-result generate-text-cohere-llm-inference-request --inference-request-is-stream``
  * ``oci generative-ai-inference generate-text-result generate-text-llama-llm-inference-request --inference-request-is-stream``

* Speech service

  * Support for Whisper Models in creation of transcription job

    * ``oci speech transcription-job create --model-details``

  * Support for Delete Job API in transcription job

    * ``oci speech transcription-job delete --transcription-job-id``

* Operations Insights service

  * Support for updating host-insights

    * ``oci opsi host-insights update-pe-comanaged-host``

  * Support to receive insights from resources in child compartments for news reports

    * ``oci opsi news-reports create --are-child-compartments-included, --day-of-week``

  * Support to update more parameters for news reports

    * ``oci opsi news-reports update --are-child-compartments-included, --day-of-week, --description, --name``

  * Support to choose the day of the week the report is received for news reports

    * ``oci opsi news-reports update --are-child-compartments-included, --day-of-week, --description, --name``

Changed
~~~~~~~
* Upgraded the cryptography version to (>=3.2.1,<43.0.0) and pyOpenSSL version to (>=17.5.0,<25.0.0)

3.37.11 - 2024-02-27
--------------------
Added
~~~~~
* Support for retrieving logs in Container Instance Service.

  * ``oci container-instances container retrieve-logs --is-previous``

* Support for queue source feature in Connector Hub Service.

  * ``oci och queue-source``

* Support for asynchronous data asset export in Data Catalog Service.

  * ``oci data-catalog data-asset asynchronous-export``

* Support for the secret auto-generation in Vault Secret Management Service.

  * ``oci vault secret create-base64 --enable-auto-generation --secret-generation-context``
  * ``oci vault secret update --enable-auto-generation --secret-generation-context``
  * ``oci vault secret update-base64 --enable-auto-generation --secret-generation-context``

* Support for new optional parameters in key commands to enable or modify automatic key rotation settings in Key Management Service.

  * ``oci kms management key create --is-auto-rotation-enabled``
  * ``oci kms management key create --is-auto-rotation-enabled --auto-key-rotation-details``
  * ``oci kms management key import --is-auto-rotation-enabled``
  * ``oci kms management key import --is-auto-rotation-enabled --is-auto-rotation-enabled``
  * ``oci kms management key update --is-auto-rotation-enabled``
  * ``oci kms management key update --is-auto-rotation-enabled --auto-key-rotation-details``

* Support for tagging for following commands in Database Management Service.

  * ``oci database-management managed-database``
  * ``oci database-management managed-database-group``
  * ``oci database-management external-db-system-discovery``
  * ``oci database-management external-db-system``
  * ``oci database-management external-cluster``
  * ``oci database-management external-cluster-instance``
  * ``oci database-management external-asm``
  * ``oci database-management external-asm-instance``
  * ``oci database-management external-listener``
  * ``oci database-management external-db-node``
  * ``oci database-management external-db-home``
  * ``oci database-management external-db-system-connector``
  * ``oci database-management external-exadata-infrastructure``
  * ``oci database-management external-exadata-storage-connector``
  * ``oci database-management external-exadata-storage-grid``
  * ``oci database-management external-exadata-storage-server``
  * ``oci database-management job``
  * ``oci database-management private-endpoint``

* Operator Access Control Service

  * Support for multiple approvals (two approvals).

    * ``oci opctl operator-control create --number-of-approvers``
    * ``oci opctl operator-control update --number-of-approvers``

  * Support for forwarding Hypervisor logs.

    * ``oci opctl operator-control-assignment create --is-hypervisor-log-forwarded``
    * ``oci opctl operator-control-assignment update --is-hypervisor-log-forwarded``

  * Support for Assignment health check.

    * ``oci opctl operator-control-assignment get-assignment-validation-status --operator-control-assignment-id``
    * ``oci opctl operator-control-assignment validate-operator-assignment --operator-control-assignment-id --action-name``

* Database Service

  * Support for the cluster placement group feature in Cloud Exadata Infrastructure.

    * ``oci db cloud-exa-infra create --cluster-placement-group-id``
    * ``oci db cloud-exa-infra list --cluster-placement-group-id``

  * Support for Create Autonomous Dataguard Association.

    * ``oci db autonomous-container-database-dataguard create --peer-autonomous-vm-cluster-id --peer-cloud-autonomous-vm-cluster-id --peer-db-unique-name``

* Digital Assistant Service

  * Support for specifying dialog version when creating skills.

    * ``oci oda management skill create --dialog-version``

  * Support for bulk creation of skill entities.

    * ``oci oda management skill bulk-create-skill-entities --items --oda-instance-id --skill-id``

  * Support for training skill query entities.

    * ``oci oda management skill train --items --oda-instance-id``

  * Support for cascading delete of skill custom entities.

    * ``oci oda management skill cascading-delete-skill-custom-entities --oda-instance-id --skill-id``

3.37.10 - 2024-02-20
--------------------
Added
~~~~~
* Support for Bring Your Own Container Jobs (v2) in the Data Science service

  * ``oci data-science job create --job-environment-configuration-details``
  * ``oci data-science job-run create --job-environment-configuration-override-details``

* Support for Secure Desktops Service

  * ``oci desktops``

* Support for new optional parameter in Language Service

  * ``oci ai language batch-detect-language --should-ignore-transliteration --chars-to-consider --endpoint-id``
  * ``oci ai language batch-detect-pii-entities --endpoint-id``
  * ``oci ai language batch-detect-key-phrases --endpoint-id``
  * ``oci ai language batch-detect-sentiments --endpoint-id``

* Core Service

  * Support for new optional parameter

    * ``oci compute instance update --platform-config``

  * Support for new commands

    * ``oci compute instance update-instance-amd-vm-update-instance-platform-config``
    * ``oci compute instance update-instance-intel-vm-update-instance-platform-config``

3.37.9 - 2024-02-13
-------------------
Added
~~~~~

* Support for new optional parameter isReplicateAutomaticBackups in the Database Service

  * ``oci db autonomous-database change-disaster-recovery-configuration --is-replicate-automatic-backups``
  * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details --is-replicate-automatic-backups``
 
Changed
~~~~~~~
* Loganalytics service

  * Support for additional attributes in entity and topology

    * ``oci log-analytics entity create --metadata, --time-last-discovered``
    * ``oci log-analytics entity list --metadata-equals``
    * ``oci log-analytics entity update --metadata, --time-last-discovered``
    * ``oci log-analytics entity upload-discovery-data --log-group-id``
    * ``oci log-analytics entity-topology list --metadata-equals``

  * Support for historic collection and log type while creating object collection rule

    * ``oci log-analytics object-collection-rule create --is-force-historic-collection, --log-type``

  * Support for position aware parsers

    * ``oci log-analytics parser extract-structured-log-field-paths --is-position-aware``
    * ``oci log-analytics parser extract-structured-log-header-paths --is-position-aware``
    * ``oci log-analytics parser test-parser --is-position-aware``
    * ``oci log-analytics parser upsert-parser --is-position-aware``

  * Support for filtering detection rules based on target service

    * ``oci log-analytics rule list --target-service``

  * Support for filtering scheduled tasks based on target service

    * ``oci log-analytics scheduled-task list --target-service``

  * Support for filtering log sources based on their type

    * ``oci log-analytics source list-sources --source-type``

  * Support for additional recall and release attributes

    * ``oci log-analytics storage recall-archived-data --is-use-recommended-data-set``
    * ``oci log-analytics storage release-recalled-data --collection-id``

  * Support for opc-meta-properties header while uploading log events

    * ``oci log-analytics upload upload-log-events-file --opc-meta-properties``

3.37.8 - 2024-02-06
--------------------
Added
~~~~~

* Support for the Globally Distributed Database Service

  * ``oci gdd``

* Support for Data Sources, including Prometheus Emitter, in the Management Agent Service

  * ``oci management-agent agent create-prometheus-emitter``

* Support for Bring Your Own Certificates in MySQL HeatWave Database Service

  * ``oci mysql db-system clone --secure-connections``
  * ``oci mysql db-system create --secure-connections``
  * ``oci mysql db-system import --secure-connections``
  * ``oci mysql db-system update --secure-connections``

* Support for resource locking operations in the Digital Media Services

  * ``oci media-services media-asset add --type full``

* Vault Secret Management Service

  * Support for the secret rotation

    * ``oci vault secret rotate``

  * Support for cancelling the ongoing rotation

    * ``oci vault secret cancelrotation``

* Vault Key Management Service

  * Support for Dedicated KMS

    * ``oci kms kms-hsm-cluster hsm-cluster cancel-hsm-cluster-deletion --hsm-cluster-id``
    * ``oci kms kms-hsm-cluster hsm-cluster change-compartment --compartment-id``
    * ``oci kms kms-hsm-cluster hsm-cluster create --compartment-id``
    * ``oci kms kms-hsm-cluster hsm-cluster download-certificate-signing-request --hsm-cluster-id``
    * ``oci kms kms-hsm-cluster hsm-cluster get --hsm-cluster-id``
    * ``oci kms kms-hsm-cluster hsm-cluster list --compartment-id``
    * ``oci kms kms-hsm-cluster hsm-cluster schedule-hsm-cluster-deletion --hsm-cluster-id, --time-of-deletion``
    * ``oci kms kms-hsm-cluster hsm-cluster update --hsm-cluster-id, --defined-tags, --display-name, --force, --freeform-tags``
    * ``oci kms kms-hsm-cluster hsm-cluster upload-partition-certificates --hsm-cluster-id, --partition-certificate, --partition-owner-certificate``
    * ``oci kms kms-hsm-cluster hsm-partition get --hsm-cluster-id, --hsm-partition-id``
    * ``oci kms kms-hsm-cluster hsm-partition get-pre-co-user-credentials --hsm-cluster-id``
    * ``oci kms kms-hsm-cluster hsm-partition list --hsm-cluster-id, --all``

3.37.7 - 2024-01-30
--------------------
Added
~~~~~
* Support for Capacity Management features in OCI Control Center service

  * ``oci capacity-management occ-availability-catalog-collection list``
  * ``oci capacity-management occ-availability-catalog list``
  * ``oci capacity-management occ-capacity-request create``
  * ``oci capacity-management occ-capacity-request delete``
  * ``oci capacity-management occ-capacity-request get``
  * ``oci capacity-management occ-capacity-request update``

* Support for Named Credential in the Database Management service

  * ``oci database-management named-credential create``
  * ``oci database-management named-credential get``
  * ``oci database-management named-credential list``
  * ``oci database-management named-credential update``
  * ``oci database-management named-credential change-compartment``
  * ``oci database-management named-credential delete``
  * ``oci database-management managed-database list-users --opc-named-credential-id --managed-database-id``

Modified
~~~~~~~~
* Data integration service
  * Support for REST connectivity with oath2
    * ``oci data-integration data-asset create``


3.37.6 - 2024-01-25
--------------------
Added
~~~~~
* Support for the new Generative AI Service Inference Service 

  * ``oci generative-ai-inference``

3.37.5 - 2024-01-23
--------------------
Added
~~~~~

* Support for the new Generative AI Service Management

  * ``oci generative-ai``

* Support for Process Sets in Stack Monitoring service

  * ``oci stack-monitoring process-set``

3.37.4 - 2024-01-16
--------------------
Added
~~~~~

* Feature to add filtering support based on the Resource ID for CI service work requests.

  * ``oci container-instances work-request list --resource-id "$resourceid"``

* Support for new optional parameters in ADM service

  * ``oci adm vulnerability-audit create --build-type``
  * ``oci adm vulnerability-audit create-vulnerability-audit-external-resource-vulnerability-audit-source --build-type``
  * ``oci adm vulnerability-audit create-vulnerability-audit-oci-resource-vulnerability-audit-source --build-type``
  * ``oci adm vulnerability-audit create-vulnerability-audit-unknown-source-vulnerability-audit-source --build-type``
  * ``oci adm remediation-run list-application-dependency-recommendations --purl``
  * ``oci adm vulnerability-audit list-application-dependency-vulnerabilities --purl``
  * ``oci adm vulnerability-audit list-application-dependency-vulnerabilities --severity-greater-than-or-equal``
  * ``oci adm vulnerability-audit list --max-observed-severity-greater-than-or-equal-to``

* Data Safe Service

  * Support for updating risk level of the specified finding

    * ``oci data-safe finding update``

  * Support for listing all changes made by user to risk levels of findings of the specified assessment

    * ``oci data-safe security-assessment list-findings-change-audit-logs``

  * Support for security feature usage

    * ``oci data-safe security-assessment list-security-feature-analytics``
    * ``oci data-safe security-assessment list-security-features``

  * Support for viewing the top security findings in Data Safe Security Assessment

    * ``oci data-safe security-assessment list-finding-analytics``

  * Support for viewing the schemas that a user can access in Data Safe User Assessment.

    * ``oci data-safe database-table-access-entry get``
    * ``oci data-safe database-table-access-entry-collection list``
    * ``oci data-safe database-view-access-entry get``
    * ``oci data-safe database-view-access-entry-collection list``
    * ``oci data-safe role-grant-path-collection list``
    * ``oci data-safe security-policy-report get``
    * ``oci data-safe security-policy-report-collection list``
    * ``oci data-safe user-assessment list-user-access-analytics``

  * Support for new commands

    * ``oci data-safe peer-target-database``
    * ``oci data-safe report update``
    * ``oci data-safe target-database refresh``

  * Add new param peer-target-database-details

    * ``oci data-safe target-database create --peer-target-database-details``

* Support for new dimension-specific alarm suppression commands in Monitoring service

  * ``oci monitoring alarm-suppression``
  * ``oci monitoring alarm-suppression-collection list-alarm-suppressions``
  * ``oci monitoring alarm-suppression summarize-alarm-suppression-history``


Modified
~~~~~~~~

 * Changed trail-locations parameter as optional, added new optional parameters for Data Safe service

  * ``oci data-safe audit-profile calculate-audit-volume-available --trail-locations, --database-unique-name``
  * ``oci data-safe masking-policy apply-sdm-masking-policy-difference --sdm-masking-policy-difference-id``
  * ``oci data-safe work-request list --access-level, --compartment-id-in-subtree``

3.37.3 - 2024-01-10
--------------------
Fixed
~~~~~
* Reverted YubiKey authentication


3.37.2 - 2024-01-09
--------------------
Added
~~~~~
* Support for OCI CLI authentication using PKCS#11 compatible hardware devices like YubiKey

    * ``oci <command> --auth yubi_key``

* Support for summarizing disk Statistics and Host Recommendation in OPSI Host Capacity Service

  * ``oci opsi host-insights summarize-disk-statistics --compartment-id --id --analysis-time-interval``
  * ``oci opsi host-insights summarize-host-recommendation --compartment-id --id --analysis-time-interval --resource-metric``

* Support for new commands in the Apm Synthetic Service

  * ``oci apm-synthetics monitor create-dns-server-monitor  --apm-domain-id --display-name --monitor-type --vantage-points --repeat-interval-in-seconds  --target --name-server --protocol --record-type``
  * ``oci apm-synthetics monitor create-dns-sec-monitor  --apm-domain-id  --display-name --monitor-type --vantage-points --repeat-interval-in-seconds --target --name-server --protocol --record-type``
  * ``oci apm-synthetics monitor create-dns-trace-monitor  --apm-domain-id  --display-name --monitor-type --vantage-points --repeat-interval-in-seconds --target --name-server --protocol --record-type``
  * ``oci apm-synthetics monitor update-dns-server-monitor  --apm-domain-id --display-name --monitor-type --vantage-points --repeat-interval-in-seconds  --target --name-server --protocol --record-type``
  * ``oci apm-synthetics monitor update-dns-sec-monitor  --apm-domain-id  --display-name --monitor-type --vantage-points --repeat-interval-in-seconds --target --name-server --protocol --record-type``
  * ``oci apm-synthetics monitor update-dns-trace-monitor  --apm-domain-id  --display-name --monitor-type --vantage-points --repeat-interval-in-seconds --target --name-server --protocol --record-type``
  * ``oci apm-synthetics on-premise-vantage-point create --name --description --apm-domain-id``
  * ``oci apm-synthetics on-premise-vantage-point get  --on-premise-vantage-point-id --apm-domain-id``
  * ``oci apm-synthetics on-premise-vantage-point-collection list-on-premise-vantage-points  --apm-domain-id``

* Support for creation of up to 60 Containers per Container Instance instead of 10 in Container Instance Service

  * ``oci container-instances container-instance create --containers``

* Support for New Database Type "Golden Gate Stream Analytics (GGSA)" in the GoldenGate Service

  * ``oci goldengate connection list --assignable-deployment-type GGSA``
  * ``oci goldengate deployment create --deployment-type GGSA``
  * ``oci goldengate deployment-type-collection list-deployment-types --deployment-type GGSA``
  * ``oci goldengate deployment-version list --deployment-type GGSA``

* Support for "ORACLE_GOLDENGATE" resource type in Discovery and Monitoring in Stack Monitoring Service

  * ``oci stack-monitoring discovery-job``

* Support for response values "CREATE_BACKUP" and "DELETE_BACKUP" for Work Request Commands in Mysql Database Service

  * ``oci mysql work-request``


3.37.1 - 2023-12-12
--------------------
Added
~~~~~

* Support for carbon footprint reporting in the Usage Service

  * ``oci usage-api average-carbon-emission request``
  * ``oci usage-api clean-energy-usage request``
  * ``oci usage-api configuration request-usage-carbon-emission-config``
  * ``oci usage-api usage-carbon-emission-summary request-usage-carbon-emissions``
  * ``oci usage-api usage-carbon-emissions-query create``
  * ``oci usage-api usage-carbon-emissions-query delete``
  * ``oci usage-api usage-carbon-emissions-query get``
  * ``oci usage-api usage-carbon-emissions-query list``
  * ``oci usage-api usage-carbon-emissions-query update``

* Support for change compartment of configurations in the PostgreSQL service

  * ``oci psql configuration change-compartment``

* Support for Token Exchange in the IdentityDomains Service

  * ``oci identity-domains identity-propagation-trust``

* Support for resource locking in the Data Catalog Service

  * ``oci data-catalog catalog add``
  * ``oci data-catalog catalog remove``
  * ``oci data-catalog catalog-private-endpoint add``
  * ``oci data-catalog catalog-private-endpoint remove``
  * ``oci data-catalog metastore add``
  * ``oci data-catalog metastore remove``

* Support for new optional parameter --dedicated-vm-host-id in the Core Service

  * ``oci compute instance update --dedicated-vm-host-id``

* Support for additional attributes for existing APIs in the Data Safe Service

  * ``oci data-safe sensitive-data-model list-discovery-analytics --is-common, --sensitive-type-id``
  * ``oci data-safe sensitive-type list --is-common``

* Cloud Advisor Service

  * Support for non root compartment in list commands for resource action summary and history summary

    * ``oci optimizer resource-action-summary list -c <compartment ocid>``
    * ``oci optimizer history-summary list -c <compartment ocid>``

  * Support for new optional parameter resource metadata in resource actions

    * ``oci optimizer resource-action-summary list -c <compartment ocid> --include-resource-metadata``
    * ``oci optimizer resource-action get --resource-action-id <resource action ocid> --include-resource-metadata``
    * ``oci optimizer history-summary list -c <compartment ocid> --include-resource-metadata``

* Data Integration Service

  * Support for concurrency throttling on

    * ``oci data-integration workspace oci data-integration task create``

  * Support for incremental extract, updates to

    * ``oci data-integration workspace oci data-integration dataflow create`

* Goldengate Service

  * Support for routing method for GoldenGate connections

    * ``oci goldengate connection create--connection --routing-method``

  * Support for subnetId update of GoldenGate connections

    * ``oci goldengate connection update--connection --subnet-id``

3.37.0 - 2023-12-05
--------------------
Added
~~~~~

* Database service

  * Support for the serial console history.

    * ``oci db console-history``

  * Support for new optional parameters, autonomous-data-storage-size-in-tbs, cpu-core-count-per-node and total-container-databases in the cloud autonomous and autonomous vm cluster db resources.

    * ``oci db autonomous-vm-cluster update --autonomous-data-storage-size-in-tbs, --cpu-core-count-per-node, --total-container-databases``
    * ``oci db cloud-autonomous-vm-cluster update --autonomous-data-storage-size-in-tbs, --cpu-core-count-per-node, --total-container-databases``

  * Support for new list system versions commands.

    * ``oci db system-version list``

  *Support for new optional parameter in cloud-vm-cluster and vm-cluster resources.

    * ``oci db cloud-vm-cluster create --system-version``
    * ``oci db vm-cluster create --system-version``

* Support for multiple clusters in a SDDC in Oracle Cloud VMware Provisioning service.

  * ``oci ocvs esxi-host replace-host``
  * ``oci ocvs cluster cluster``
  * ``oci ocvs sddc retrieve-password``

* Support for upload-discovery-data in Log Analytics service.

  * ``oci log-analytics entity upload-discovery-data --upload-discovery-data-details --namespace-name``
  * ``oci log-analytics entity upload-discovery-data --file --namespace-name``

* ADM service.

  * Support for new list actions.

    * ``oci adm remediation-recipe list``
    * ``oci adm remediation-run list``
    * ``oci adm remediation-run list-application-dependency-recommendations``
    * ``oci adm remediation-run-stage list-stages``

  * Support for new optional parameters --usage-data.

    * ``oci adm vulnerability-audit create --usage-data``
    * ``oci adm vulnerability-audit create-vulnerability-audit-external-resource-vulnerability-audit-source --usage-data``
    * ``oci adm vulnerability-audit create-vulnerability-audit-oci-resource-vulnerability-audit-source --usage-data``
    * ``oci adm vulnerability-audit create-vulnerability-audit-unknown-source-vulnerability-audit-source --usage-data``

* Support for new AWR Hub Snapshot ingest commands in Operations Insights service.

  * ``oci opsi awr-hub-sources``
  * ``oci opsi operations-insights-warehouses``
  * ``oci opsi awr-hub-objects``

* Support for managing available certificates of target servers in Goldengate service.

  * ``oci goldengate certificate``


Changed
~~~~~~~

* [BREAKING] Multiple parameters changes in OCVS service. Few params deleted in sddc resource.

  * ``oci ocvs esxi-host create --cluster-id``
  * ``oci ocvs esxi-host list --cluster-id``
  * ``oci ocvs esxi-host update  --next-commitment``
  * ``oci ocvs sddc``

* Description of export details in the Logging Analytics service

  * ``oci log-analytics query export``

* Description change in Compute Cloud at Customer service

Removed
~~~~~

* [BREAKING] The following commands have been removed in ADM service.

  * ``oci adm application-dependency-recommendation-collection list-application-dependency-recommendations``
  * ``oci adm remediation-recipe-collection list-remediation-recipes``
  * ``oci adm remediation-run-collection list-remediation-runs``
  * ``oci adm remediation-run-stage-collection list-stages``

3.36.2 - 2023-11-14
--------------------
Added
~~~~~
* Support for new Oracle Database PostgreSQL service

  * ``oci psql``

* Support for enabling, disabling, renewing, and viewing SSL/TLS in the BDS service

  * ``oci bds instance enable-certificate``
  * ``oci bds instance disable-certificate``
  * ``oci bds instance renew-certificate``
  * ``oci bds instance certificate-service-info``

* Identity Domains Service

  * Support for new command

    * ``oci identity-domains approval-workflow``
    * ``oci identity-domains approval-workflow-assignment``
    * ``oci identity-domains approval-workflow-step``
    * ``oci identity-domains branding-setting``
    * ``oci identity-domains cloud-gate``
    * ``oci identity-domains cloud-gate-mapping``
    * ``oci identity-domains cloud-gate-server``
    * ``oci identity-domains cloud-gates``
    * ``oci identity-domains condition``
    * ``oci identity-domains my-completed-approval``
    * ``oci identity-domains my-pending-approval``
    * ``oci identity-domains my-pending-approvals list``
    * ``oci identity-domains my-request``
    * ``oci identity-domains network-perimeter``
    * ``oci identity-domains notification-setting``
    * ``oci identity-domains notification-settings``
    * ``oci identity-domains o-auth-client-certificate``
    * ``oci identity-domains o-auth-partner-certificate``
    * ``oci identity-domains policies``
    * ``oci identity-domains rule``
    * ``oci identity-domains rules``
    * ``oci identity-domains schema``
    * ``oci identity-domains schemas``
    * ``oci identity-domains self-registration-profile``
    * ``oci identity-domains self-registration-profiles``
    * ``oci identity-domains setting``
    * ``oci identity-domains settings``
    
  * Support for new optional parameter

    * ``oci identity-domains authentication-factors-remover create --token
    * ``oci identity-domains my-authentication-factors-remover create --token``
    * ``oci identity-domains my-request create --action --approval-details --expires``

* Support for Capacity Topology API in the Compute service

  * ``oci compute capacity-topology``

3.36.1 - 2023-11-07
--------------------
Added
~~~~~
* Java Management Service

  * Support for distribution and management of Deployment Rule Set

    * ``oci jms drs-file-collection list-drs-files``
    * ``oci jms fleet create-drs-file``
    * ``oci jms fleet update-drs-file``
    * ``oci jms fleet enable-drs``
    * ``oci jms fleet disable-drs``

  * Support for exporting data across regions

    * ``oci jms export-setting``
    * ``oci jms export-status``

  * Support for new optional parameter

    * ``oci jms fleet-agent-configuration update --mac-os-configuration``
    * ``oci jms java-family list --is-supported-version``
    * ``oci jms work-request list --managed-instance-id``

* Database Service

  * Support for SaaS administrative user configuration

    * ``oci db autonomous-database configure-saas-admin-user``
    * ``oci db autonomous-database saas-admin-user-status``

  * Support for Create Autonomous Dataguard Association

    * ``oci db autonomous-container-database-dataguard create``

3.36.0 - 2023-10-31
--------------------
Added
~~~~~
* Full Stack Disaster Recovery Service

  * Support for performing disaster recovery drills

    * ``oci disaster-recovery dr-plan-execution create-start-drill``
    * ``oci disaster-recovery dr-plan-execution create-start-drill-precheck``
    * ``oci disaster-recovery dr-plan-execution create-stop-drill``
    * ``oci disaster-recovery dr-plan-execution create-stop-drill-precheck``

  * Support for new optional parameter

    * ``oci disaster-recovery dr-protection-group list --lifecycle-sub-state``

* Stack Monitoring Service

  * Support for new commands on extensibility, metric extensions, and baseline and anomaly detection

    * ``oci stack-monitoring config create-license-auto-assign-config``
    * ``oci stack-monitoring config create-license-enterprise-extensibility-config``
    * ``oci stack-monitoring config update-license-auto-assign-config``
    * ``oci stack-monitoring config update-license-enterprise-extensibility-config``
    * ``oci stack-monitoring resource manage-license``
    * ``oci stack-monitoring resource summarize-count``
    * ``oci stack-monitoring resource list``
    * ``oci stack-monitoring resource-task``
    * ``oci stack-monitoring resource-type``
    * ``oci stack-monitoring metric-extension``
    * ``oci stack-monitoring baselineable-metric``

  * Support for new optional parameter

    * ``oci stack-monitoring resource create --license``
    * ``oci stack-monitoring resource search --license``

* Support for new optional parameter on integration with the Database Management service in the MySQL HeatWave Database service

  * ``oci mysql db-system clone --database-management``
  * ``oci mysql db-system create --database-management``
  * ``oci mysql db-system import --database-management``
  * ``oci mysql db-system list --database-management``
  * ``oci mysql db-system update --database-management``

* Support for new commands on integration with the MySQL HeatWave Database service in the Database Management service

  * ``oci database-management managed-my-sql-databases``

* Data Safe Service

  * Support for new commands on database security configuration, security policy, and analytics for SQL collection, firewall policies, and firewall violations

    * ``oci data-safe database-security-config``
    * ``oci data-safe security-policy``
    * ``oci data-safe security-policy-deployment``
    * ``oci data-safe security-policy-entry-state``
    * ``oci data-safe sql-collection``
    * ``oci data-safe sql-collection-analytics``
    * ``oci data-safe sql-collection-log-insights``
    * ``oci data-safe sql-firewall-allowed-sql``
    * ``oci data-safe sql-firewall-allowed-sql-analytics``
    * ``oci data-safe sql-firewall-policy``
    * ``oci data-safe sql-firewall-policy-analytics``
    * ``oci data-safe sql-firewall-violation-summary``

  * Support for new optional parameters

    * ``oci data-safe work-request list --access-level --compartment-id-in-subtree``

Changed
~~~~~~~
* [BREAKING] Optional parameter --sdm-masking-policy-difference-id for the below command is now required in the Data Safe service

  * ``oci data-safe masking-policy apply-sdm-masking-policy-difference --sdm-masking-policy-difference-id``

* [BREAKING] Database Tool Service

  * Multiple commands renamed

    * ``oci dbtools connection add-lock``
    * ``oci dbtools connection remove-lock``
    * ``oci dbtools connection create-generic-jdbc``
    * ``oci dbtools connection create-postgresql``
    * ``oci dbtools connection update-generic-jdbc``
    * ``oci dbtools connection update-postgresql``
    * ``oci dbtools connection validate-postgresql``
    * ``oci dbtools private-endpoint add-lock``
    * ``oci dbtools private-endpoint remove-lock``

  * Required parameter --database-tools-connection-id renamed

    * ``oci dbtools connection add-lock --connection-id``
    * ``oci dbtools connection remove-lock --connection-id``
    * ``oci dbtools connection update-generic-jdbc --connection-id``
    * ``oci dbtools connection update-postgresql --connection-id``
    * ``oci dbtools connection validate-postgresql --connection-id``

  * Required parameter --user-password renamed

    * ``oci dbtools connection create-generic-jdbc --user-password-secret-id``
    * ``oci dbtools connection create-postgresql --user-password-secret-id``
    * ``oci dbtools connection update-generic-jdbc --user-password-secret-id``
    * ``oci dbtools connection update-postgresql --user-password-secret-id``

  * Required parameter --database-tools-private-endpoint-id renamed

    * ``oci dbtools private-endpoint add-lock --private-endpoint-id``
    * ``oci dbtools private-endpoint remove-lock --private-endpoint-id``

  * Optional parameter removed

    * ``oci dbtools connection update-mysql-database --user-password``

3.35.0 - 2023-10-24
--------------------
Added
~~~~~
* Support for new optional parameters in the list alarms status in the OCI Monitoring Service

  * ``oci monitoring alarm-status list-alarms-status --entity-id, --resource-id, --service-name, --status``

* Add support for creating/updating new connection types in the Goldengate service

  * ``oci goldengate connection create-amazon-kinesis-connection``
  * ``oci goldengate connection update-amazon-kinesis-connection``
  * ``oci goldengate connection create-amazon-redshift-connection``
  * ``oci goldengate connection update-amazon-redshift-connection``
  * ``oci goldengate connection create-elasticsearch-connection``
  * ``oci goldengate connection update-elasticsearch-connection``
  * ``oci goldengate connection create-generic-connection``
  * ``oci goldengate connection update-generic-connection``
  * ``oci goldengate connection create-google-big-query-connection``
  * ``oci goldengate connection update-google-big-query-connection``
  * ``oci goldengate connection create-google-cloud-storage-connection``
  * ``oci goldengate connection update-google-cloud-storage-connection``
  * ``oci goldengate connection create-redis-connection``
  * ``oci goldengate connection update-redis-connection``

* Support for managing replicas in the NoSQL service

  * ``oci nosql table create-replica``
  * ``oci nosql table update-replica``

* Application Dependency Management

  * Adds new commands for managing ADM Remediation resources

    * ``oci adm remediation-recipe``
    * ``oci adm remediation-run``
    * ``oci adm remediation-run-collection list-remediation-runs``
    * ``oci adm remediation-run-stage get-stage``
    * ``oci adm remediation-run-stage-collection list-stages``
    * ``oci adm application-dependency-recommendation-collection list-application-dependency-recommendations``

  * Fix bug where when creating a Vulnerability Audit, we now wait for the lifecycle state of the audit instead of its Work Request.

* Database Service

  * Support for new optional parameter in autonomous container database

    * ``oci db autonomous-container-database create --is-dst-file-update-enabled``
    * ``oci db autonomous-container-database update --is-dst-file-update-enabled``

  * Newly added api for creating maintenance run for ACD resources

    * ``oci db maintenance-run create``

* Database Tools

  * Support for the new Generic JDBC connection type

    * ``oci dbtools connection create-generic-jdbc``
    * ``oci dbtools connection update-generic-jdbc``

  * Support for the new Postgresql connection type

    * ``oci dbtools connection create-postgresql``
    * ``oci dbtools connection update-postgresql``

  * Support for connections without runtime support on existing connection types

    * ``oci dbtools connection create-oracle-database --runtime-support unsupported``
    * ``oci dbtools connection create-mysql-database --runtime-support unsupported``

  * Support for connection list filtering using the runtime-support property

    * ``oci dbtools connection list --runtime-support``

  * Support for proxy authentication on Oracle connections

    * ``oci dbtools connection create-oracle-database --proxy-client``
    * ``oci dbtools connection update-oracle-database --proxy-client``

  *  Support for resource locking

    * ``oci dbtools private-endpoint add-lock``
    * ``oci dbtools private-endpoint remove-lock``

Changed
~~~~~~~
* [BREAKING] New required parameters in the Database Tools Service

  * ``oci dbtools connection create-mysql-database --connection-string --user-name``
  * ``oci dbtools connection create-oracle-database --connection-string --user-name``

3.34.0 - 2023-10-17
--------------------
Added
~~~~~
* Support for the new Redis service

  * ``oci redis``

* Support for export Container and Kubernetes application listings in the Marketplace Service

  * ``oci marketplace-publisher``

* Support for achieving higher limits in the Network Firewall Service

  * ``oci network-firewall address-list``
  * ``oci network-firewall application``
  * ``oci network-firewall application-group``
  * ``oci network-firewall decryption-profile``
  * ``oci network-firewall decryption-rule``
  * ``oci network-firewall mapped-secret``
  * ``oci network-firewall network-firewall-policy``
  * ``oci network-firewall security-rule``
  * ``oci network-firewall service``
  * ``oci network-firewall service-list``
  * ``oci network-firewall url-list``

* Support for exporting access request reports in the Managed Access Service

  * ``oci oma lockbox export-access-requests``

* Support for Mount File System in Data Science Jobs and Notebooks in the Data Science Service

  * ``oci data-science job create --job-storage-mount-configuration-details-list``
  * ``oci data-science job update --job-storage-mount-configuration-details-list``
  * ``oci data-science notebook-session create --notebook-session-storage-mount-configuration-details-list``
  * ``oci data-science notebook-session update --notebook-session-storage-mount-configuration-details-list``

* Logging Management

  * Support for unified agent operational metrics for the service configuration option

    * ``oci logging agent-configuration``

  * Added new destination field in the option ``--service-configuration``

Changed
~~~~~~~
* [BREAKING] Optional parameter ``--auto-approval-state`` was removed in the Managed Access Service

  * ``oci oma lockbox update``

* [BREAKING] Optional parameter ``--service-stage`` was removed in the Logging Management Service

  * ``oci logging service list``

* [BREAKING] Optional parameters ``--application-lists, --decryption-profiles, --decryption-rules, --ip-address-lists, --mapped-secrets, --security-rules, --url-lists`` were removed in the Network Firewall Service

  * ``oci network-firewall network-firewall-policy create``

  * ``oci network-firewall network-firewall-policy update``

3.33.4 - 2023-10-10
--------------------
Added
~~~~~
* Database Service

  * Support for new command

    * ``oci db pluggable-database relocate-pdb``
    * ``oci db pluggable-database create-local-clone``
    * ``oci db pluggable-database create-remote-clone``
    * ``oci db pluggable-database convert-to-regular``
    * ``oci db pluggable-database refresh``
    
  * Support for new optional parameter

    * ``oci db database restore --pdb-name``
    * ``oci db pluggable-database create --create-pdb-backup --cdb-admin-password``

  * Support for displaying resource usage information on autonomous vm cluster

    * ``oci db autonomous-vm-cluster get-autonomous-vm-cluster-resource-usage --autonomous-vm-cluster-id``
    * ``oci db autonomous-vm-cluster list-autonomous-vm-cluster-acd-resource-usage --autonomous-vm-cluster-id``

* Marketplace Service

  * Support for export Container and Kubernetes app listings

    * ``oci marketplace listing export``

  * Support for work request status for export Container and Kubernetes app listings

    * ``oci marketplace work-request``

* Support for creating a Flow Log type Capture filter in Virtual Cloud Network service

  * ``oci network capture-filter create --flow-log-capture-filter-rules``
  * ``oci network capture-filter list --filter-type``
  * ``oci network capture-filter update --flow-log-capture-filter-rules``

3.33.3 - 2023-10-03
--------------------
Added
~~~~~
* Database Service

  * Support for resource-pool-shapes for autonomous databases

    * ``oci db autonomous-database resource-pool-shapes``

  * Support for Elastic Resource Pools for autonomous databases, adding two optional parameter

    * ``oci db autonomous-database create --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-adb-cross-region-data-guard-details --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-from-backup-id --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-from-backup-timestamp --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-from-clone --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database create-refreshable-clone --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database update --resource-pool-leader-id --resource-pool-summary``
    * ``oci db autonomous-database list --is-resource-pool-leader --resource-pool-leader-id``

* Support for Private Endpoints in Data Science Service

  * ``oci data-science ds-private-endpoint``

* Support for File System Service (FSS) as transfer medium for Datapump export/import in the Database Migration Service (DMS)

  * Support for new optional parameter

    * ``oci database-migration migration create --data-transfer-medium-details``
    * ``oci database-migration migration update --data-transfer-medium-details``
    * ``oci database-migration migration create --dump-transfer-details``
    * ``oci database-migration migration update --dump-transfer-details``
    * ``oci database-migration migration create --data-transfer-medium-details-v2``
    * ``oci database-migration migration update --data-transfer-medium-details-v2``

* Support for new optional parameters for Replica in the MySQL Heatwave Service

  * ``oci mysql replica create --replica-overrides``
  * ``oci mysql replica update --replica-overrides``
  * ``oci mysql replica list --configuration-id --is-up-to-date``

3.33.2 - 2023-09-26
--------------------
Added
~~~~~
* Support for Private Endpoints for External Key Manager in Key Management Service

  * ``oci kms ekm ekms-private-endpoint create --ca-bundle, --compartment-id , --display-name, --external-key-manager-ip, --subnet-id, --defined-tags, --freeform-tags, --port``
  * ``oci kms ekm ekms-private-endpoint get --ekms-private-endpoint-id``
  * ``oci kms ekm ekms-private-endpoint list --compartment-id``
  * ``oci kms ekm ekms-private-endpoint delete --ekms-private-endpoint-id``
  * ``oci kms ekm ekms-private-endpoint update --ekms-private-endpoint-id, --defined-tags, --display-name, --freeform-tags``

* Support for new optional parameters in Vaults and Keys for External Key Manager in Key Management Service

  * ``oci kms management vault create --vault-type, --external-key-manager-metadata``
  * ``oci kms management key create --external-key-reference, --protection-mode``
  * ``oci kms management key-version create --external-key-version-id``

* Support for FAaas Self Service with Henosis for Oracle Integration Cloud

  * ``oci integration integration-instance create --domain-id``

3.33.1 - 2023-09-12
--------------------
Added
~~~~~
* Support for --is-dedicated optional param for listCharactersSets api in the Database service

  * ``oci db autonomous-database-character-sets list --is-dedicated``

* Support for face detection feature in Vision Service ("featureType":"FACE_DETECTION")

  * ``oci ai-vision image-job create --features``

* Stack Monitoring

    * New api for stack-monitoring config

      * ``oci stack-monitoring config change-compartment``
      * ``oci stack-monitoring config create``
      * ``oci stack-monitoring config create-auto-promote-config``
      * ``oci stack-monitoring config delete``
      * ``oci stack-monitoring config get``
      * ``oci stack-monitoring config update``
      * ``oci stack-monitoring config update-auto-promote-config``
      * ``oci stack-monitoring config list``

* Support for Announcement Chaining in Announcements Service, adding two new optional parameters

    * ``oci announce announcements list --chain-id --should-show-only-latest-in-chain``

* Database Management Service

    * Support for SQL tuning set

      * ``oci database-management perfhub managed-database modify-snapshot-settings``

  * Existing parameter connection-info is now an optional parameter

    * ``oci database-management external-db-system-connector update-macs-connector --connection-info``

3.33.0 - 2023-09-05
--------------------
Added
~~~~~
* Support for filtering and sorting work requests in the Container Instances service

  * ``oci container-instances work-request list --availability-domain --sort-by --sort-order --status``
  * ``oci container-instances work-request list-errors --sort-by --sort-order``
  * ``oci container-instances work-request list-logs --sort-by --sort-order``

* Queue Service

  * Support for queue channels

    * ``oci queue channels list-channels``

  * Support for new optional parameters

    * ``oci queue messages get-messages --channel-filter``
    * ``oci queue messages get-stats --channel-id``
    * ``oci queue queue-admin queue create --channel-consumption-limit``
    * ``oci queue queue-admin queue purge --channel-ids``
    * ``oci queue queue-admin queue update --channel-consumption-limit``

* Data Catalog Service

  * Support for new entity lineage retrieval and asynchronous glossary export commands in the Data Catalog service

    * ``oci data-catalog entity fetch-entity-lineage``
    * ``oci data-catalog glossary asynchronous-export``

  * Support for new optional parameters on folders and jobs in the Data Catalog service

    * ``oci data-catalog folder list --type-key``
    * ``oci data-catalog job list --glossary-key``
    * ``oci data-catalog job-definition create --glossary-key``
    * ``oci data-catalog job-definition list --glossary-key``
    * ``oci data-catalog job-definition update --glossary-key``

Changed
~~~~~~~
* [BREAKING] Customer Incident Management Service

  * Endoint changed from https://incidentmanagement.{region}.{domainAndTopLevelDomain} to https://incidentmanagement.{region}.oci.{domainAndTopLevelDomain} (e.g. https://incidentmanagement.us-phoenix-1.oraclecloud.com to https://incidentmanagement.us-phoenix-1.oci.oraclecloud.com)

  * Incident commands moved to parent group

    * ``oci support incident create``
    * ``oci support incident get``
    * ``oci support incident list``
    * ``oci support incident update``
    * ``oci support incident-resource-type list``
    * ``oci support validation-response validate-user``

  * Command removed

    * ``oci support user user create``

3.32.0 - 2023-08-29
--------------------
Added
~~~~~
* Database Service

  * Support for displaying resource usage information on autonomous container database get operations

    * ``oci db autonomous-container-database get-autonomous-container-database-resource-usage --autonomous-container-database-id``

  * Support for displaying resource usage information on cloud autonomous vm cluster get operations

    * ``oci db cloud-autonomous-vm-cluster get-cloud-autonomous-vm-cluster-resource-usage --cloud-autonomous-vm-cluster-id``

  * Support for displaying resource usage information for list of autonomous container databases on cloud autonomous vm cluster get operations

    * ``oci db cloud-autonomous-vm-cluster list-cloud-autonomous-vm-cluster-acd-resource-usage --cloud-autonomous-vm-cluster-id``

* APM Synthetic Monitoring Service

  * Support for the network monitor creation and updation

    * ``oci apm-synthetics monitor create-network-monitor``
    * ``oci apm-synthetics monitor update-network-monitor``

* Database Migration Service

  * Support for new parameters for GoldenGate Service integration in DMS

    * ``oci database-migration connection create --replication-credentials``
    * ``oci database-migration connection update --replication-credentials``

  * Support for new parameters for GoldenGate service integration in DMS

    * ``oci database-migration migration create --golden-gate-service-details``
    * ``oci database-migration migration update --golden-gate-service-details``

* Networking Services

  * Support for new parameters is-private, is-transport-mode

    * ``oci network cpe create --is-private``
    * ``oci network virtual-circuit create --is-transport-mode``
    * ``oci network virtual-circuit update --is-transport-mode``

  * Support for virtual circuit associated tunnels

    * ``oci network virtual-circuit-associated-tunnel-details list-virtual-circuit-associated-tunnels --virtual-circuit-id``

  * Support for new parameters transportAttachmentId, transportOnlyMode in the Dynamic Routing Gateway

    * ``oci network drg-attachment create-drg-attachment-loop-back-drg-attachment-network-create-details --network-details-ids``
    * ``oci network drg-attachment create-vcn-drg-attachment-loop-back-drg-attachment-network-create-details --network-details-ids``
    * ``oci network drg-attachment update-drg-attachment-loopback-drg-attachment-network-update-details --network-details-ids``
    * ``oci network drg-attachment update-vcn-drg-attachment-loopback-drg-attachment-network-update-details --network-details-ids``

  * Support for Encrypted Fastconnect

* Compute Service

  * Support for assigning an IPv6 address to a compute instance during instance launch or secondary VNIC attach
    * ``oci compute instance launch --assign-ipv6-ip true``


Changed
~~~~~~~
* [BREAKING] Removal of Analytics Cluster in MySQL Database Service

  * ``oci mysql db-system analytics-cluster``
  * ``oci mysql db-system analytics-cluster-memory-estimate``

* [BREAKING] New required parameter in Networking Services

  * ``oci network virtual-circuit update --virtual-circuit-id``

3.31.1 - 2023-08-22
--------------------
Added
~~~~~
* Support for Warehouse data objects in the Operations Insights service

  * ``oci opsi opsi-warehouse-data-objects list``
  * ``oci opsi opsi-warehouse-data-objects query-warehouse-data-standard-query``
  * ``oci opsi opsi-warehouse-data-objects query-warehouse-data-templatized-query``

* Support standard queries for Operations Insights data objects in the Operations Insights service

  * ``oci opsi opsi-data-objects query-data-standard-query``

* Support for new parameter in the Operations Insights service

  * ``oci opsi opsi-data-objects list --group-name --name``
  * ``oci opsi opsi-data-objects query-data-templatized-query --data-objects --query-bind-params --query-from-clause --query-query-execution-timeout-in-seconds``

* Support for the Compute Cloud at Customer service

  * ``oci ccc``

* Support for Database In-Memory for autonomous databases in the Database service

  * ``oci db autonomous-database create --in-memory-percentage``
  * ``oci db autonomous-database create-adb-cross-region-data-guard-details --in-memory-percentage``
  * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details --in-memory-percentage``
  * ``oci db autonomous-database create-from-backup-id --in-memory-percentage``
  * ``oci db autonomous-database create-from-backup-timestamp --in-memory-percentage``
  * ``oci db autonomous-database create-from-clone --in-memory-percentage``
  * ``oci db autonomous-database create-refreshable-clone --in-memory-percentage``
  * ``oci db autonomous-database update --in-memory-percentage``

3.31.0 - 2023-08-15
--------------------
Added
~~~~~
* Support for new data sync commands in the Rover service

  * ``oci rover device data-sync``

* Support for new parameters including Single Sign-On support in the Golden Gate service

  * ``oci goldengate deployment create --credential-store --identity-domain-id --password-secret-id``
  * ``oci goldengate deployment create --credential-store --identity-domain-id --password-secret-id``

* Support for the placement constraint and cluster configuration feature for the Cluster networks in the Compute Management service

  * ``oci compute-management cluster-network create --cluster-configuration``

Changed
~~~~~~~
* Required parameters is now optional for below diagnostics bundle commands in the Rover service

  * ``oci rover device diagnostics bundle create --display-name``
  * ``oci rover device diagnostics bundle get --encryption-key-file``

* [BREAKING] Renamed commands for below external-db-system-connector commands in the Database Management service

  * ``oci database-management external-db-system-connector check-connection-status``
  * ``oci database-management external-db-system-connector create-macs-connector``
  * ``oci database-management external-db-system-connector update-macs-connector``

3.30.2 - 2023-08-08
--------------------
Added
~~~~~
* Database Service

  * Support for adding backup retention in days for create operations

    * ``oci db autonomous-database create --backup-retention-period-in-days``
    * ``oci db autonomous-database create-adb-cross-region-data-guard-details --backup-retention-period-in-days``
    * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details --backup-retention-period-in-days``
    * ``oci db autonomous-database create-from-backup-id --backup-retention-period-in-days``
    * ``oci db autonomous-database create-from-backup-timestamp --backup-retention-period-in-days``
    * ``oci db autonomous-database create-from-clone --backup-retention-period-in-days``
    * ``oci db autonomous-database create-refreshable-clone --backup-retention-period-in-days``
    * ``oci db autonomous-database create-virtual-clone --backup-retention-period-in-days``
    * ``oci db autonomous-database update --backup-retention-period-in-days, --compute-model``

  * Support for adding and updating localAdgAutoFailoverMaxDataLossLimit for local autonomous data guard

    * ``oci db autonomous-database update --local-adg-auto-failover-max-data-loss-limit``

* Identity Domains Service

  * Support for new commands

    * ``oci identity-domains app``
    * ``oci identity-domains app-role``
    * ``oci identity-domains app-status-changer``
    * ``oci identity-domains apps search``

* Goldengate Service

  * Support for new operations for deployment upgrade entity

    * ``oci goldengate deployment-upgrade cancel``
    * ``oci goldengate deployment-upgrade reschedule``

* The AI Language service

  * Support to get information on model type and other details of models

  * ``oci ai language model-type-info get``

* Operator Access Control service

  * Support for Compute Cloud at Customer (C3) resource type

    * ``oci opctl operator-control-assignment create``

3.30.1 - 2023-08-01
--------------------
Added
~~~~~
* Loganalytics

  * Support for Log Source Validations

    * ``oci log-analytics source validate-loglist-endpoint``
    * ``oci log-analytics source validate-log-endpoint``
    * ``oci log-analytics source validate-label-condition``

  * Support for listing properties

    * ``oci log-analytics property list-effective-properties``
    * ``oci log-analytics property list-properties-metadata``

  * Support for getting recalls statistics

    * ``oci log-analytics storage get-recalled-data-size``
    * ``oci log-analytics storage get-recall-count``
    * ``oci log-analytics storage list-overlapping-recalls``

  * Support for getting rules summary

    * ``oci log-analytics rule get-rules-summary``

  * Support for new optional parameter

    * ``oci log-analytics source upsert-source --endpoints, --source-properties``
    * ``oci log-analytics source validate-source --endpoints, --source-properties``
    * ``oci log-analytics source validate-source-extfield-details --endpoints, --source-properties``
    * ``oci log-analytics storage recall-archived-data --is-recall-new-data-only, --purpose``
    * ``oci log-analytics storage estimate-recall-data-size --is-recall-new-data-only, --log-sets``
    * ``oci log-analytics em-bridge delete --is-delete-entities``

* Exadata Fleet Update Service

  * Support for the Exadata Fleet Update service

    * ``oci fleet-software-update``

* Container Engine For Kubernetes

  * Support for OKE cluster credential rotation feature

    * ``oci ce cluster start-credential-rotation``
    * ``oci ce cluster complete-credential-rotation``
    * ``oci ce credential-rotation-status get``

* Fusion Applications Environment Management

  * Support for new scheduled activity response properties

    * ``oci fusion-apps scheduled-activity list --scheduled-activity-association-id, --scheduled-activity-phase``

* Operations Insights

  * Support for OPSI news reports

    * ``oci opsi news-report list``
    * ``oci opsi news-reports change``
    * ``oci opsi news-reports delete``
    * ``oci opsi news-reports get``
    * ``oci opsi news-reports update``

3.30.0 - 2023-07-25
--------------------
Added
~~~~~
* Goldengate Service

  * Support for Automatic Backup Download

    * ``oci golden-gate deployment-backup copy --bucket-name --namespace-name``

* Budgets Service

  * Support for creating single use (non-recurring) budgets

    * ``oci budgets budget create``
    * ``oci budgets budget update``

* AI Document Service

  * Support for composing two or more Document Service custom key value models into one single model.

    * ``oci ai-document model create``

* Core Service

  * Support for Custom hostname

    * ``oci compute-management instance-pool create``
    * ``oci compute-management instance-pool update``

Changed
~~~~~~~
* [BREAKING] Subscriptions and AssignedSubscription resources are now polymorphic in Organizations service

    * ``oci organizations subscription list --entity-version``
    * ``oci organizations assigned-subscription list --entity-version``

3.29.4 - 2023-07-18
--------------------
Added
~~~~~

* Support for no-browser authentication

  * oci session authenticate --no-browser

* Big Data service

  * Support for new commands

    * ``oci bds instance get-os-patch-details``
    * ``oci bds instance install-os-patch``
    * ``oci bds instance list-os-patches``
    * ``oci bds instance master-nodes add``
    * ``oci bds instance utility-nodes add``

  * Support for new optional parameter

    * ``oci bds instance list-patch-histories --patch-type``

* File Storage service

  * Support for new commands

    * ``oci fs mount-target validate-key-tabs``
    * ``oci fs outbound-connector``

  * Support for new optional parameters for Kerberos and LDAP with NFSv3

    * ``oci fs export create --is-idmap-groups-for-sys-auth``
    * ``oci fs export update --is-idmap-groups-for-sys-auth``
    * ``oci fs mount-target create --idmap-type --kerberos --ldap-idmap``
    * ``oci fs mount-target update --idmap-type --kerberos --ldap-idmap``

* Support for new optional parameter in the Disaster Recovery service

  * ``oci disaster-recovery dr-protection-group list --role``

* Support for test connectivity for connections associated with deployments in the Goldengate service

  * ``oci goldengate connection-assignment test``

3.29.3 - 2023-07-11
--------------------
Added
~~~~~

* Support for optional parameters in the Application Performance Monitoring Synthetic service

  * ``oci apm-synthetics monitor create-browser-monitor --is-default-snapshot-enabled --verify-response-codes``
  * ``oci apm-synthetics monitor create-rest-monitor --client-certificate-details``
  * ``oci apm-synthetics monitor create-scripted-browser-monitor --is-default-snapshot-enabled``
  * ``oci apm-synthetics monitor create-scripted-rest-monitor --req-authentication-scheme --verify-response-codes``
  * ``oci apm-synthetics monitor update-browser-monitor --is-default-snapshot-enabled --verify-response-codes``
  * ``oci apm-synthetics monitor update-rest-monitor ---client-certificate-details``
  * ``oci apm-synthetics monitor update-scripted-browser-monitor ---is-default-snapshot-enabled``
  * ``oci apm-synthetics monitor update-scripted-rest-monitor --req-authentication-scheme --verify-response-codes``

* Support for new commands in the OSP Gateway service

  * ``oci osp-gateway address-rule-service address-rule get``
  * ``oci osp-gateway address-service address``

* AI Document Service

  * Support for new commands

    * ``oci ai-document analyze-document-result``
    * ``oci ai-document model patch``

  * Support for new optional parameters

    * ``oci ai-document model create --alias-name --component-models``

* Support for workload mapping processing in the Container Engine service

  * ``oci ce workload-mapping``
  * ``oci ce workload-mapping-summary``

* Support for new commands in the Data Integration service

  * ``oci data-integration composite-state get``
  * ``oci data-integration export-request``
  * ``oci data-integration export-request-summary-collection list-export-requests``
  * ``oci data-integration import-request``
  * ``oci data-integration import-request-summary-collection list-import-requests``
  * ``oci data-integration data-entity create-entity-shape-create-entity-shape-from-object``
  * ``oci data-integration workspace delete-export-request``
  * ``oci data-integration workspace delete-import-request``
  * ``oci data-integration workspace update-export-request``
  * ``oci data-integration workspace update-import-request``

* Support for new optional parameter --kms-key-id in updating and creating backup and volume backup's envelope key in Core services

  * ``oci bv backup create --kms-key-id``
  * ``oci bv backup update --kms-key-id``
  * ``oci bv boot-volume-backup create --kms-key-id``
  * ``oci bv boot-volume-backup update --kms-key-id``

3.29.2 - 2023-06-27
--------------------
Added
~~~~~

* Support for the OS Management Hub service

  * ``oci os-management-hub``
  
* Support for ECPU integration in the License Manager service

  * ``oci license-manager product-license list-top-utilized-resources --resource-unit-type ECPU``

* Support for SqlEndpoints in the Data Flow service

  * ``oci data-flow sql-endpoint``

* Support for freeform and defined tags in the Artifacts service

  * ``oci artifacts container repository create --freeform-tags --defined-tags``
  * ``oci artifacts container repository update --freeform-tags --defined-tags``
  * ``oci artifacts container image update --freeform-tags --defined-tags``
  * ``oci artifacts container image-signature create --freeform-tags --defined-tags``
  * ``oci artifacts container image-signature update --freeform-tags --defined-tags``

* Support for OS Management Hub in the OS Management Hub service

* Mysql Database Service

  * Support for new optional parameters that allow to set up replication delay.

    * ``oci mysql channel create-from-mysql --target-delay-in-seconds``
    * ``oci mysql channel update-from-mysql --target-delay-in-seconds``

  * Support for new optional parameters that allow to set up how to handle replicated tables that do not have a Primary Key.

    * ``oci mysql channel create-from-mysql --target-tables-without-primary-key-handling``
    * ``oci mysql channel update-from-mysql --target-tables-without-primary-key-handling``

* Database Service

  * Support for the CDB key store type change

    * ``oci db database change-key-store-type``

  * Support for the PDB rotate key

    * ``oci db pluggable-database rotate-encryption-key --pluggable-database-id``

* Database Management Service

  * Support for SQL Plan Management(SPM)

    * ``oci database-management managed-database list-sql-plan-baselines``
    * ``oci database-management managed-database get-sql-plan-baseline``
    * ``oci database-management managed-database drop-sql-plan-baselines``
    * ``oci database-management managed-database enable-auto-plan-capture``
    * ``oci database-management managed-database disable-auto-plan-capture``
    * ``oci database-management managed-database cfg-auto-capture-filters``
    * ``oci database-management managed-database enable-spb-usage``
    * ``oci database-management managed-database disable-spb-usage``
    * ``oci database-management managed-database get-spb-configuration``
    * ``oci database-management managed-database summarize-sql-plan-baselines``
    * ``oci database-management managed-database summarize-sql-plan-baselines-by-last-execution``
    * ``oci database-management managed-database enable-auto-spm-evolve-task``
    * ``oci database-management managed-database disable-auto-spm-evolve-task``
    * ``oci database-management managed-database cfg-auto-spm-evolve-task``
    * ``oci database-management managed-database enable-hf-auto-spm-evolve-task``
    * ``oci database-management managed-database disable-hf-auto-spm-evolve-task``
    * ``oci database-management managed-database load-spb-from-cc``
    * ``oci database-management managed-database load-spb-from-awr``
    * ``oci database-management managed-database change-plan-retention``
    * ``oci database-management managed-database change-space-budget``
    * ``oci database-management managed-database change-spb-attr``
    * ``oci database-management managed-database list-cursor-cache-statements``
    * ``oci database-management managed-database list-spb-jobs``

  * Support for Enable/disable of Stack Monitoring service for External DB System

    * ``oci database-management external-db-system enable-external-db-system-stack-monitoring``
    * ``oci database-management external-db-system disable-external-db-system-stack-monitoring``

  * Support for new optional paramater for External DB System

    * ``oci database-management external-db-system create --stack-monitoring-config``

  * Support for IN and OUT binds in SQL Jobs

    * ``oci database-management job create-sql-job --in-binds --out-binds``
    * ``oci database-management job update-sql-job-details --in-binds --out-binds``

3.29.1 - 2023-06-20
--------------------
Added
~~~~~

* Support for the Serial Console Access in the Database service

  * ``oci db console-connection create``
  * ``oci db console-connection delete``
  * ``oci db console-connection update``
  * ``oci db node update``

* Database Migration Service

  * Support for creating a new connection with Network Security Group (NSG) Id's

    * ``oci database-migration connection create --nsg-ids``

  * Support for updating a connection with new Network Security Group (NSG) Id's

    * ``oci database-migration connection update --nsg-ids``

* Support for new optional parameter in the Functions service

  * ``oci fn application create --shape``

* Data Flow service

  * Support for creating and managing Data Flow Pools

    * ``oci data-flow pool``

  * Support for additional optional parameters for using Data Flow pools

    * ``oci data-flow application create --pool-id``
    * ``oci data-flow application update --pool-id``
    * ``oci data-flow run create --pool-id``
    * ``oci data-flow run submit --pool-id``
    * ``oci data-flow run list --pool-id``

* Rover Node Service

  * Support for the following in the Roving Edge Infrastructure Service

    * ``oci rover node create --cert-compartment-id --cert-key-algorithm --cert-signature-algorithm --common-name --issuer-certificate-authority-id --time-cert-validity-end``
    * ``oci rover node update --cert-compartment-id --cert-key-algorithm --cert-signature-algorithm --certificate-authority-id --common-name --time-cert-validity-end``

  * Commands for rover upgrade bundle support

    * ``oci rover node rover-bundle copy-to-customer``
    * ``oci rover node rover-bundle get-status``
    * ``oci rover node rover-bundle-request list``
    * ``oci rover node rover-bundle-version get``

  * Commands for rover node certificate support

    * ``oci rover node ca-bundle get``
    * ``oci rover node certificate create``
    * ``oci rover node certificate update``
    * ``oci rover node certificate get-leaf-certificate``
    * ``oci rover node certificate-authority update-root-ca``

  * Commands for rover upgrade bundle support

    * ``oci rover standalone-cluster rover-bundle copy-to-customer``
    * ``oci rover standalone-cluster rover-bundle get-status``
    * ``oci rover standalone-cluster rover-bundle-request list``
    * ``oci rover standalone-cluster rover-bundle-version get``

3.29.0 - 2023-06-13
--------------------
Added
~~~~~
* Support for the OCI Control Center service

  * ``oci occ``

* Oracle Cloud Vmware Solution service

  * Support for allowing users to select the billing interval of deleted ESXi hosts while adding new ESXi hosts

    * ``oci ocvs esxi-host swap-billing --swap-billing-host-id``
    * ``oci ocvs esxi-host create --billing-donor-host-id``
    * ``oci ocvs esxi-host list --is-billing-donors-only``
    * ``oci ocvs esxi-host update --billing-donor-host-id``

  * Support swap-billing in ocvs

    * ``oci ocvs esxi-host swap-billing``

* Support for resource quota and limit in the Usage service

  * ``oci usage usagelimits usage-limit-summary``
  * ``oci usage resources resource-summary list-resources``
  * ``oci usage resources resource-quotum-summary list-resource-quota``

* Custom Key Value and Custom Document Classification Support in the AI Document service

  * ``oci ai-document model``
  * ``oci ai-document project``
  * ``oci ai-document work-request``
  * ``oci ai-document work-request-error``
  * ``oci ai-document work-request-log-entry list-work-request-logs``

* Support for the Domain Name System service in Object Storage service

  * ``oci os ns get --realm-specific-endpoint``

* Java Management service

  * Support for Java Migration Analysis

    * ``oci jms fleet request-java-migration-analyses``
    * ``oci jms java-migration-analysis-result``

  * Support for Performance Tuning Analysis

    * ``oci jms fleet request-performance-tuning-analyses``
    * ``oci jms performance-tuning-analysis-result ``

  * Support Fleet Diagnoses

    * ``oci jms fleet-diagnosis-summary list-fleet-diagnoses``

  * Support announcements

    * ``oci jms announcement-collection list-announcements``

  * Support Application Installation

    * ``oci jms application-installation-usage-summary summarize-application-installation-usage``
    * ``oci jms deployed-application-installation-usage-summary summarize-deployed-application-installation-usage``

  * Add optional --waiting-period-in-minutes option to JFR and crypto analysis

    * ``oci jms fleet request-crypto-analyses --waiting-period-in-minutes``
    * ``oci jms fleet request-jfr-recordings --waiting-period-in-minutes``

  * Support for new optional parameters --java-migration-analysis --performance-tuning-analysis

    * ``oci jms fleet-advanced-feature-configuration update --java-migration-analysis --performance-tuning-analysis``

* Support of TCPS protocol for Cloud Databases (Oracle Base Databases and Exadata on Dedicated Infrastructure) in Operations Insights service

  * ``oci opsi database-insights create-pe-comanged-database --connection-details``
  * ``oci opsi database-insights change-pe-comanaged-database-detail --connection-details``
  * ``oci opsi database-insights enable-pe-comanaged-database --connection-details``

Changed
~~~~~~~
* [BREAKING] Rename subgroup in usage service. New subgroup named 'rewards'

  * ``oci usage rewards redeemable-user``
  * ``oci usage rewards redemption-summary``
  * ``oci usage rewards redeemable-user-summary``
  * ``oci usage rewards product-summary``
  * ``oci usage rewards monthly-reward-summary``

3.28.2 - 2023-06-06
--------------------
Added
~~~~~
* Support for adding and removing Kafka in the Big Data service

  * ``oci bds kafka add``
  * ``oci bds kafka remove``

* Support for obtaining compute capacity report in Core services

  * ``oci compute compute-capacity-report``

* Support for enabling and disabling MySQL HeatWave Lakehouse in the Mysql Database service

  * ``oci mysql db-system heatwave-cluster add --is-lakehouse-enabled``
  * ``oci mysql db-system heatwave-cluster update --is-lakehouse-enabled``

* Support for adding, creating, and removing migration with csvText in the Database Migration service

  * ``oci database-migration migration add --csv-text``
  * ``oci database-migration migration create --csv-text``
  * ``oci database-migration migration remove --csv-text``

3.28.1 - 2023-05-30
--------------------
Added
~~~~~
* File Storage service

  * Support for new policy-based snapshots commands

    * ``oci fs filesystem-snapshot-policy``

  * Support for optional parameters to file-system and snapshot

    * ``oci fs file-system create --filesystem-snapshot-policy-id``
    * ``oci fs file-system list  --filesystem-snapshot-policy-id``
    * ``oci fs file-system update --filesystem-snapshot-policy-id``
    * ``oci fs snapshot create --expiration-time``
    * ``oci fs snapshot update --expiration-time``
    * ``oci fs snapshot list --compartment-id --filesystem-snapshot-policy-id``

* Support for creating and updating a VM Cluster network with DR network support in the Database service

  * ``oci db exadata-infrastructure-network create --dr-scan-details``
  * ``oci db exadata-infrastructure-network update --dr-scan-details``

* Support for optional parameter to indicate a dashboard is shared in the Management Dashboard services

  * ``oci management-dashboard dashboard create --features-config``
  * ``oci management-dashboard dashboard update --features-config``
  * ``oci management-dashboard saved-search create --features-config``
  * ``oci management-dashboard saved-search update --features-config``

Changed
~~~~~~~
* Required parameter --file-system-id is now optional for below command in the File Storage service

  * ``oci fs snapshot list --file-system-id``


3.28.0 - 2023-05-23
--------------------
Added
~~~~~
* Logging Management service

  * New optional parameter for CRI-O parser

    * ``oci logging service list --service-stage``

  * Added new CRI-O parser in the option ``--service-configuration``

  * [BREAKING] Commands removed

    * ``oci logging log-included-search get``
    * ``oci logging log-included-search list``

* Database Service

  * Added availability domain information in get VM cluster and Exadata Infrastructure.

    * ``oci db vm-cluster get --vm-cluster-id``
    * ``oci db exadata-infrastructure get --exadata-infrastructure-id``

  * Support for new optional parameter dbservers in the autonomous database dedicated service

    * ``oci db cloud-autonomous-vm-cluster create --dbservers``


* DNS service

  * Support for secondary egress zones API operations

    * ``oci dns zone create --compartment-id --name --zone-type --external-downstreams ``

  * Support to create zone from zone-file

    * ``oci dns zone create-zone-from-zone-file --compartment-id --create-zone-from-zone-file-details``

  * Support for new optional parameter external-downstream in zone-update

    * ``oci dns zone update --external-downstreams``

3.27.1 - 2023-05-16
--------------------
Added
~~~~~
* Support for Self Service Integration in the Fusion Application service
 
  * ``oci fusion-apps service-attachment create``
  * ``oci fusion-apps service-attachment delete``
  * ``oci fusion-apps service-attachment verify``

3.27.0 - 2023-05-09
--------------------
Added
~~~~~
* Support for the Access Governance cloud service

  * ``oci access-governance-cp``

* Database Service

  * Support for One-Off Patches resource to create, download database patches for customers that lost access to MOS.

    * ``oci db oneoff-patch create``
    * ``oci db oneoff-patch get``
    * ``oci db oneoff-patch list``
    * ``oci db oneoff-patch delete``
    * ``oci db oneoff-patch update``
    * ``oci db oneoff-patch download``

  * Support for changing Disaster Recovery configuration of a remote Autonomous Database in remote region of whether it's a snapshot standby

    * ``oci db autonomous-database change-disaster-recovery-configuration --is-snapshot-standby``

  * Support for Schedule automatic backup for exacs and dbcs

    * ``oci db database create --auto-backup-enabled --auto-backup-window --auto-full-backup-day --auto-full-backup-window --run-immediate-full-backup``
    * ``oci db database update --database-id --auto-backup-enabled --auto-backup-window --auto-full-backup-day --auto-full-backup-window --run-immediate-full-backup``
    * ``oci db system launch --auto-backup-enabled --auto-backup-window --auto-full-backup-day --auto-full-backup-window --run-immediate-full-backup``


* Support for provisioning Software Defined Data Center (SDDCs) using standard bare metal shapes with Block Storage as the datastore in the Oracle Cloud Vmware Solution

  * ``oci ocvs sddc create --datastores``

* Support for the Instance Configuration Parity feature in the Core Services

  * ``oci compute-management instance-configuration``

Changed
~~~~~~~
* [BREAKING] The Data Connectivity service is now removed

  * ``oci data-connectivity``

3.26.0 - 2023-05-02
--------------------

Added
~~~~~
* Support for new command in stack-monitoring in the Resource service

  * ``oci stack-monitoring resource update-and-propagate-tags``

* Support for on-demand node upgrade optional parameter for Kubernetes in the Container Engine service

  * ``oci ce node-pool create --node-pool-cycling-details``
  * ``oci ce node-pool update --node-pool-cycling-details``

* Data Science serivce

  * [BREAKING] Support for new BYOL SSL and ORDS certificates required parameters for Cloud Autonomous VM Clusters

    * ``oci db cloud-autonomous-vm-cluster rotate-cloud-autonomous-vm-cluster-ords-certs --certificate-generation-type``
    * ``oci db cloud-autonomous-vm-cluster rotate-cloud-autonomous-vm-cluster-ssl-certs --certificate-generation-type``

  * Support for new BYOL SSL and ORDS certificates optional parameters for Cloud Autonomous VM Clusters

    * ``oci db cloud-autonomous-vm-cluster rotate-cloud-autonomous-vm-cluster-ords-certs --ca-bundle-id --certificate-authority-id --certificate-id``
    * ``oci db cloud-autonomous-vm-cluster rotate-cloud-autonomous-vm-cluster-ssl-certs --ca-bundle-id --certificate-authority-id --certificate-id```

* Stack Monitoring service

  * Support for new optional parameter in creating discorvery job

    * ``oci stack-monitoring discovery-job create --should-propagate-tags-to-discovered-resources``

  * Support for new optional parameters to resources create and update commands

    * ``oci stack-monitoring resource create --additional-aliases --additional-credentials --defined-tags --freeform-tags``
    * ``oci stack-monitoring resource update --additional-aliases --additional-credentials --defined-tags --freeform-tags``

  * Support for new command in resources

    * ``oci stack-monitoring resource update-and-propagate-tagss``

3.25.4 - 2023-04-25
--------------------

Added
~~~~~
* Database Management service

  * Support for new commands to monitor external exadata infrastructure

    * ``oci database-management external-exadata-infrastructure change-compartment``
    * ``oci database-management external-exadata-infrastructure create``
    * ``oci database-management external-exadata-infrastructure delete``
    * ``oci database-management external-exadata-infrastructure disable-external-exadata-infrastructure-management``
    * ``oci database-management external-exadata-infrastructure discover``
    * ``oci database-management external-exadata-infrastructure enable-external-exadata-infrastructure-management``
    * ``oci database-management external-exadata-infrastructure get``
    * ``oci database-management external-exadata-infrastructure list``
    * ``oci database-management external-exadata-infrastructure update``
    * ``oci database-management external-exadata-storage-connector check``
    * ``oci database-management external-exadata-storage-connector create``
    * ``oci database-management external-exadata-storage-connector delete``
    * ``oci database-management external-exadata-storage-connector get``
    * ``oci database-management external-exadata-storage-connector list``
    * ``oci database-management external-exadata-storage-connector update``
    * ``oci database-management external-exadata-storage-grid get``
    * ``oci database-management external-exadata-storage-server get``
    * ``oci database-management external-exadata-storage-server get-iorm-plan``
    * ``oci database-management external-exadata-storage-server get-open-alert-history``
    * ``oci database-management external-exadata-storage-server get-top-sql-cpu-activity``
    * ``oci database-management external-exadata-storage-server list``

  * Support for new optional parameter --external-exadata-infrastructure-id

    * ``oci database-management managed-database list --external-exadata-infrastructure-id``

* Support for new optional parameters in the Database service

  * ``oci db cloud-autonomous-vm-cluster create --is-mtls-enabled-vm-cluster --scan-listener-port-non-tls --scan-listener-port-tls``
  * ``oci db exadata-infrastructure create --network-bonding-mode-details``
  * ``oci db exadata-infrastructure update --network-bonding-mode-details``

* Support for new commands in the Integration service

  * ``oci integration integration-instance change-private-endpoint-outbound-connection``
  * ``oci integration integration-instance change-private-endpoint-outbound-connection-none-outbound-connection``
  * ``oci integration integration-instance change-private-endpoint-outbound-connection-private-endpoint-outbound-connection``
  * ``oci integration integration-instance enable-process-automation``

* Organizations service

  * Support for new commands

    * ``oci organizations governance organization-tenancy add``
    * ``oci organizations governance organization-tenancy remove``

  * Support for new optional parameters

    * ``oci organizations child-tenancy create --governance-status``
    * ``oci organizations sender-invitation create --subjects``

3.25.3 - 2023-04-18
--------------------

Added
~~~~~
* Support for private endpoints in the Digital Assistant service

  * ``oci oda management oda-private-endpoint``
  * ``oci oda management oda-private-endpoint-attachment``
  * ``oci oda management oda-private-endpoint-scan-proxy``

* Support for cancel backup in Database Service

  * ``oci db backup cancel --backup-id``

* Support for param ``--record-metadata-job-id``  in Data Labeling service

  * ``oci data-labeling-service-dataplane record create-record-document-metadata --record-metadata-job-id``
  * ``oci data-labeling-service-dataplane record update-record-document-metadata --record-metadata-job-id``

3.25.2 - 2023-04-11
--------------------

Added
~~~~~
* Support for rotation of certificate of ORDS service on Autonomous VM Clusters on Exadata Cloud in the Database service.

  * ``oci db autonomous-vm-cluster rotate-autonomous-vm-cluster-ords-certs``
  * ``oci db autonomous-vm-cluster rotate-autonomous-vm-cluster-ssl-certs``

* Support for Application Virtual IP (VIP) features in the Database Service

  * ``oci db application-vip create``
  * ``oci db application-vip delete``
  * ``oci db application-vip get``
  * ``oci db application-vip list``

* Support for ADDM Spotlight for databases enabled in the Operations Insights service

  * ``oci opsi database-insights ingest-addm-reports``
  * ``oci opsi database-insights list-addm-db-finding-categories``
  * ``oci opsi database-insights list-addm-db-findings-time-series``
  * ``oci opsi database-insights list-addm-db-parameter-categories``
  * ``oci opsi database-insights list-addm-db-recommendation-categories``
  * ``oci opsi database-insights list-addm-db-recommendations-time-series``
  * ``oci opsi database-insights list-addm-dbs``
  * ``oci opsi database-insights summarize-addm-db-findings``
  * ``oci opsi database-insights summarize-addm-db-parameter-changes``
  * ``oci opsi database-insights summarize-addm-db-parameters``
  * ``oci opsi database-insights summarize-addm-db-recommendations``
  * ``oci opsi database-insights summarize-addm-db-schema-objects``
  * ``oci opsi database-insights summarize-addm-db-sql-statements``

* Data Safe service

  * Support for new command to list aggregated audit policy details on target databases

    * ``oci data-safe audit-policy-analytics list``

  * Support for new commands for data masking

    * ``oci data-safe difference-column get``
    * ``oci data-safe masking-object list``
    * ``oci data-safe masking-policy apply-sdm-masking-policy-difference``
    * ``oci data-safe masking-schema list``
    * ``oci data-safe sdm-masking-policy-difference``

  * Support for new commands for data discovery

    * ``oci data-safe sensitive-object list``
    * ``oci data-safe sensitive-schema list``

  * Support for new commands to list user profiles and analytics

    * ``oci data-safe user-assessment get-profile``
    * ``oci data-safe profile list-profile-analytics``
    * ``oci data-safe user-assessment list-profile-summaries``

  * Support for new optional parameters

    * ``oci data-safe masking-policy mask-data --is-drop-temp-tables-enabled --is-redo-logging-enabled --is-refresh-stats-enabled --parallel-degree --recompile``
    * ``oci data-safe security-assessment list-findings --references``
    * ``oci data-safe sensitive-column list --is-case-in-sensitive``


Changed
~~~~~~~
* Required parameter --display-name is now optional for below commands in the Data Safe service

  * ``oci data-safe private-endpoint update --display-name``
  * ``oci data-safe user-assessment list-users --user-profile --user-role --user-type``


3.25.1 - 2023-04-04
--------------------

Added
~~~~~
* Support for a new optional parameter to HTTP healthchecks for HTTPS backendsets in the Load Balancer service

  * ``oci lb health-checker update --is-force-plain-text``

3.25.0 - 2023-03-28
--------------------

Added
~~~~~
* Compute service

  * Support for new compute cluster commands

    * ``oci compute compute-cluster change-compartment``
    * ``oci compute compute-cluster create``
    * ``oci compute compute-cluster delete``
    * ``oci compute compute-cluster get``
    * ``oci compute compute-cluster list``
    * ``oci compute compute-cluster update``

  * Support for a new optional parameter --compute-cluster-id

    * ``oci compute instance launch --compute-cluster-id``
    * ``oci compute instance list --compute-cluster-id``

* Support for a new command to get connection diagnostics for registered databases in the Database Migration service

  * ``oci database-migration connection connection-diagnostics``

* Support for a new command to validate connection credentials in the DevOps service

  * ``oci devops connection validate``

* Support for a new optional parameter allowing ACD and OKV wallet naming in the Database service

  * ``oci db autonomous-container-database create --db-name``

Changed
~~~~~~~
* [BREAKING] Database service

  * The command db-system-compute-performance list has been renamed

    * ``oci db system list-db-system-compute-performances``

  * The command db-system-storage-performance list has been renamed

    * ``oci db system list-db-system-storage-performances``

3.24.0 - 2023-03-21
--------------------

Added
~~~~~
* Database Service

  * Support for changing Disaster Recovery configuration of a remote Autonomous Database in remote region of its Disaster Recovery Association

    * ``oci db autonomous-database change-disaster-recovery-configuration``

  * Support for creating a remote Disaster Recovery Association clone of an Autonomous Database

    * ``oci db autonomous-database create-autonomous-database-create-cross-region-disaster-recovery-details``

* Support for OCI DevOps Managed Build stage to use custom shape build runner in the DevOps service

  * ``oci devops build-pipeline-stage create-build-stage --build-runner-config``
  * ``oci devops build-pipeline-stage update-build-stage ---build-runner-config``

* Support for listing Pre-Built Functions and creating Functions from Pre-Built Functions in the Functions service

  * ``oci fn function create --source-details``
  * ``oci fn pbf-listing get``
  * ``oci fn pbf-listing list``
  * ``oci fn pbf-listing-version get``
  * ``oci fn pbf-listing-version list``
  * ``oci fn trigger list``

* Support for creating/updating new connection types in the Golden Gate service

  * ``oci goldengate connection create-amazon-s3-connection``
  * ``oci goldengate connection update-amazon-s3-connection``
  * ``oci goldengate connection create-hdfs-connection``
  * ``oci goldengate connection update-hdfs-connection``
  * ``oci goldengate connection create-microsoft-sqlserver-connection``
  * ``oci goldengate connection update-microsoft-sqlserver-connection``
  * ``oci goldengate connection create-jms-connection``
  * ``oci goldengate connection update-jms-connection``
  * ``oci goldengate connection create-mongo-db-connection``
  * ``oci goldengate connection update-mongo-db-connection``
  * ``oci goldengate connection create-oracle-nosql-connection``
  * ``oci goldengate connection update-oracle-nosql-connection``
  * ``oci goldengate connection create-snowflake-connection``
  * ``oci goldengate connection update-snowflake-connection``

Changed
~~~~~~~

* [BREAKING] The below commands have been changed as follow in the Golden Gate service

  * ``oci goldengate connection create-connection-create-azure-data-lake-storage-connection-details -> create-azure-data-lake-storage-connection``
  * ``oci goldengate connection update-connection-update-azure-data-lake-storage-connection-details -> update-azure-data-lake-storage-connection``
  * ``oci goldengate connection create-connection-create-azure-synapse-connection-details -> create-azure-synapse-connection``
  * ``oci goldengate connection update-connection-update-azure-synapse-connection-details -> update-azure-synapse-connection``
  * ``oci goldengate connection create-connection-create-kafka-schema-registry-connection-details -> create-kafka-schema-registry-connection``
  * ``oci goldengate connection update-connection-update-kafka-schema-registry-connection-details -> update-kafka-schema-registry-connection``
  * ``oci goldengate connection create-connection-create-postgresql-connection-details -> create-postgresql-connection``
  * ``oci goldengate connection update-connection-update-postgresql-connection-details -> update-postgresql-connection``

3.23.4 - 2023-03-14
--------------------
* Support for Identity Domains service

    * ``oci identity-domains``

* Database Service

  * Support for Long Term Backup for Autonomous Databases on Exadata Cloud at Customer

    * ``oci db autonomous-database-backup create --backup-destination-details``
    * ``oci db autonomous-database-backup list --type``

* Container Engine for Kubernetes service

  * Support for enhanced cluster

    * ``oci ce cluster create --type``
    * ``oci ce cluster update --type``

  * Support for Cluster AddOns

    * ``oci ce addon``

  * Support for Serverless

    * ``oci ce virtual-node-pool``

* Data integration service

  * Support for copy objects and template retrieval

    * ``oci data-integration workspace copy-object-request create``
    * ``oci data-integration workspace copy-object-request get``
    * ``oci data-integration workspace delete-copy-object-request``
    * ``oci data-integration workspace update-copy-object-request``
    * ``oci data-integration workspace copy-object-request-summary-collection list-copy-object-requests``
    * ``oci data-integration template get``
    * ``oci data-integration template list``

* Goldengate service

  * Support for managing available deployment version in the system

    * ``oci goldengate deployment-version``

  * Support for listing deployment versions

    * ``oci goldengate deployment-version list``

  * Support new commands for deployment upgrade entity

    * ``oci goldengate deployment-upgrade upgrade``
    * ``oci goldengate deployment-upgrade rollback``
    * ``oci goldengate deployment-upgrade snooze``
    * ``oci goldengate deployment-upgrade cancel-snooze``

  * Support for specifying oggVersion when upgrading a deployment

    * ``oci goldengate deployment upgrade-to``

  * Support for specifying maintenance-window and ogg version in case of create deployment

    * ``oci goldengate deployment create --maintenance-window-day --maintenance-window-start-hour --ogg-version``

  * Support for specifying maintenance-window in case of update deployment

    * ``oci goldengate deployment create --maintenance-window-day --maintenance-window-start-hour``

  * Support for specifying deployment type and ogg versions when listing deployment types

    * ``oci goldengate deployment-type-collection list-deployment-types --deployment-type --ogg-version``

* Operations Insights

  * Support in OPSI Host Capacity planning for Host network metrics

    * ``oci opsi host-insights summarize-network-usage-trend --compartment-id --id --analysis-time-interval``

  * Support in OPSI Host Capacity planning for Host storage metrics

    * ``oci opsi host-insights summarize-storage-usage-trend --compartment-id --id --analysis-time-interval``

Fixed
~~~~~

* Upgraded the cryptography version to (>=3.2.1,<40.0.0) and pyOpenSSL version to (>=17.5.0,<24.0.0') to fix CVE-2023-0286 and CVE-2023-23931

3.23.3 - 2023-03-07
--------------------
Added
~~~~~
* Database service

  * Support for autonomous database long-term backup schedule

    * ``oci db autonomous-database update --long-term-backup-schedule``
    * ``oci db autonomous-database update --long-term-backup-schedule``

  * Support for autonomous database long-term backup

    * ``oci db autonomous-database-backup create --retention-period-in-days --is-long-term-backup``
    * ``oci db autonomous-database-backup update``
    * ``oci db autonomous-database-backup delete``

* Support for Model Deployment resource to use a customized container image containing runtime dependencies of ML Model and custom web server to handle inference requests in the Data Science service

  * ``oci data-science model-deployment create``
  * ``oci data-science model-deployment update``
  * ``oci data-science model-deployment activate``
  * ``oci data-science model-deployment get``
  * ``oci data-science model-deployment list``

* Support for Disaster Recovery in the Oracle Content Management service

  * ``oci oce oce-instance create --dr-region``
  * ``oci oce oce-instance update --dr-region --lifecycle-details``

* Operations Insights service

  * Support for Full Features for Autonomous Databases

    * ``oci opsi database-insights enable-autonomous-database-insight-advanced-features``
    * ``oci opsi database-insights disable-autonomous-database-insight-advanced-features``
    * ``oci opsi database-insights change-autonomous-database-insight-advanced-features``

  * Support for new optional parameters

    * ``oci opsi database-insights summarize-database-insight-resource-capacity-trend --high-utilization-threshold --low-utilization-threshold``
    * ``oci opsi database-insights summarize-database-insight-resource-forecast-trend --high-utilization-threshold --low-utilization-threshold``
    * ``oci opsi database-insights summarize-database-insight-resource-statistics --high-utilization-threshold --low-utilization-threshold``
    * ``oci opsi database-insights summarize-database-insight-resource-usage --cdb-name``
    * ``oci opsi database-insights summarize-database-insight-resource-usage-trend --cdb-name``
    * ``oci opsi database-insights summarize-database-insight-resource-utilization-insight --cdb-name --high-utilization-threshold --low-utilization-threshold``
    * ``oci opsi database-insights summarize-sql-insights --vmcluster-name``

* Support for new optional flag in instance update API of Compute Service

  * ``oci compute instance update --update-operation-constraint``

* Support for new parameters in Management Agent's service

  * ``oci management-agent agent summarize-agent-counts --compartment-id-in-subtree``
  * ``oci management-agent agent summarize-plugin-counts --compartment-id-in-subtree``
  * ``oci management-agent agent list --gateway-id``

Changed
~~~~~~~
* Documentation change for Language codes supported as Text Translation now supports Hebrew and Greek as well and addition of support for auto-detection in AI Language text analyze with pretrained models

* Changed no passphrase indication for RSA keys from empty to "N/A"
  * ``oci setup config``
  * ``oci setup keys``

3.23.2 - 2023-02-28
--------------------
Added
~~~~~
* Support for new command allowing on-demand bootstrap script execution in the Big Data service

  * ``oci bds instance execute-bootstrap-script``

* Support for calling Oracle Cloud Infrastructure services in the eu-dcc-rating-1, eu-dcc-rating-2, eu-dcc-dublin-1, eu-dcc-dublin-2, and eu-dcc-milan-2 regions

3.23.1 - 2023-02-21
--------------------
Added
~~~~~
* Database Management service

  * Support for external Oracle database systems

    * ``oci database-management external-db-system-discovery``
    * ``oci database-management external-db-system``
    * ``oci database-management external-cluster``
    * ``oci database-management external-cluster-instance``
    * ``oci database-management external-asm``
    * ``oci database-management external-asm-instance``
    * ``oci database-management external-listener``
    * ``oci database-management external-db-node``
    * ``oci database-management external-db-home``
    * ``oci database-management external-db-system-connector``
    * ``oci database-management external-database-collection``

  * Support for summarize managed database availability metrics

    * ``oci database-management managed-database summarize-managed-database-availability-metrics``

* Anomaly Detection service

  * Support for detect-anomaly-job and detect-anomaly-job-collection

    * ``oci ai-anomaly-detection detect-anomaly-job create``
    * ``oci ai-anomaly-detection detect-anomaly-job delete``
    * ``oci ai-anomaly-detection detect-anomaly-job get``
    * ``oci ai-anomaly-detection detect-anomaly-job update``
    * ``oci ai-anomaly-detection detect-anomaly-job change-compartment``
    * ``oci ai-anomaly-detection detect-anomaly-job create-detect-anomaly-job-embedded-input-details``
    * ``oci ai-anomaly-detection detect-anomaly-job create-detect-anomaly-job-inline-input-details``
    * ``oci ai-anomaly-detection detect-anomaly-job create-detect-anomaly-job-object-list-input-details``
    * ``oci ai-anomaly-detection detect-anomaly-job-collection list-detect-anomaly-jobs``

  * Supprt for the new optional parameter --sensitivity in the below commands

    * ``oci anomaly-detection model detect-anomalies``
    * ``oci anomaly-detection model detect-anomalies-embedded``
    * ``oci anomaly-detection model detect-anomalies-inline``

3.23.0 - 2023-02-14
--------------------
Added
~~~~~
* Support for the Autonomous Recovery Service

  * ``oci recovery``

* Support for the Visual Builder Studio service

  * ``oci vbstudio``

* Added support for selecting DBServers while creating Autonomous VM Cluster in Database service

  * ``oci db autonomous-virtual-machine get --autonomous-virtual-machine-id``
  * ``oci db autonomous-virtual-machine list --autonomous-vm-cluster-id, --compartment-id``

Changed
~~~~~~~
* [BREAKING] Support for a new Capacity Availability API in the Compute service

  * ``oci compute computecapacityreport update``

* Modified existing commands in Database service

  * ``oci db autonomous-vm-cluster create --db-servers``

3.22.5 - 2023-02-07
--------------------
Added
~~~~~
* Support for Autonomous Container Database role in the Database service

  * Support for new command

    * ``oci db autonomous-container-database change-dataguard-role``
    * ``oci db autonomous-container-database-version list``

  * Support for new optional parameter

    * ``oci db autonomous-container-database create --fast-start-fail-over-lag-limit-in-seconds --version-preference --db-version``
    * ``oci db autonomous-container-database-dataguard update --fast-start-fail-over-lag-limit-in-seconds --protection-mode``
    * ``oci db autonomous-container-database update --version-preference``

* Devops Deploy service

  * Support for new optional parameters

    * ``oci devops deploy-stage create-oke-helm-chart-stage --cleanup-on-fail --debug-helm --force-helm --history-max --no-hooks --render-subchart-notes --reset-values --reuse-values --set-string --set-values --skip-crds --wait-helm``
    * ``oci devops deploy-stage update-oke-helm-chart-stage --cleanup-on-fail --debug-helm --force-helm --history-max --no-hooks --render-subchart-notes --reset-values --reuse-values --set-string --set-values --skip-crds --wait-helm``

  * Support for new optional helm-verification-key-source parameter

    * ``oci devops deploy-artifact --create-helm-repository-artifact --helm-verification-key-source``
    * ``oci devops deploy-artifact --update-helm-repository-artifact --helm-verification-key-source``

  * Support for new optional dry-run parameter

    * ``oci devops deployment create-pipeline-deployment --dry-run``
    * ``oci devops deployment create-single-stage-deployment --dry-run``

* Support for new Uploading MasterKey Wallets commands in the OCI GoldenGate Deployments service

  * ``oci goldengate deployment wallet-exists``
  * ``oci goldengate deployment export-wallet``
  * ``oci goldengate deployment import-wallet``
  * ``oci goldengate deployment-wallets list-wallet-operations``

* Support for new Custom configuration commands in the OPSI service

  * ``oci opsi opsi-configurations create-opsi-ux-configuration-details``
  * ``oci opsi opsi-configurations list``
  * ``oci opsi opsi-configurations get``
  * ``oci opsi opsi-configurations delete``
  * ``oci opsi opsi-configurations update-opsi-ux-configuration-details``
  * ``oci opsi opsi-configurations change``
  * ``oci opsi opsi-configurations summarize-configuration-items``


3.22.4 - 2023-01-31
--------------------
Added
~~~~~

* Support for new optional parameters for ExaCC, vault secret, and tool details in the Database service

  * ``oci db autonomous-database create --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database create-adb-cross-region-data-guard-details --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database create-from-backup-id --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database create-from-backup-timestamp --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database create-from-clone --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database create-refreshable-clone --compute-count --compute-model --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-database update --compute-count --secret-id --secret-version-number --db-tools-details``
  * ``oci db autonomous-vm-cluster create --compute-model``
  * ``oci db cloud-autonomous-vm-cluster create --compute-model``

* Support for new optional parameters enabling role-based access control in the Opensearch service

  * ``oci opensearch cluster create --security-mode --security-master-user-name --security-master-user-password-hash``
  * ``oci opensearch cluster update --security-mode --security-master-user-name --security-master-user-password-hash``

* Devops service

  * Support for new commands

    * ``oci devops deploy-stage create-shell-stage``
    * ``oci devops deploy-stage update-shell-stage``

  * Support for new artifact type COMMAND_SPEC for existing parameter ``--artifact-type``

    * ``oci devops deploy-artifact update --artifact-type command_spec``
    * ``oci devops deploy-artifact create-generic-artifact --artifact-type command_spec``
    * ``oci devops deploy-artifact create-inline-artifact --artifact-type command_spec``
    * ``oci devops deploy-artifact update-generic-artifact --artifact-type command_spec``
    * ``oci devops deploy-artifact update-inline-artifact --artifact-type command_spec``

Fixed
~~~~~

* Fixed reading from and writing to default config (~/.oci/config) when importing authentication session

  * ``oci session import``

3.22.3 - 2023-01-24
--------------------
Added
~~~~~

* Support for the Cloud Migrations service

  * ``oci cloud-migrations``

* Support for new optional parameter to set Custom Private IP during Private End Point provisioning in the Database service

  * ``oci db autonomous-database create --private-endpoint-ip``
  * ``oci db autonomous-database create-adb-cross-region-data-guard-details --private-endpoint-ip``
  * ``oci db autonomous-database create-from-backup-id --private-endpoint-ip``
  * ``oci db autonomous-database create-from-backup-timestamp --private-endpoint-ip``
  * ``oci db autonomous-database create-from-clone --private-endpoint-ip``
  * ``oci db autonomous-database create-refreshable-clone --private-endpoint-ip``
  * ``oci db autonomous-database update --private-endpoint-ip``

* Support for Machine Learning pipelines for the Data Science Service

  * ``oci data-science pipeline``
  * ``oci data-science pipeline-run``

* Support for the language PII (Personal Identifiable Information) detection in the AI Language service

  * ``oci ai language batch-detect-pii-entities``

* Support for cross region replication in the File Storage service

  * ``oci fs replication create``
  * ``oci fs replication get``
  * ``oci fs replication list``
  * ``oci fs replication delete``
  * ``oci fs replication change-compartment``
  * ``oci fs file-system estimate-replication``
  
3.22.2 - 2023-01-17
--------------------
Added
~~~~~

* Database service

    * Support for Private DNS in ExaCS systems during provisioning

      * ``oci db cloud-vm-cluster create --private-zone-id``

    * Support for Elastic Storage Expansion (Multi-Rack) feature

      * ``oci db exadata-infrastructure create --is-multi-rack-deployment, --multi-rack-configuration-file``
      * ``oci db exadata-infrastructure get --excluded-fields``
      * ``oci db exadata-infrastructure list --excluded-fields``
      * ``oci db exadata-infrastructure update --is-multi-rack-deployment, --multi-rack-configuration-file``

    * Support for target version fields of infra patching v2 features on cloud exadata infrastructure

      * ``oci db cloud-exa-infra get --storageserverversion``
      * ``oci db cloud-exa-infra get --dbserverversion``
      * ``oci db cloud-exa-infra get --monthlystorageserverversion``
      * ``oci db cloud-exa-infra get --monthlydbserverversion``

* Data Science Service

    * Support for creating model version sets in model catalog

      * ``oci data-science model-version-set *``

    * Support for option paramater ``model-version-set-id`` and  ``version-label`` for following commands

      * ``oci data-science model create --model-version-set-id, --version-label``
      * ``oci data-science model list --model-version-set-name, --version-label``
      * ``oci data-science model update --model-version-set-id, --version-label``

3.22.1 - 2023-01-10
--------------------
Added
~~~~~
* Support for the Queue service

 * ``oci queue``
 
* Support new pluggable-database commands for the Database service

 * ``oci db database move``
 * ``oci db pluggable-database disable-pluggable-database-management``
 * ``oci db pluggable-database enable-pluggable-database-management``
 * ``oci db pluggable-database modify-pluggable-database-management``
 
* Support optional parameters availability_configuration and maintenance_window_schedule on monitors creation and updation for the APM Synthetics service

 * ``oci apm-synthetics monitor create-browser-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor create-rest-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor create-scripted-browser-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor create-scripted-rest-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor update-browser-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor update-rest-monitor --availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor update-scripted-browser-monitor ---availability_configuration, --maintenance_window_schedule``
 * ``oci apm-synthetics monitor update-scripted-rest-monitor --availability_configuration, --maintenance_window_schedule``

* Support new Project commands & optional parameters for the DevOps service
 
 * ``oci devops work-request list --operation-type-multi-value-query``
 * ``oci devops project schedule-cascading-delete``
 * ``oci devops project cancel-cascading-delete``
  
* Support option paramter nsg-ids for the Database Migration service

 * ``oci database-migration connection create --nsg-ids``
 * ``oci database-migration connection update --nsg-ids``
  
* Support for new optional parameter in the Big Data Service (BDS)

 * ``oci bds instance create --cluster-profile``

* Service Mesh service

 * Support for new command in virtual-deployment

  * ``oci service-mesh virtual-deployment update-virtual-deployment-disabled-service-discovery-configuration``

 * Support for cancelling a work request for any work request that has been accepted but not yet started
 
  * ``oci service-mesh work-request cancel``
  
 * Support for new optional parameters in the list work requests to filter on associated resource id and operation status 
 
  * ``oci service-mesh work-request list --operation-status --resource-id``
  
 * Support for sorting in the list work requests, list work request errors, list work request logs
 
  * ``oci service-mesh work-request list --sort-by --sort-order``
  * ``oci service-mesh work-request list-work-request-errors --sort-by --sort-order``
  * ``oci service-mesh work-request list-work-request-logs --sort-by --sort-order``
  
* Fusion Application service
  
 * Support for Fusion Application self-service refresh scheduling
  
  * ``oci fusion-apps update-refresh-activity-details update-refresh-activity``
  * ``oci fusion-apps refresh-activity delete``
  
 * Support for new optional parameters in create-refresh-activity-details

  * ``oci fusion-apps create-refresh-activity-details create-refresh-activity --time-scheduled-start``
 
 * Support for new refresh activity lifecycle state NEEDS_ATTENTION in list

  * ``oci fusion-apps refresh-activity list --lifecycle-state needs_attention``
 
* Golden Gate service

 * Support for new commands

  * ``oci goldengate connection create-connection-create-azure-data-lake-storage-connection-details``
  * ``oci goldengate connection create-connection-create-azure-synapse-connection-details``
  * ``oci goldengate connection create-connection-create-kafka-schema-registry-connection-details``
  * ``oci goldengate connection create-connection-create-postgresql-connection-details``
  * ``oci goldengate connection update-connection-update-azure-data-lake-storage-connection-details``
  * ``oci goldengate connection update-connection-update-azure-synapse-connection-details``
  * ``oci goldengate connection update-connection-update-kafka-schema-registry-connection-details``
  * ``oci goldengate connection update-connection-update-postgresql-connection-details``

 * Support for new optional parameter

  * ``oci goldengate connection create-object-storage-connection --private-key-passphrase``
  * ``oci goldengate connection update-object-storage-connection --private-key-passphrase``

Changed
~~~~~~~
* [BREAKING] The command ingest-stream-distribution-channel-asset-metadata-entry-details has been renamed in Media service

 * ``oci media-services stream-distribution-channel ingest``

* [BREAKING] Optional parameters --rule are now required for access-policy create in Service Mesh service

 * ``oci service-mesh access-policy create --rule

* Required parameters --listeners and --service-discovery are now optional on virtual-deployment in Service Mesh service

 * ``oci service-mesh virtual-deployment create --listeners, --service-discovery``
 * ``oci service-mesh virtual-deployment create-virtual-deployment-dns-service-discovery-configuration --listeners``


3.21.0 - 2022-12-06
--------------------
Added
~~~~~

* Support for the Document Understanding service

 * ``oci ai-document``

* Support for Container Instances service

 * ``oci container-instances``

* Support for Collecting Diagnostics action in GoldenGate Deployment service

 * ``oci goldengate deployment collect-diagnostics``

* Support for enabling create stack from OCI DevOps Service or Bitbucket Cloud/Server as Source Control Management in Resource Manager service

 * ``oci resource-manager configuration-source-provider update-bitbucket-cloud-username-app-password-provider``
 * ``oci resource-manager configuration-source-provider update-bitbucket-server-access-token-provider``
 * ``oci resource-manager stack create-from-bitbucket-cloud``
 * ``oci resource-manager stack create-from-bitbucket-server``
 * ``oci resource-manager stack update-from-bitbucket-cloud``
 * ``oci resource-manager stack update-from-devops``
 * ``oci resource-manager configuration-source-provider create-bitbucket-cloud-username-app-password-provider``
 * ``oci resource-manager configuration-source-provider create-bitbucket-server-access-token-provider``
 * ``oci resource-manager stack code``



* Support for new optional parameters for Devops Deployments in Devops service

 * ``oci devops deployment create-pipeline-deployment --stage-override-arguments``
 * ``oci devops deployment create-single-stage-deployment --stage-override-arguments``

* Stack Monitoring service

    * Support for PeopleSoft Discovery in Stack Monitoring service

        * ``oci stack-monitoring discovery-job create --discovery-details``

    * Support for Apache Tomcat and SQLServer Discovery

        * ``oci stack-monitoring discovery-job create --discovery-detail``

* Mysql Database Service

    * Support for new required parameter "compartmentId" in BackupSummary response of API

        * ``oci mysql backup get --backup-id"``

    * Supports Managed Read Reaplicas - Load Balancing by adding a LOADBALANCER endpoint to DbSystem endpoints

        * ``oci mysql db-system get --db-system-id"``

    * Support for Mysql Database Service Managed Read Replicas

        * ``oci mysql replica *``

    * Support for new optional parameters that allow to set up replication filters

        * ``oci mysql channel create-from-mysql --target-filters``
        * ``oci mysql channel update-from-mysql --target-filters``

    * Support for new optional parameters that allow to set up replication from a source configured without global transaction identifiers

        * ``oci mysql channel create-from-mysql --source-anonymous-transactions-handling``
        * ``oci mysql channel update-from-mysql --source-anonymous-transactions-handling``

* Support for the Timezone and Language Preferences in Announce service

 * ``oci announce announcement-subscription create --preferred-language``
 * ``oci announce announcement-subscription update --preferred-language``
 * ``oci announce announcements-preferences create --preferred-time-zone``
 * ``oci announce announcements-preferences update --preferred-time-zone``

* Support for DataSafe Report Scheduling and Alerts Bulk API in data-safe service

 * ``oci data-safe masking-policy download-masking-log``
 * ``oci data-safe report-summary list-reports``
 * ``oci data-safe report-definition remove``
 * ``oci data-safe report-definition schedule-report``
 * ``oci data-safe report-definition schedule-report-schedule-audit-report-details``
 * ``oci data-safe target-alert-policy-association patch``

* Java Management Service

    * Support for Java Server Usage reporting

        * ``oci jms java-server-usage``
        * ``oci jms java-server-instance-usage summarize``
        * ``oci jms deployed-application-usage summarize``

    * Support for Java Library Usage reporting

        * ``oci jms library-usage *``

    * Support for Cryptographic Roadmap Impact Analysis

     * ``oci jms crypto-analysis-result *`
     * ``oci jms fleet request-crypto-analyses``

    * Support for Java Flight Recorder recordings and upload

     * ``oci jms fleet request-jfr-recordings``

    * Support for Restricting Management of Advanced Functionality

     * ``oci jms fleet-advanced-feature-configuration``

    * Support for new command

     * ``oci jms java-family list``

* Operations Insights

  * Support for ExaCS systems to Operations Insights

    * ``oci opsi exadata-insights create-pe-comanaged-exadata``
    * ``oci opsi exadata-insights enable-pe-comanaged-exadata``
    * ``oci opsi exadata-insights update-pe-comanaged-exadata``
    * ``oci opsi exadata-insights add-pe-comanaged-exadata-members``
    * ``oci opsi database-insights list-database-configurations``

  * Optional Parameter ``--vmcluster-name`` parameter added in ``oci opsi database-insights`` and ``oci opsi host-insights``

    * ``oci opsi database-insights summarize-database-insight*``

* Support for multiple choices for parameter of type click.Choice

Changed
~~~~~~~
* [BREAKING] ``--compartment-id`` is now a required parameter in ``oci data-safe alert patch``
* Reduced offline installation package size
* Remove deprecated command in the Java Management Service

 * ``oci jms java-family-collection list-java-families``


3.20.3 - 2022-11-22
--------------------
Fixed
~~~~~

* Upgraded the cryptography version to (>=3.2.1,<39.0.0) to fix the `OpenSSL Security bug <https://www.openssl.org/blog/blog/2022/11/01/email-address-overflows/>`_

3.20.2 - 2022-11-15
--------------------
Added
~~~~~

* Database service

  * Support for mTLS authentication with Listener and for providing custom value for TLS port and Non-TLS Port during AVM Cluster Creation on ExaCC
  
    * ``oci db autonomous-vm-cluster create --is-mtls-enabled --scan-listener-port-non-tls --scan-listener-port-tls``
  
  * Support for new optional parameters in CloudAutonomousVmClusters
  
    * ``oci db cloud-autonomous-vm-cluster create --autonomous-data-storage-size-in-tbs --cpu-core-count-per-node --db-servers --maintenance-window-details --memory-per-oracle-compute-unit-in-gbs --total-container-databases``
    * ``oci db cloud-autonomous-vm-cluster update --maintenance-window-details``
    
  * Support for new command in CloudExadataInfrastructure
   
    * ``oci db cloud-exadata-infrastructure-unallocated-resources get``
  
* Support to list resources and outputs associated with resource manager job and stack for the Resource Management service

  * ``oci resource-manager associated-resource-summary list-job-associated-resources``
  * ``oci resource-manager associated-resource-summary list-stack-associated-resources``
  * ``oci resource-manager job-output-summary list-job-outputs``

Changed
~~~~~~~

* Improved handling SSL error messages in CLI to enable customers self help

3.20.1 - 2022-11-08
--------------------

Added
~~~~~

* Database service

  * Support for new commands

    * ``oci db autonomous-database list-refreshable-clones``
    * ``oci db cloud-exa-infra add-storage``
    * ``oci db cloud-vm-cluster add``
    * ``oci db cloud-vm-cluster remove``

  * Support for new optional parameters

    * ``oci db cloud-vm-cluster create --data-storage-size-in-tbs --db-node-storage-size-in-gbs --db-servers --memory-size-in-gbs``
    * ``oci db cloud-vm-cluster update --data-storage-size-in-tbs --db-node-storage-size-in-gbs --memory-size-in-gbs``

* Support for creating rollback jobs in the Resource Manager service

  * ``oci resource-manager job create-plan-rollback-job``
  * ``oci resource-manager job create-apply-rollback-job``

* Support for EDGE value for existing parameter --node-type in the Big Data service

  * ``oci bds instance worker-nodes add --node-type``

* Support for new optional parameter in the Data Flow service
  
  * ``oci data-flow private-endpoint create --scan-details``
  * ``oci data-flow private-endpoint update --scan-details``

* Application Dependency Management service

  * Support for new commands

    * ``oci adm vulnerability-audit create-vulnerability-audit-external-resource-vulnerability-audit-source``
    * ``oci adm vulnerability-audit create-vulnerability-audit-oci-resource-vulnerability-audit-source``
    * ``oci adm vulnerability-audit create-vulnerability-audit-unknown-source-vulnerability-audit-source``

  * Support for new optional parameters

    * ``oci adm vulnerability-audit list-application-dependency-vulnerabilities --depth --root-node-id``

Changed
~~~~~~~

* Dependency on click is downgraded to 7.1.2

* The required parameters --application-dependencies --compartment-id are now optional in the Application Dependency Management service

  * ``oci adm vulnerability-audit create --application-dependencies --compartment-id``

* Error message improvement with troubleshooting tips on RequestTimeout and ConnectTimeout for CLI commands with JSON inputs

Fixed     
~~~~~

* Fixed incorrectly raised PermissionError when downloading content in folders created from the console in the Object Storage service

  * ``oci os object bulk-download``

* Fixed repeated confirmation prompt for no passphrase setup

  * ``oci setup config``
  * ``oci setup keys``


3.20.0 - 2022-11-01
--------------------

Added
~~~~~

* Database service

  * Support for Clone from backup from last available timestamp

    * ``oci db autonomous-database create-from-backup-timestamp --use-latest-available-backup-time-stamp ``

  * The required parameter --timestamp is now optional in the below command

    * ``oci db autonomous-database create-from-backup-timestamp``

  * The required parameter --display-name is now optional in the below command

    * ``oci db autonomous-database-backup create``

* Support for agent settings parameter for specifying third-party Qualys scanner when creating or updating a host scan recipe in the Vulnerability Scanning service

  * ``oci vulnerability-scanning host scan recipe create --agent-settings ``
  * ``oci vulnerability-scanning host scan recipe update --agent-settings ``

* Support for the below commands in the Logging Analytics service

  * ``oci log-analytics storage list-encryption-key-info``
  * ``oci log-analytics storage assign-encryption-key``

* Golden Gate service

  * Support for Connections for Database Resources

    * ``oci golden-gate connection``

  * Support for the below new command

    * ``oci goldengate deployment-type-collection list-deployment-types``

  * Support for the parameters --assignable-connection-id, --assigned-connection-id and --supported-connection-type in the below command

    * ``oci goldengate deployment list``

Changed
~~~~~~~~

* [BREAKING] The command oci organizations work-request-log-entry list has been changed to oci organizations work-request-log list in the Organization service

* Improved CLI error message on incorrect JSON input

3.19.0 - 2022-10-25
--------------------
Added
~~~~~~~~

* Support for Full Stack Disaster Recovery service

  * ``oci disaster-recovery``

* The AI Language service

  * Support for the Language custom models

    * ``oci ai language project``
    * ``oci ai language model``
    * ``oci ai language endpoint``

  * Support for the language translation

    * ``oci ai language batch-language-translation``

  * Support for new optional parameters in the batch service

    * ``oci ai language batch-detect-entities --compartment-id --endpoint-id``
    * ``oci ai language batch-detect-key-phrases --compartment-id``
    * ``oci ai language batch-detect-language --compartment-id``
    * ``oci ai language batch-detect-sentiments --compartment-id``
    * ``oci ai language batch-detect-text-classification --compartment-id --endpoint-id``

* Data Flow Service

  * Support for running code interactively with Session Applications using Statement resource

    * ``oci data-flow statement create --code --run-id``
    * ``oci data-flow statement delete --run-id --statement-id``
    * ``oci data-flow statement get --run-id --statement-id``
    * ``ooci data-flow statement list --run-id``

  * Support for new optional parameters

    * ``oci data-flow application create --idle-timeout-in-minutes --max-duration-in-minutes``
    * ``oci data-flow application update --idle-timeout-in-minutes --max-duration-in-minutes``
    * ``oci data-flow run create --idle-timeout-in-minutes --max-duration-in-minutes``
    * ``oci data-flow run submit --idle-timeout-in-minutes --max-duration-in-minutes``
    * ``oci data-flow run update --idle-timeout-in-minutes --max-duration-in-minutes``

* Support for using combination of environment variable and other required parameter in commands ,if config file is not present 

Fixed
~~~~~

* Fixed mismatched help text format when using ``--help``

Changed
~~~~~~~

* Dependency on click is upgraded to 8.0.4

* Data Flow Service

  * [BREAKING] The parameter --file-url has been removed from the below command

    * ``oci data-flow application create``

  * [BREAKING] The parameters --defined-tags, --force, --freeform-tags, --if-match, --max-wait-seconds, --wait-for-state, --wait-interval-seconds have been deleted from the below command

    * ``oci data-flow statement list``

3.18.1 - 2022-10-04
--------------------
Added
~~~~~~~~

* Bastion support for target host identification and enabled SOCKS support for dynamic port forwarding sessions

  * ``oci bastion``

* Operations Insights service

  * Support for creating Enterprise Manager-based Windows host targets for ``--platform-type``

    * ``oci opsi host-insights list --platform-type``

  * Support for creating Management Agent Cloud Service-based Windows and Solaris hosts targets for ``--platform-type``

    * ``oci opsi host-insights list --platform-type``

  * Support for Host Top Process allowing users to locate top processes running at a particular point in time

    * ``oci opsi host-insights summarize-top-processes-usage --compartment-id --id --resource-metric --timestamp --analysis-time-interval``

  * Support for Host Top Process allowing users to filter by a single process in order to trend this process over time

    * ``oci opsi host-insights summarize-top-processes-usage --compartment-id --id --resource-metric --timestamp --analysis-time-interval``
    
* Cloud-Bridge Service

  * Support for check to require ``--vcenter-endpoint`` and ``--discovery-credentials`` parameters if asset source is VMWARE for ``--type``

    * ``oci cloud-bridge discovery asset-source create --type VMWARE``

3.18.0 - 2022-09-27
--------------------

Added
~~~~~~~~

* Support for previous pagination in Resource Search service

  * ``oci search resource structured-search --page $opc-previous-token``

* Support for Elastic Compute feature as part of database service

  * ``oci db exadata-infrastructure generate-recommended-vm-cluster-network --db-servers``
  * ``oci db exadata-infrastructure update --additional-compute-count, --additional-compute-system-model``
  * ``oci db vm-cluster-network resize --action, --exadata-infrastructure-id, --vm-cluster-network-id, --vm-networks``

* Stack Monitoring service

  * Support for new command

    * ``oci stack-monitoring resource search-associated-resources``

  * Support for new optional parameter

    * ``oci stack-monitoring resource search --external-id``
    * ``oci stack-monitoring resource create --external-id``
    * ``oci stack-monitoring resource delete --is-delete-members``

* NoSQL service

  * ``oci nosql query prepare``

    * Added a new optional argument ``--is-get-query-plan``
    * Added the optional ``queryPlan`` property in the JSON response

  * ``oci nosql table get``

    * Added the properties ``isAsUuid`` and ``isGenerated`` to the ``Column`` JSON object that is included in the JSON response
    * Added the ``identity`` JSON object that is included in the the JSON response

  * ``oci nosql table list-table-usage``

    * Added the property ``maxShardSizeUsageInPercent`` in the JSON response

Changed
~~~~~~~
* [BREAKING]  DNS service

  *  ``oci dns resolver-endpoint create --subnet-id --nsg-ids``

    * Required parameter ``--subnet-id`` was added
    * Optional paramater ``--nsg-ids`` was added
    * Optional paramater ``--endpoint-type`` was removed


  * ``oci dns resolver-endpoint update``

    * The optional paramater ``--nsg-ids`` was added

3.17.0 - 2022-09-20
--------------------

Added
~~~~~

* Support for the Cloud Migrations service

  * ``oci cloud-migrations``

* Support for the Cloud Bridge service

  * ``oci cloud-bridge``

* Support for listing summary messages, trail files, and trail file sequences for a deployment in the Golden Gate service

  * ``oci goldengate message-summary list-messages``
  * ``oci goldengate trail-file-summary list-trail-files``
  * ``oci goldengate trail-sequence-summary list-trail-sequences``

* Threat Intelligence service

  * Support for new command

    * ``oci threat-intelligence indicator summarize``

  * Support for new optional parameters

    * ``oci threat-intelligence indicator-summaries list-indicators --time-created-after --time-created-before --time-last-seen-after --time-last-seen-before --time-updated-before``

* Log Analytics service

  * Support for new commands

    * ``oci log-analytics ingest-time-rule``
    * ``oci log-analytics rule list``

  * Support for new optional parameters

    * ``oci log-analytics object-collection-rule create --log-set --log-set-ext-regex --log-set-key --timezone``
    * ``oci log-analytics object-collection-rule update --log-set --log-set-ext-regex --log-set-key --timezone``
    * ``oci log-analytics storage recall-archived-data --log-sets --query-string``

* Support for new commands in the DevOps service

  * ``oci devops connection create-vbs-connection``
  * ``oci devops connection update-vbs-connection``
  * ``oci devops trigger create-vbs-trigger``
  * ``oci devops trigger update-vbs-trigger``

* Support for new optional parameters in the Usage service

  * ``oci usage-api schedule create --output-file-format --saved-report-id --description``
  * ``oci usage-api schedule update --output-file-format --result-location --description``

* Data integration service

  * Support for new commands

    * ``oci data-integration runtime-operator get``
    * ``oci data-integration runtime-operators list-runtime-operators``
    * ``oci data-integration runtime-pipeline get``
    * ``oci data-integration runtime-pipelines list-runtime-pipelines``
    * ``oci data-integration task-run-lineage list-task-run-lineages``
    * ``oci data-integration task-run-lineage list_taskrun_lineages``

  * Support for new optional parameters

    * ``oci data-integration data-entity list --include-types``
    * ``oci data-integration data-flow-validation create --target-field-map-summary --typed-object-map``
    * ``oci data-integration dis-application create --compartment-id``
    * ``oci data-integration schema list --include-types``
    * ``oci data-integration workspace create --endpoint-compartment-id --endpoint-id --endpoint-name --registry-compartment-id --registry-id --registry-name``

Changed
~~~~~~~
* [BREAKING] oci governance-rules-control-plane work-request work-request-log list renamed in the Governance Rules Control Plane service

  * ``oci governance-rules-control-plane work-request work-request-log-entry list-work-request-logs``

* [BREAKING] --previous-deployment-id is now a required parameter in the DevOps service

  * ``oci devops deployment create-pipeline-redeployment --previous-deployment-id``

* The parameter --query-properties is now optional in the Usage service

  * ``oci usage-api schedule create``

3.16.1 - 2022-09-13
--------------------

Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the Madrid region (``--region eu-madrid-1``)

* Data Science service

  * Support for new optional parameter

    * ``oci data-science model create-model-artifact --if-match``

  * Support for new commands

    * ``oci data-science model export-model-artifact``
    * ``oci data-science model export-model-artifact-artifact-export-details-object-storage``
    * ``oci data-science model import-model-artifact``
    * ``oci data-science model import-model-artifact-artifact-import-details-object-storage``

3.16.0 - 2022-09-06
--------------------

Added
~~~~~
* Monitoring service

  * Support for new parameters
  
    * ``oci monitoring alarm create --is-notifications-per-metric-dimension-enabled``
    * ``oci monitoring alarm update --is-notifications-per-metric-dimension-enabled``
    * ``oci monitoring metric-data post --content-encoding``

  * Support for retrieving dimension

    * ``oci monitoring alarm-dimension-states-collection retrieve-dimension-states``

* Support for Preferred Credentials for performing privileged operations in the Database Management service
 
  * ``oci database-management preferred-credential``

* Data Connectivity service

  * Support for new commands

    * ``oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-message``
    * ``oci data-connectivity data-preview create-data-preview-derived-entity``
    * ``oci data-connectivity data-profile create-data-profile-derived-entity``
    * ``oci data-connectivity execute-operation-job-details create-execute-operation-job-operation-from-api``

  * Support for new parameters

    * ``oci data-connectivity endpoint update --dns-zones``
    * ``oci data-connectivity data-entity list --include-types``
    * ``oci data-connectivity schema list --include-types``

  * Support for new optional parameter data-entity-entity-properties in the below commands

    * ``oci data-connectivity data-entity create-data-preview-ds``
    * ``oci data-connectivity data-entity create-data-preview-file``
    * ``oci data-connectivity data-entity create-data-preview-sql``
    * ``oci data-connectivity data-entity create-data-preview-table``
    * ``oci data-connectivity data-entity create-data-preview-view``
    * ``oci data-connectivity data-entity create-data-profile-ds``
    * ``oci data-connectivity data-entity create-data-profile-file``
    * ``oci data-connectivity data-entity create-data-profile-sql``
    * ``oci data-connectivity data-entity create-data-profile-table``
    * ``oci data-connectivity data-entity create-data-profile-view``
    * ``oci data-connectivity data-preview create-data-preview-data-entity-from-data-store``
    * ``oci data-connectivity data-preview create-data-preview-data-entity-from-file``
    * ``oci data-connectivity data-preview create-data-preview-data-entity-from-sql``
    * ``oci data-connectivity data-preview create-data-preview-data-entity-from-table``
    * ``oci data-connectivity data-preview create-data-preview-data-entity-from-view``
    * ``oci data-connectivity data-profile create-data-profile-data-entity-from-data-store``
    * ``oci data-connectivity data-profile create-data-profile-data-entity-from-file``
    * ``oci data-connectivity data-profile create-data-profile-data-entity-from-sql``
    * ``oci data-connectivity data-profile create-data-profile-data-entity-from-table``
    * ``oci data-connectivity data-profile create-data-profile-data-entity-from-view``
    * ``oci data-connectivity execute-operation-job-details create-execute-operation-job-operation-from-procedure``

Changed
~~~~~~~
* [BREAKING] Data Connectivity service

  * The optional parameter resource-id renamed to registry-id for the command

    * ``oci data-connectivity work-request list``

  * The commands below are deleted

    * ``oci data-connectivity connection-validation delete``
    * ``oci data-connectivity connection-validation get``
    * ``oci data-connectivity connection-validation list``

3.15.2 - 2022-08-26
--------------------

Added
~~~~~
* Support for dynamic window sizing and new terminal too small error message in interactive mode

  * ``oci -i``

* Support for in-place upgrade in the OCVS service

  * ``oci ocvs esxi-host create``

* Support for customers to choose to opt for Guest VM event collection, diagnostics logs and traces in the Database service

  * ``oci db system launch``
  * ``oci db system launch-from-backup``
  * ``oci db system launch-from-database``
  * ``oci db system launch-from-db-system``
  * ``oci db system update``
  * ``oci db data-guard-association create with-new-db-system``

* Support for performance-based autotuning of Block and Boot Volumes in the Block Storage service

  * ``oci bv boot-volume create``
  * ``oci bv boot-volume create-boot-volume-boot-volume-source-from-boot-volume-replica-details``
  * ``oci bv boot-volume update``
  * ``oci bv volume create``
  * ``oci bv volume create-volume-volume-source-from-block-volume-replica-details``
  * ``oci bv volume update``

* Support for Single Client Access Name protocol as Data Source and for Network Security Groups in Private Access Channel in the Analytics service

  * ``oci analytics analytics-instance create-private-access-channel``

3.15.1 - 2022-08-23
--------------------

Added
~~~~~
* Support for support rewards redemption summaries in the Usage service 

  * ``oci usage redemption-summary list-redemption-summaries``

* Support for parent tenancy of an organization to view child tenancy categories, recommendations, and resource actions in the Optimizer service

  * ``oci optimizer category-summary list``
  * ``oci optimizer recommendation-summary list``
  * ``oci optimizer resource-action-summary list``

* Support for File filter in the DevOps service
  
  * ``oci devops trigger create-bitbucket-cloud-trigger``
  * ``oci devops trigger create-github-trigger``
  * ``oci devops trigger create-gitlab-trigger``
  * ``oci devops trigger update-bitbucket-cloud-trigger``
  * ``oci devops trigger update-github-trigger``
  * ``oci devops trigger update-gitlab-trigger``

* Added additional support for Configuration variables to MDS in the MySQL Service
 
  * ``oci mysql configuration create --init-variables``

* Database service

  * Support for allowing choosing prior versions for Infrastructure Maintenance for ExaCC
   
    * ``oci db infrastructure-target-version get``

  * Support for new optional parameters

    * ``oci db maintenance-run update --target-db-server-version --target-storage-server-version``

Changed
~~~~~~~
* Optimizer service

  * The parameter --category-id is now optional in the below command
  
    * ``oci optimizer recommendation-summary list``

  * The parameter --recommendation-id is now optional in the below commands

    * ``oci optimizer resource-action-summary filter-resource-actions``
    * ``oci optimizer resource-action-summary list``

3.15.0 - 2022-08-16
--------------------
Added
~~~~~
* Support for debug reports and analysis in Service Mesh service

  * ``oci service-mesh debug report``

* Support for Logging Analytics as a target for Streaming Source feature for Service Connector Hub in the Logging service

  * ``oci logging analytics target``

* Support for streaming Application logs to Logging Service in the Data Flow Service

  * ``oci data-flow run create --application-log-config``
  * ``oci data-flow application create --application-log-config``
  * ``oci data-flow application update --application-log-config``
  * ``oci data-flow run submit --application-log-config``

* Support for the below commands in the Cloud Guard service

  * ``oci cloud-guard data-source``
  * ``oci cloud-guard detector-recipe-detector-rule``
  * ``oci cloud-guard problem list-problem-entities``
  * ``oci cloud-guard work-request``
  * ``oci cloud-guard work-request-error``
  * ``oci cloud-guard work-request-log-entry``

Changed
~~~~~
* The parameter --source-detector-recipe-id is now optional in the below command in the Cloud Guard service

  * ``oci cloud-guard detector-recipe create``

Fixed
~~~~~
* [BREAKING] The command ``oci logging-search search-result search-logs`` has been changed back to be ``oci logging-search search-logs``

3.14.0 - 2022-08-09
--------------------
Added
~~~~~
* Support for moving resources in the Dashboard Service
 
  * ``oci dashboard-service dashboard-group change-compartment``
  * ``oci dashboard-service dashboard change-dashboard-group`` 
  
* Java Management service

  * Support for Java download and installation

    * ``oci jms java-family get``
    * ``oci jms java-family-collection list-java-families``
    * ``oci jms java-release``
    * ``oci jms installation-site-summary add``
    * ``oci jms fleet generate-agent-deploy-script``
  
  * Support for new parameters

    * ``oci jms application-usage summarize --display-name-contains``
    * ``oci jms fleet create --inventory-log, --is-advanced-features-enabled``
    * ``oci jms fleet list --display-name-contains``
    * ``oci jms fleet update --is-advanced-features-enabled``
    * ``oci jms installation-site-summary list-installation-sites --path-contains, --time-end, --time-start``
    * ``oci jms installation-usage summarize --path-contains``
    * ``oci jms managed-instance-usage summarize --hostname-contains``
  
* Support for ETags for Optimistic Concurrency Control for all commands in Load Balancer service 

  * ``oci lb --if-match``
   
* Support for single host Software Defined Data Center in the Oracle Cloud VMware Provisioning service
 
  * `` oci ocvs sddc create --is-single-host-sddc ``
  
* Support for maintenance run history for Infrastructure maintenance for ExaCC as part of Database service

  * ``oci db maintenance-run-history``
  
* Support for Optimiser statistics monitoring and management for Database Management service
 
  * ``oci database-management managed-database get-optimizer-statistics-advisor-execution``
  * ``oci database-management managed-database get-optimizer-statistics-advisor-execution-script``
  * ``oci database-management managed-database get-optimizer-statistics-collection-operation``
  * ``oci database-management managed-database implement-optimizer-statistics-advisor-recommendations``
  * ``oci database-management managed-database list-optimizer-statistics-advisor-executions``
  * ``oci database-management managed-database list-optimizer-statistics-collection-aggregations``
  * ``oci database-management managed-database list-optimizer-statistics-collection-operations``
  * ``oci database-management managed-database list-table-statistics``
    
* APM Synthetic service

  * Support for Round Robin Alerting for create/update monitors

    * ``oci apm-synthetics monitor create-browser-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor create-rest-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor create-scripted-browser-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor create-scripted-rest-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor update-browser-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor update-rest-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor update-scripted-browser-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
    * ``oci apm-synthetics monitor update-scripted-rest-monitor --batch-interval-in-seconds, --dns-configuration, --is-run-now, --scheduling-policy``
        
  * Support for aggregated network data

    * ``oci apm-synthetics aggregated-network-data-result aggregate-network-data``
  
* Operations Insights (OPSI) service

  * Support for OCI Compute Instances

    * ``oci opsi host-insights create-macs-cloud-host``
    * ``oci opsi host-insights enable-macs-cloud-host``
    * ``oci opsi host-insights list-macs-cloud-hosts``
    * ``oci opsi host-insights update-macs-cloud-host``
    
  * Support to filter by host Id and host type for capacity planning
  
    * oci opsi host-insights summarize-host-insight-resource-capacity-trend --host-id --host-type
    * oci opsi host-insights summarize-host-insight-resource-forecast-trend --host-id --host-type
    * oci opsi host-insights summarize-host-insight-resource-statistics --host-id --host-type
    * oci opsi host-insights summarize-host-insight-resource-usage-trend --host-id --host-type
    * oci opsi host-insights summarize-host-insight-resource-usage --host-id --host-type
    * oci opsi host-insights summarize-host-insight-resource-utilization-insight --resource-metric --host-id --host-type
    * oci opsi host-insights summarize-top-processes-usage-trend --host-id --host-type
    * oci opsi host-insights list-host-configurations --host-id --host-type
    * oci opsi host-insights list-hosted-entities --host-id --host-type
  
* Support shape option for creating instance in the Integration service

  * ``oci integration integration-instance create --shape``

Changed
~~~~~~~
* [BREAKING] Multiple subgroup and command renames in the Open Search service

  * ``oci opensearch cluster``
  * ``oci opensearch backup``

* [BREAKING] --inventory-log is now a required parameter in the Java Management Service

  * ``oci jms fleet create --inventory-log`` 

3.13.0 - 2022-08-02
--------------------
Added
~~~~~
* Support for the Open Search service

  * ``oci opensearch``

* Support for private repositories in the DevOps service

  * Added support for DevOps Build connection resource for private repositories
  
    * ``oci devops connection create-bitbucket-server-connection``
    * ``oci devops connection create-gitlab-server-connection``
    * ``oci devops connection update-bitbucket-server-connection``
    * ``oci devops connection update-gitlab-server-connection``

  * Added support for DevOps Build trigger resource for private repositories
  
    * ``oci devops trigger create-gitlab-server-trigger``
    * ``oci devops trigger create-bitbucket-server-trigger``
    * ``oci devops trigger update-bitbucket-server-trigger``
    * ``oci devops trigger update-gitlab-server-trigger``

  * Added support for DevOps Build stage resource to use private connections
  
    * ``oci devops build-pipeline-stage create-build-stage --network-channel``
    * ``oci devops build-pipeline-stage update-build-stage --network-channel``
  
Changed
~~~~~~~
* Changed --table-limits argument to optional in the NoSQL service

  * ``oci nosql table create --table-limits``

* Changed loading json document to support case insensitive prefix (file://) for global parameter and all json loading commands

  * ``--from-json``
  
* [BREAKING] Command and subgroup work-request-log list renamed in the Governance Rules Control Plane service

  * ``oci governance-rules-control-plane work-request work-request-log-entry list-work-request-logs``
  
* [BREAKING] Subgroup work-request renamed in the Tenant Manager Control Plane service

  * ``oci organizations work-request-log list``

3.12.0 - 2022-07-26
--------------------
Added
~~~~~
* [BREAKING]  Support for the Fusion Apps as a Service

  * ``oci fusion-apps``

* Support for specifying size preference when requesting a Data Transfer Appliance in the Data Transfer Service

  * ``oci dts appliance request --minimum-storage-capacity-in-terabytes``

* Support for listing all boot volume and replicas within a volume group replica in Boot-volume service

  * ``oci bv boot-volume list --volume-group-id``
  * ``oci bv boot-volume-replica list --volume-group-replica-id``

* ``Big data service``

    * Added support for encryption of boot and block volumes associated with the cluster using customer specified kmsKeyId

       * ``oci bds instance create --kms-key-id``
       * ``oci bds instance update --kms-key-id``

    * Added support for VM.Standard.E4.Flex shape for Cloud SQL (CSQL) node

       * ``oci bds cloudsql add --shape-config``

* Support for Autonomous Database Dedicated on ExaCS in Operator Access Control Service

  * ``oci opctl operator-control create --resource-type``
  * ``oci opctl operator-control-assignment create --resource-type``

* Support for new parameter in management-agent service

      * ``oci management-agent work-request list --type``
      * ``oci management-agent plugin list --agent-id``
      * ``oci management-agent agent list --access-level --compartment-id-in-subtree``

* Support for viewing Automatic Workload Repository (AWR) data for databases added to AWRHub in Operations Insights service

  * ``oci opsi awr-hubs *``

* Support for Monthly Security Maintenance with subtype "SECURITY_MONTHLY" in Database service

  * ``oci db maintenance-run list --maintenance-subtype SECURITY_MONTHLY``

* Support for new fields to enable/modify database management in Database service

  * ``oci db database modify-database-management --port --protocol --role --ssl-secret-id``

* Support for runtime configuration in notebook session in Data-science service

  * ``oci data-science notebook-session create --runtime-config-details``
  * ``oci data-science notebook-session update --runtime-config-details``

* Support for following command in Media service

  * ``oci media-services media-stream``

Fixed
~~~~~~~
* Fixed "wait-for-state" for oci db autonomous-database delete

  * ``oci db autonomous-database delete --wait-for-state``

3.11.1 - 2022-07-19
--------------------
Added
~~~~~
* Support for 2 new global parameters to provide connection and read timeout value

  * ``oci --connection-timeout --read-timeout``
  
* Support for Container Databases (CDBs) and Pluggable Databases (PDBs) discovery in the Stack Monitoring service

  * ``oci stack-monitoring discovery-job create --compartment-id --discovery-details``
  
* Support for the Fusion Apps service 

  * ``oci fusion-apps``

* Support for the Oracle Process Automation service

  * ``oci opa``

* Support for ingress routing tables to NAT Gateway and Internet Gateway in the VCN Routing service

  * ``oci network nat-gateway create --route-table-id``
  * ``oci network nat-gateway update --route-table-id`` 
  * ``oci network internet-gateway create --route-table-id``
  * ``oci network internet-gateway update --route-table-id``
  
* Support for maintenance reboot due date extension on Virtual Machine instances in the core service

  * ``oci compute instance-maintenance-reboot get``
  * ``oci compute instance update --time-maintenance-reboot-due``
  
* Support for Oracle Managed Access service
  
  * ``oci oma``
  
* Support for grapePeriod for wallet rotation feature in the Autonomous Database service

  * ``oci db autonomous-database-wallet rotate --grace-period``
  * ``oci db autonomous-database-wallet rotate-regional-wallet --grace-period`` 
  
* Support for the Media service

  * ``oci media-services``
  
Changed
~~~~~~~
* Modified supported version for the following package: cryptography (>=3.2.1, <=37.0.2), pyOpenSSL (>=17.5.0, <=22.0.0)

3.11.0 - 2022-07-12
--------------------
Added
~~~~~
* Support to provide database management private endpoint ID as input to enable DBCS databases in the Operations Insights service

  * ``oci opsi database-insights create-pe-comanged-database --dbm-private-endpoint-id``

* Support for the below new fields to create data guard association with new db system in the Database service

  * ``oci db data-guard-association create with-new-db-system --database-defined-tags --database-freeform-tags --db-system-defined-tags --db-system-freeform-tags --fault-domains --license-model --node-count --private-ip --time-zone``

* Support for Native Pod Networking in Oracle Kubernetes Engine service

  * ``oci ce cluster create --cluster-pod-network-options``
  * ``oci ce node-pool create --max-pods-per-node --pod-nsg-ids --pod-subnet-ids``
  * ``oci ce node-pool update --max-pods-per-node --pod-nsg-ids --pod-subnet-ids``

* Support for Compute Instance Maintenance in the Compute service

  * ``oci compute instance action --action rebootmigrate``

* Support Point-in-time Recovery for non-HA MySQL Database service

  * oci mysql db-system create ... --backup-policy='{"pitr-policy": {"isEnabled": true | false}}'

  * oci mysql db-system create ... --source='{"sourceType": "PITR", "dbSystemId": "$DBSYSTEM_ID", "recoveryPoint": "$RECOVERY_POINT"}'

Changed
~~~~~~~
* [BREAKING] The confusing flag naming for preserving data volumes created on instance launch --preserve-data-volumes is removed in the compute service

  * ``oci compute instance terminate --preserve-data-volumes``

* Bug fixes and improvements to project_o

3.10.5 - 2022-06-28
--------------------
Added
~~~~~
* Support for the Network Monitoring service

  * ``oci vn-monitoring``

* Support for EmWarehouse Service

  * ``oci em-warehouse``

* Support for specifying application scan settings when creating or updating host scan recipes in the Vulnerability Scanning service

  * ``oci vulnerability-scanning host scan recipe create --application-settings``
  * ``oci vulnerability-scanning host scan recipe update --application-settings``

* Support for shared infrastructure autonomous database character sets in the Database service

  * ``oci db autonomous-database-character-sets list``

* Support for safe-deleting nodes in the Container Engine for Kubernetes service

  * ``oci ce node-pool create --is-force-deletion-after-override-grace-duration-query-param``
  * ``oci ce node-pool update --is-force-deletion-after-override-grace-duration-query-param``
  * ``oci ce node-pool delete --is-force-deletion-after-override-grace-duration-query-param``
  * ``oci ce node-pool delete-node --is-force-deletion-after-override-grace-duration-query-param``

Changed
~~~~~~~~
* Support for ``ncharacter-set`` and ``ncharacter-set`` in Autonomous database service

  * ``oci db autonomous-database create --character-set "AL32UTF8" --ncharacter-set "AL16UTF16"``

3.10.4 - 2022-06-21
--------------------
Added
~~~~~
* Support for the Network Firewall service

  * ``oci network-firewall``
  
* Support for CSV file type datasets for text labeling and JSONL in the Data Labeling service

  * ``oci data-labeling-service dataset create-dataset-text-dataset-format-details --dataset-format-details-text-file-type-metadata``

* Support for diagnostics in the Database Management service

  * ``oci database-management diagnosability``
  * ``oci database-management sql-tuning-task``

Fixed
~~~~~~~
* Fixed following command/operations input, output filenames and path for windows OS in object storage service

  * ``oci os object sync``

* Fixed pagination bug in list database service

  * ``oci db database list``

3.10.3 - 2022-06-14
--------------------
Added
~~~~~

* Support for clearing commands history with 'F7' in interactive mode
  
  * ``oci -i``

* Support for the Web Application Acceleration (WAA) service

  * ``oci waa``

* Support for the Governance Rules service

  * ``oci governance-rules-control-plane governance-rule``

* Support for the OneSubscription service

  * ``oci onesubscription``

* Support for quota resource locking in the Limits service

  * ``oci limits quota addlock``
  * ``oci limits quota removelock``
  * ``oci limits quota create --locks``
  * ``oci limits quota delete --is-lock-override``

* Support for ``--wait-for-state`` for following command in the MySQL Database service

  * ``oci mysql backup update``

* Support for time zone in Cloud Autonomous VM (CAVM) clusters in the Database service

  * ``oci db cloud-autonomous-vm-cluster create --cluster-time-zone``

* Support for configuration options in the Application Performance Monitoring service

  * ``oci apm-config config create-options``

* Support for MySQL connections in the Database Tools service

  * ``oci dbtools connection``

* Support for resource locking in the Identity service

  * ``oci iam tag-namespace add --tag-namespace-id $tag_namespace_id --type $lock_type``
  * ``oci iam tag-namespace remove --tag-namespace-id $tag_namespace_id --type $lock_type``
  * ``oci iam tag-default add --tag-default-id $tag_default_id --type $lock_type``
  * ``oci iam tag-default remove --tag-default-id $tag_default_id --type $lock_type``

Fixed
~~~~~~~
* Fixed bugs in the following commands in Rover service

  * ``oci rover node add-workload``
  * ``oci rover node create``


3.10.2 - 2022-06-07
--------------------
Added
~~~~~
* Support for private endpoint in the Resource Manager service

  * ``oci resource-manager private-endpoint``
  
* Support for generated downloading terraform plan output in json or binary format in the Resource Manager service

  * ``oci resource-manager job get-job-tf-plan`` 
  
* Support for query OPSI Data Objects

  * ``oci opsi opsi-data-objects``

Changed
~~~~~~~
* Modified supported version for the following package: prompt-toolkit (==3.0.29)

Fixed
~~~~~~~
* Bug fix for --arguments property to be able to correctly convert string to json in dataflow service

  * ``oci data-flow run create --arguments``

* Bug in --wait-for-state param for following commands in the Key management system service

  * ``oci kms management key-version create``
  * ``oci kms management key-version cancel-key-version-deletion``
  * ``oci kms management key-version schedule-key-version-deletion``


3.10.1 - 2022-05-31
--------------------
Added
~~~~~
* Support for in-depth monitoring, diagnostics capabilities, and advanced management functionality for on-premise Oracle databases in the Database Management service

  * ``oci database-management fleet-health-metrics``
  * ``oci database-management summary-metrics``
  * ``oci database-management managed-database list-users``

* Support for using Oracle Cloud Agent to perform iSCSI login and logout for non-multipath-enabled iSCSI attachments in the Container Engine for Kubernetes service

  * ``oci compute volume-attachment attach-iscsi-volume --is-agent-auto-iscsi-login-enabled``

* Kubernetes service

  * Support for Fault Domain placement in the Container Engine

    * ``oci ce node-pool create --placement-configs``
    * ``oci ce node-pool update --placement-configs``

  * Support for worker node images in the Container Engine

    * ``oci ce node-pool create --kubernetes-version``

* Support for flexible shapes using the ``--driver-shape-config``  and ``--executor-shape-config`` properties in the Data Flow service

  * ``oci data-flow run create``
  * ``oci data-flow application create``
  * ``oci data-flow application update``
  * ``oci data-flow run create``
  * ``oci data-flow run submit``

3.10.0 - 2022-05-24
------------------
Added
~~~~~

* Support for License Manager Service

  * ``oci license-manager``

* Support the use of compute capacity reservation in OCVS SDDCs in the Oracle Cloud VMware Solution service

  * ``oci ocvs esxi-host create --capacity-reservation-id``
  * ``oci ocvs sddc create --capacity-reservation-id``

* Oracle Digital Assistant service

  * Support for Packaged skill management APIs

    * ``oci oda odapackage``

  * Support for Role-based access on instance creation

    * ``oci oda oda-instance create --is-role-based-access``

  * Support for assigned ownership (attachment) APIs

    * ``oci oda oda-instance-attachment``

  * Support for instance metadata management APIs

    * ``oci oda management``

* Support for Usage Plans in the API Gateway service

  * ``oci api-gateway usage-plan``
  * ``oci api-gateway subscriber``

* Support for Oracle Linux 8 Application Streams in the OS Management Service

  * ``oci os-management managed-instance disable-module-stream``
  * ``oci os-management managed-instance enable-module-stream``
  * ``oci os-management managed-instance install-module-profile``
  * ``oci os-management managed-instance list-module-profiles``
  * ``oci os-management managed-instance list-module-streams``
  * ``oci os-management managed-instance remove-module-profile``
  * ``oci os-management managed-instance switch-module-stream``
  * ``oci os-management module-profile``
  * ``oci os-management module-stream``

Changed
~~~~~~~
* Improved service error exception for all CLI commands

* [BREAKING] The parameter --specification is now required in the below command

  * ``oci api-gateway deployment create --specification``

* [BREAKING] The command below is deleted in the OS Management Service

  * ``oci os-management work-request-summary``

3.9.1 - 2022-05-17
------------------
Added
~~~~~
* Support for Interactive mode for all services

  * ``oci -i``

* Support for the following features in the DevOps service

  * Application Dependency Management service scan results in response to ``oci devops build-run get``

  * Build resources to use Bitbucket Cloud repositories for source code
  
    * ``oci devops connection create-bitbucket-cloud-connection``
    * ``oci devops connection update-bitbucket-cloud-connection``
    * ``oci devops trigger create-bitbucket-cloud-trigger``
    * ``oci devops trigger update-bitbucket-cloud-trigger``

  * Helm charts and repositories on deployments 
     
    * ``oci devops deploy-artifact create-helm-repository-artifact``
    * ``oci devops deploy-artifact update-helm-repository-artifact``
    * ``oci devops deploy-stage create-oke-helm-chart-stage``
    * ``oci devops deploy-stage update-oke-helm-chart-stage``

* Support for the following features in the Database service

  * CharacterSet and nCharacterSet selection on autonomous dedicated databases. If not specified, the databases are created with default characterSets.

    * ``oci db autonomous-database create --character-set, --ncharacter-set``
    * ``oci db autonomous-database create-from-backup-id --character-set, --ncharacter-set``
    * ``oci db autonomous-database create-refreshable-clone --character-set, --ncharacter-set``

  * Support for listing autonomous dedicated database supported character sets
    
    * ``oci db autonomous-database-character-sets list`` 

  * Support for AMD E4 flex shapes on virtual machine database systems

    * ``oci db compute-performance list``
    * ``oci db storage-performance list``    

* Support for information requests in the Operator Access Control service

  * ``oci opctl access-request list-interactions``
  * ``oci opctl access-request interaction-request``


Changed
~~~~~~~~
* Support for terraform and improvements for cross-region ADGs in the Database service

  * Changes to the response fields for ``oci db autonomous-database get`` 

    * Deprecated: ``isDataGuardEnabled``, ``standbyDb``
    * ``isLocalDataGuardEnabled`` Indicates whether the Autonomous Database has local (in-region) Data Guard enabled.
    * ``isRemoteDataGuardEnabled`` Indicates whether the Autonomous Database has Cross Region Data Guard enabled.
    * ``localStandbyDb`` Autonomous Data Guard standby database details.

  * Changes to the response fields for ``oci db autonomous-database update``

    * Deprecated: ``isDataGuardEnabled``
    * ``isLocalDataGuardEnabled`` Indicates whether the Autonomous Database has local (in-region) Data Guard enabled.

  * ``oci db autonomous-database create-adb-cross-region-data-guard-details``

    * ``--db-name`` is not a required parameter

  * ``oci db autonomous-database delete``

    * Can now be used to delete a standby instance for Cross Region Data Guard.

Fixed
~~~~~~~

* Bug for KeyError while running ``oci session export``

3.9.0 - 2022-05-10
------------------
Added
~~~~~

* Data Integration service

  * Support for BIP connection in the following commands

    * ``oci data-integration connection create-connection-create-connection-from-bip``
    * ``oci data-integration connection-validation create-connection-validation-create-connection-from-bip``

  * New parameters --conditional-composite-field-map, --is-single-load and --parallel-load-limit for the below commands

    * ``oci data-integration task create-data-loader-task --conditional-composite-field-map --is-single-load --parallel-load-limit``
    * ``oci data-integration task update-data-loader-task --conditional-composite-field-map --is-single-load --parallel-load-limit``


Changed
~~~~~~~
* Rover service

  * [BREAKING] Parameters --compartment-id and --bucket-id for add-workload operations for node and cluster are being deleted

    * ``oci rover node add-workload``
    * ``oci rover standalone-cluster add-workload``
    * ``oci rover station-cluster add-workload``


3.8.1 - 2022-05-03
------------------
Added
~~~~~
* Support for Application Dependency Management service

  * ``oci adm``

* Support for provisioned concurrency in the Functions service

  * ``oci fn function create --provisioned-concurrency``
  * ``oci fn function update --provisioned-concurrency``

* Support for allow reboot migration for DenseIO shape in maintenance situations in Compute service

  * ``oci compute instance instance-action-reset-action-details``
  * ``oci compute instance instance-action-soft-reset-action-details``

3.8.0 - 2022-04-26
------------------
Added
~~~~~
* Support for the Service Mesh service

  * ``oci service-mesh``

* Big Data service

  * Support for compute only worker nodes

    * ``oci bds instance remove  --node-id``
    * ``oci bds instance remove  --node-id --is-force-remove-enabled``

  * Support for horizontal autoscaling policy

    * ``oci bds auto-scale-config create --policy-details``
    * ``oci bds auto-scale-config edit --policy-details``

  * Support for bootstrap script

    * ``oci bds instance create --bootstrap-script-url``
    * ``oci bds instance update --bootstrap-script-url``

  * Support for customizable kerberos realm name

    * ``oci bds instance create --kerberos-realm-name``

  * Support for ODH patch patch management

    * ``oci bds instance install-patch``
    * ``oci bds instance list-patch-histories``
    * ``oci bds instance list-patches``

* Rover service

  * [BREAKING] Support for required shape parameter to the creation of a roving edge node

    * ``oci rover node create --shape``

  * Support to list the available shapes for Rover

    * ``oci rover shape list --compartment-id``

  * Support the option for the user to provide their own master key OCID to encrypt secret data to roving edge nodes, standalone clusters and station clusters.

    * ``oci rover node create --master-key-id --policy-compartment-id --policy-name``
    * ``oci rover standalone-cluster --master-key-id --policy-compartment-id --policy-name``
    * ``oci rover station-cluster --master-key-id``

  * Support to create the master key policy with required parameter master-key-id and optional parameters policy-compartment-id and policy-name

    * ``oci rover create-master-key-policy --master-key-id --policy-compartment-id --policy-name``

* APM Synthetics service

  * Support for create/update/delete of dedicated-vantage-points

    * ``oci apm-synthetics dedicated-vantage-point``

  * Support for list of dedicated-vantage-points

    * ``oci apm-synthetics dedicated-vantage-point-collection list-dedicated-vantage-points``

* Support for Additional Transcription Format (SRT) and Punctuation in the Speech service

  * ``oci speech transcription-job create --additional-transcription-formats``

* Support for cost management schedule in the Usage service

  * ``oci usage-api schedule``
  * ``oci usage-api scheduled-run``

* Support for Security Zone in the Cloud Guard service

  * ``oci cloud-guard security-zone``
  * ``oci cloud-guard security-policy``

* Support for creating budgets that target subscriptions and child tenancies

  * ``oci budgets budget create --processing-period-type``

* Support for Virtual Test Access Point (VTAP) feature as a part of the vcn service

  * ``oci network vtap``
  * ``oci network capture-filter``

* Support to reactive child tenancy in the Organizations service

  * ``oci organizations organization-tenancy restore --organization-tenancy-id``


Fixed
~~~~~~~
* Bug in --wait-for-state param for following commands in the Database service

  * ``oci db data-guard-association switchover``
  * ``oci db data-guard-association failover``
  * ``oci db data-guard-association reinstate``

Changed
~~~~~~~
* [BREAKING] --subscription-id is now required in the below command in the Organization service

  * ``oci organizations subscription-mapping list --subscription-id``

3.7.3 - 2022-04-19
------------------
Added
~~~~~

* Support for choosing compute shapes when creating SDDCs and ESXi hosts in the VMWare Solution service

  * ``oci ocvs esxi-host create --host-ocpu-count, --host-shape-name``
  * ``oci ocvs sddc create --initial-host-ocpu-count, --initial-host-shape-name``

* Database service

    * Support for stack monitoring on external databases

      * ``oci db external-cdb disable-external-container-database-stack-monitoring``
      * ``oci db external-cdb enable-external-container-database-stack-monitoring``
      * ``oci db external-non-cdb disable-external-non-container-database-stack-monitoring``
      * ``oci db external-non-cdb enable-external-non-container-database-stack-monitoring``
      * ``oci db external-pdb disable-external-pluggable-database-stack-monitoring``
      * ``oci db external-pdb enable-external-pluggable-database-stack-monitoring``

    * Support for upgrading VM database systems in place

      * ``oci db system upgrade``
      * ``oci db db-system-upgrade-history get``
      * ``oci db db-system-upgrade-history list``

* Support for the Stack Monitoring service

  * ``oci stack-monitoring``

3.7.2 - 2022-04-12
------------------
Added
~~~~~

* Database service

  * Support for enabling and disabling data collection options during create and update operations on VM clusters on Exadata Cloud

    * ``oci db vm-cluster create --data-collection-options ``
    * ``oci db vm-cluster update --data-collection-options ``

  * Support for new fields --database-edition and --max-cpu-core-count to create and update an autonomous database

    * ``oci db autonomous-database create --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-adb-cross-region-data-guard-details --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-from-backup-id --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-from-backup-timestamp --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-from-clone --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-refreshable-clone --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database create-virtual-clone --database-edition, --max-cpu-core-count``
    * ``oci db autonomous-database update --database-edition, --max-cpu-core-count``

* Network service

  * Support for using Ipv6 cidr block in the below commands

    * ``oci network byoip-range create --ipv6-cidr-block``
    * ``oci network subnet create --ipv6-cidr-blocks``
    * ``oci network subnet update --ipv6-cidr-blocks``
    * ``oci network subnet add-ipv6-subnet-cidr``
    * ``oci network subnet remove-ipv6-subnet-cidr``
    * ``oci network vcn add-ipv6-vcn-cidr``
    * ``oci network vcn remove-ipv6-vcn-cidr``
    * ``oci network vnic assign-ipv6 --ipv6-subnet-cidr``

  * Support for the parameters --ipv6-private-cidr-block, --is-oracle-gua-allocation-enabled, --byoipv6-cidr-detail in the below command

    * ``oci network vcn create --byoipv6-cidr-details, --is-oracle-gua-allocation-enabled, --ipv6-private-cidr-blocks``

Changed
~~~~~

* Parameter --cidr-block has been made optional in the Network service

  * ``oci network byoip-range create --cidr-block``

3.7.1 - 2022-04-05
------------------

Added
~~~~~

* Support viewing top process analytics in the Operations Insights service

  * ``oci opsi host-insights summarize-top-processes-usage-trend``

* Support for creating Enterprise Manager-based zLinux host targets for ``--platform-type`` in the Operations Insights service

  * ``oci opsi host-insights list --platform-type``


3.7.0 - 2022-03-29
------------------
Added
~~~~~

* Support for --type-key on entities, attributes, and folders in the Data Catalog service

  * ``oci data-catalog attribute create --type-key``
  * ``oci data-catalog folder create --type-key``

* DevOps service

  * Support for the below commands

    * ``oci devops repository get-repo-file-diff``
    * ``oci devops repository get-repo-file-lines``

  * Support for blue green and canary stages and single stage redeployment

    * oci devops deploy-stage create-deploy-compute-instance-group-blue-green-stage
    * oci devops deploy-stage create-compute-instance-group-blue-green-traffic-shift-stage
    * oci devops deploy-stage create-deploy-compute-instance-group-canary-stage
    * oci devops deploy-stage create-compute-instance-group-canary-traffic-shift-stage
    * oci devops deploy-stage create-compute-instance-group-canary-approval-stage
    * oci devops deployment create-single-stage-redeployment
    * oci devops deploy-stage update-deploy-compute-instance-group-blue-green-stage
    * oci devops deploy-stage update-compute-instance-group-blue-green-traffic-shift-stage
    * oci devops deploy-stage update-deploy-compute-instance-group-canary-stage
    * oci devops deploy-stage update-compute-instance-group-canary-traffic-shift-stage
    * oci devops deploy-stage update-compute-instance-group-canary-approval-stage
    * oci devops deployment update-single-stage-redeployment

  * Support for optional parameter --network-channel to support private oke cluster

    * ``oci devops deploy-environment create-oke-cluster-environment --network-channel``
    * ``oci devops deploy-environment update-oke-cluster-environment --network-channel``

* Support for new parameters``--bgp-admin-state`` and ``--is-bfd-enabled`` in the Networking service.

  * ``oci network virtual-circuit create --bgp-admin-state --is-bfd-enabled``
  * ``oci network virtual-circuit update --bgp-admin-state --is-bfd-enabled``

* Java Management service

  * Support for listing and removing of Java Runtime installations

    * ``oci jms installation-site-summary list-installation-sites``
    * ``oci jms installation-site-summary remove``

  * Support for work request detail status of LCM operation.

    * ``oci jms work-item-summary list-work-items --work-request-id``
    * ``oci jms work-request cancel --work-request-id``

  * Support for JMS blocklist

    * ``oci jms blocklist create``
    * ``oci jms blocklist delete``
    * ``oci jms blocklist list``

  * Support for listing work requests in a fleet.

    * ``oci jms work-request list --fleet-id``

  * Support for Fleets to use custom logs for inventory and operation

    * ``oci jms fleet create --inventory-log --operation-log``
    * ``oci jms fleet update --inventory-log --operation-log``

Changed
~~~~~~~~~

* DevOps service

  * [BREAKING] Optional parameter --repository-type has been made required

    * oci devops repository create --repository-type

3.6.2 - 2022-03-22
------------------
Added
~~~~~

* Support for virtual machines, bare metal machines, and Exadata databases with private endpoints in the Operations Insights service

  * ``oci opsi opsi-private-endpoint``
  * ``oci opsi database-insights change-pe-comanaged-database-detail``

* Support for setting deletion policies on database systems in the MySQL Database service

  * ``oci mysql db-system clone--deletion-policy``
  * ``oci mysql db-system create --deletion-policy``
  * ``oci mysql db-system import --deletion-policy``
  * ``oci mysql db-system update --deletion-policy``

Changed
~~~~~~~~

* Changed existing database insight operations updated in the Operations Insights service

  * ``oci opsi database-insights create-pe-comanged-database``
  * ``oci opsi database-insights enable-pe-comanaged-database``
  * ``oci opsi database-insights update-pe-comanaged-database``


3.6.1 - 2022-03-15
------------------
Added
~~~~~

* Support for DI application resource in the Data Integration service

  * ``oci data-integration dis-application``

* Support for enabling shielded instances feature in create SDDC in the Oracle Cloud VMware Solution service

  * ``oci ocvs sddc create --is-shielded-instance-enabled``

* Vulnerability Scanning Service

  * Support for Optional param ``--image-count`` in container scan recipe create and update

    * ``oci vulnerability-scanning container scan recipe create --image-count``
    * ``oci vulnerability-scanning container scan recipe update --image-count``

  * Support for vulnerabilities list and get

    * ``oci vulnerability-scanning vulnerability get``
    * ``oci vulnerability-scanning vulnerability list``
    * ``oci vulnerability-scanning vulnerability list-vulnerability-impacted-containers``
    * ``oci vulnerability-scanning vulnerability list-vulnerability-impacted-hosts``

* Support for Custom Maintenance Schedule for AVM clusters on ExaCC Infrastructure in the Database service

    * ``oci db autonomous-vm-cluster create --autonomous-data-storage-size-in-tbs, --cpu-core-count-per-node, --maintenance-window-details, --memory-per-oracle-compute-unit-in-gbs, --total-container-databases``
    * ``oci db autonomous-vm-cluster update --maintenance-window-details``

* Support for the following parameters -defined-tags, --display-name, --freeform-tags for the below commands in the Data Integration service

  * ``oci data-integration application create --defined-tags, --display-name, --freeform-tags``
  * ``oci data-integration application update --defined-tags, --display-name, --freeform-tags``

Changed
~~~~~~~

* Complex param --input-ports,--output-port have been updated for below commands in the Data Integration service

  * ``oci data-integration task create-task-from-rest-task --auth-config, --poll-rest-call-config, --typed-expressions``
  * ``oci data-integration task update-task-from-rest-task --auth-config, --poll-rest-call-config, --typed-expressions``

* Updated the help text for creating an Autonomous Database Data Guard standby to be more descriptive and have better examples

  * ``create-adb-cross-region-data-guard-details``

3.6.0 - 2022-03-08
------------------
Added
~~~~~
* Support for the Sales Accelerator license option in the Content Management service

  * ``oci oce oce-instance create --add-on-features``
  * ``oci oce oce-instance update --add-on-features``

* Support for new VCN hostname cluster endpoint as part of Container Engine service

  * ``oci ce cluster create-kubeconfig --kube-endpoint VCN_HOSTNAME``

* Database Migration service

  * Support for reporting all excluded objects based on static exclusion rules and dynamic exclusion settings configured by the Database Migration Service (DMS) user

    * ``oci database-migration excluded-object-summary list``

  * Support to remove, list, and add database objects reported by the Cloud Premigration Advisor Tool (CPAT)

    * ``oci database-migration migration add``
    * ``oci database-migration migration remove``
    * ``oci database-migration migration-objects list``

  * Support for migrating Oracle Database from Amazon Web Services (AWS) RDS to Oracle Autonomous Database (ADB) using Amazon Simple Storage Service (Amazon S3) and DBLINK for data transfer

    * ``oci database-migration connection create --db-subtype``

* Enhancement in launch dbsystem as well as create database using customer managed keys for VMBM in the Database service

  * ``oci db system launch --vault-id``
  * ``oci db database create --vault-id``
  * ``oci db database migrate-vault-key --vault-id --admin-password --tde-wallet-password``

Changed
~~~~~~~

* The parameters --admin-username and --admin-password are now optional in the below commands in the MySQL database service

  * ``oci mysql db-system clone``
  * ``oci mysql db-system create``
  * ``oci mysql db-system import``

* [BREAKING] The command ``oci rover cluster`` is being deleted and its logic has been divided in to the newly created commands below in the Roving Edge Infrastructure Service

  * ``oci rover station-cluster``

  * ``oci rover standalone-cluster``

3.5.3 - 2022-03-01
------------------
Added
~~~~~
* Support for managed egress via a default networking option on jobs and notebooks in the Data Science service

  * ``oci data-science``

* Networking service

  * Support for DRG route distribution statements to be specified with a new match type 'MATCH_ALL' for matching criteria

    * ``oci network drg-route-distribution-statement add --statements '[{"matchCriteria":[{"matchType": "MATCH_ALL"}],"action": "ACCEPT","priority": 1}]' --route-distribution-id "id-example"``

  * Support for VCN route types on DRG attachments for deciding whether to import VCN CIDRs or subnet CIDRs into route rules

    * ``oci network drg-attachment create --drg-id "example-drg-id" --network-details '{"type":"VCN","id":"example-vcn-id","vcnRouteType":"VCN_CIDRS"}'``


* Database service

  * Support for CPS offline reports in the Database service

    * ``oci db exadata-infrastructure create --is-cps-offline-report-enabled``
    * ``oci db exadata-infrastructure update --is-cps-offline-report-enabled``

  * Support for infrastructure patching v2 features

    * ``oci db maintenance-run update --current-custom-action-timeout-in-mins, --custom-action-timeout-in-mins, --is-custom-action-timeout-enabled, --is-resume-patching``

  * Support for Autonomous Database Create with Auto Scaling Storage via a new parameter (is-auto-scaling-for-storage-enabled)

    * ``oci db autonomous-database create --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-adb-cross-region-data-guard-details --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-from-backup-id --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-from-backup-timestamp --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-from-clone --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-refreshable-clone --is-auto-scaling-for-storage-enabled``
    * ``oci db autonomous-database create-virtual-clone --is-auto-scaling-for-storage-enabled``

  * Support for Autonomous Database Update for Auto Scaling Storage via a new parameter (is-auto-scaling-for-storage-enabled)

    * ``oci db autonomous-database update --is-auto-scaling-for-storage-enabled``

  * Support for shrinking an Autonomous Database

    * ``oci db autonomous-database shrink --autonomous-database-id``

Changed
~~~~~~~

* Upgraded third party module cx_Oracle version to 8.3 to provide support for python 3.8

* Updated docs for ``oci iam db-token get``

3.5.2 - 2022-02-22
------------------
Added
~~~~~

* Support for Speech Service

  * ``oci speech``

* Support for Data Connectivity Management Service

  * ``oci data-connectivity``

* Support for Resource Profile, Sightings, Tactics, and Technique features as a part of the Cloud Guard Service

  * ``oci cloud-guard problem-endpoint-summary list-problem-endpoints``
  * ``oci cloud-guard resource-risk-score-aggregation request-summarized-trend-resource-risk-scores``
  * ``oci cloud-guard resource-profile get``
  * ``oci cloud-guard resource-profile-endpoint-summary list-resource-profile-endpoints``
  * ``oci cloud-guard resource-profile-impacted-resource-summary list-resource-profile-impacted-resources``
  * ``oci cloud-guard resource-profile-risk-score-aggregation-summary request-summarized-top-trend-resource-profile-risk-scores``
  * ``oci cloud-guard resource-profile-summary list-resource-profiles``
  * ``oci cloud-guard resource-type-summary list-resource-types``
  * ``oci cloud-guard sighting get``
  * ``oci cloud-guard sighting-endpoint-summary list-sighting-endpoints``
  * ``oci cloud-guard sighting-impacted-resource-summary list-sighting-impacted-resources``
  * ``oci cloud-guard sighting-summary list-sightings``
  * ``oci cloud-guard tactic-summary list-tactics``
  * ``oci cloud-guard technique-summary list-techniques``

* Support for disabling crash recovery to improve the performance of large imports in the MySql Database service.

  * ``oci mysql db-system clone --crash-recovery``
  * ``oci mysql db-system create --crash-recovery``
  * ``oci mysql db-system import --crash-recovery``
  * ``oci mysql db-system update --crash-recovery``

* Support for customer managed encryption keys for secrets stored in Analytics service

  * ``oci analytics analytics-instance set-kms-key``

* Support for option --kms-key-id to specify customer managed vault key ocid when creating an instance in the Analytics service

  * ``oci analytics analytics-instance create --kms-key-id``

Fixed
~~~~~~~

* Bug in the object storage sync in windows which deletes unexpected local subfolders `github issue #502 <https://github.com/oracle/oci-cli/issues/502>`_

3.5.1 - 2022-02-15
------------------
Added
~~~~~
* Support for the AI Vision service

  * ``oci ai-vision``

* Support for the Threat Intelligence service

  * ``oci threat-intelligence``

* Support for creation of NoSQL database tables with on-demand throughput capacity in the NoSQL Database Cloud service

  * New optional property ``capacityMode`` in ``oci nosql table create --table-limits`` parameter

* Support for trace snapshots in the Application Performance Monitoring service

  * ``oci apm-traces trace aggregated-snapshot get``

* Support for auditing and alerts in the Data Safe service

  * ``oci data-safe alert update``

* Support for data discovery and data masking in the Data Safe service

  * ``oci data-safe alert-policy-rule-collection list-alert-policy-rules``
  * ``oci data-safe audit-profile discover-audit-trails``
  * ``oci data-safe audit-profile-collection list-audit-profiles --audit-collected-volume-greater-than-or-equal-to``
  * ``oci data-safe report-definition generate-report``

* Support for documentation for pagination support in Logging Search service

  * ``oci logging-search search-logs``

* Support for Announcements Subscriptions feature

  * ``oci announce announcement-subscription change-compartment``
  * ``oci announce announcement-subscription create``
  * ``oci announce announcement-subscription create-filter-group``
  * ``oci announce announcement-subscription delete``
  * ``oci announce announcement-subscription delete-filter-group``
  * ``oci announce announcement-subscription get``
  * ``oci announce announcement-subscription list``
  * ``oci announce announcement-subscription update-filter-group``

3.5.0 - 2022-02-08
------------------
Added
~~~~~

* Support for listing fast launch job configs in the Data Science service

  * ``oci data-science fast-launch-job-config list``

* Support for Subscription endpoints to Upgrade and Manage Payment feature in the OSP Gateway service

  * ``oci osp-gateway subscription-service subscription``

* Support for --is-highly-available for clone and update db-system in the MySQL Database service

  * ``oci mysql db-system clone --is-highly-available``
  * ``oci mysql db-system update --is-highly-available``

* Support for Storage Management in the Database Management service

  * ``oci database-management tablespace``
  * ``oci database-management managed-database list-asm-properties``

Changed
~~~~~

* [BREAKING] the command ``oci osp-gateway invoice`` has been changed to ``oci osp-gateway invoice-service invoice`` in the OSP Gateway service

3.4.5 - 2022-02-01
------------------
Added
~~~~~
* Support for the Console Dashboard service

  * ``oci dashboard-service dashboard-group``
  * ``oci dashboard-service dashboard``

* Support for fetching listings by image OCID in the Marketplace service

  * ``oci marketplace listing list --image-id``

* Container Engine for Kubernetes (OKE) Service

    * Support for capacity reservation

      * ``oci ce node-pool create --placement-configs``
      * ``oci ce node-pool update --placement-configs``

    * Support for Tagging features

      * ``oci ce cluster create --defined-tags, --freeform-tags  --persistent-volume-defined-tags, --persistent-volume-freeform-tags, --service-lb-defined-tags, --service-lb-freeform-tags``
      * ``oci ce cluster update --defined-tags, --freeform-tags``
      * ``oci ce node-pool create --defined-tags, --freeform-tags, --node-defined-tags, --node-freeform-tags``
      * ``oci ce node-pool update --defined-tags, --freeform-tags, --node-defined-tags, --node-freeform-tags``

3.4.4 - 2022-01-25
------------------
Added
~~~~~

* Below services were added to support the Account Management finance data

  * One Subscription Billing Schedule service

    * ``oci osub-billing-schedule billing-schedule-summary``

  * One Subscription Subscription service

    * ``oci osub-subscription commitment``
    * ``oci osub-subscription ratecard``
    * ``oci osub-subscription subscription``

  * One Subscription Usage service

    * ``oci osub-usage computed-usage``
    * ``oci osub-usage computed-usage-aggregated-summary``

  * One Subscription Organization subscription service

    * ``oci osub-organization-subscription subscription``

* Support for new field 'type' to specify if a run or application is streaming or batch in the Data Flow service

  * ``oci data-flow application create --type``
  * ``oci data-flow run create --type``
  * ``oci data-flow run submit --type``

3.4.3 - 2022-01-18
------------------
Added
~~~~~
* Support for calling Oracle Cloud Infrastructure services in the me-dcc-muscat-1 region

* Support for the Visual Builder service

    * ``oci visual-builder``

* Support for cross-region replication of volume groups in the Block Storage service

    * ``oci bv volume-group create --volume-group-replicas``
    * ``oci bv volume-group update  --volume-group-replicas``

* Support for boot volume encryption in the Container Engine for Kubernetes service

    * ``oci ce node-pool create --is-pv-encryption-in-transit-enabled, --kms-key-id``
    * ``oci ce node-pool update  --is-pv-encryption-in-transit-enabled, --kms-key-id``

* Support for adding metadata to records when creating and updating records in the Data Labeling service

    * ``oci data-labeling-service-dataplane record``

* Support for global export formats in snapshot datasets in the Data Labeling service

    * ``oci data-labeling-service dataset snapshot --export-format``
    * ``oci data-labeling-service dataset update --labeling-instructions``

* Support for adding labeling instructions to datasets in the Data Labeling service

    * ``oci data-labeling-service dataset create --labeling-instructions``
    * ``oci data-labeling-service dataset update --labeling-instructions``

* Support for updating autonomous dataguard associations for autonomous container databases in the Database service

    * ``oci db autonomous-container-database-dataguard update``

* Support for setting up automatic failover when creating autonomous container databases in the Database service

    * ``oci db autonomous-container-database create --is-automatic-failover-enabled``

* Support for setting the RECO storage size when updating a database system in the Database service

    * ``oci db system update --reco-storage-size-in-gbs``

* Support for reconnecting refreshable clones to source for autonomous databases on shared infrastructure in the Database service

    * ``oci db autonomous-database update --is-refreshable-clone true``

* Support for checking if an autonomous database on shared infrastructure can be reconnected to source, in the Database service

    * ``oci db autonomous-database get --autonomous-database-id <ocid>``

3.4.2 - 2022-01-11
------------------
Added
~~~~~
* Network Load Balancer service

  * Support for Multiple Protocols on the Same Listener of the Network Load Balancer.

    * ``oci nlb listener create --protocol``
    * ``oci nlb listener create --protocol``

  * Support for IPv6 in the below commands

    * ``oci nlb backend-set create --ip-version``
    * ``oci nlb backend-set update --ip-version``
    * ``oci nlb listener create --ip-version``
    * ``oci nlb listener update --ip-version``
    * ``oci nlb network-load-balancer create --nlb-ip-version``
    * ``oci nlb network-load-balancer update --nlb-ip-version``

* Support for creating Enterprise Manager-based Solaris/SunOS Host targets in the Operations Insights service

  * ``oci opsi host-insights``

* More information related to the user system in the --debug option

* Improvement to the OCI CLI service error exception message

Fixed
~~~~~~~

* Removed python install by source in install.sh script for Oracle Linux 7

* While creating iam db-token, persist private key only when request is successful

    * ``oci iam db-token get``

3.4.1 - 2021-12-21
------------------
Fixed
~~~~~
* Bug when using ``oci os object put`` from STDIN. Please see `github issue #490 <https://github.com/oracle/oci-cli/issues/490>`_ for more details.


3.4.0 - 2021-12-14
------------------

* Support for node replacement in the VMWare Solution service
  
  * ``oci ocvs esxi-host create --failed-esxi-host-id`` 

* Support for ingestion of SQL stats metrics in the Operations Insights service
  
  * ``oci opsi database-insights ingest-sql-stats --database-id``
    
* Support for AWR hub integration in the Operations Insights service
  
  * ``oci opsi awr-hubs``
  * ``oci opsi operations-insights-warehouse-users``
  * ``oci opsi operations-insights-warehouses``

* Support for automatically generating logical entities from filename patterns and relationships between business terms across glossaries in the Data Catalog service

  * ``oci data-catalog pattern create --file-path-prefix``
  * ``oci data-catalog pattern update --file-path-prefix``
  * ``oci data-catalog pattern validate --file-path-prefix``
  * ``oci data-catalog entity list-aggregated-physical --is-include-properties``
  * ``oci data-catalog entity create --type-key``
  
* Support for automatic start/stop at scheduled times in the Database service
  
  * Option ``--scheduled-operations`` for the following operations under ``oci db autonomous-database``:  ``create, create-adb-cross-region-data-guard-details, create-from-backup-id, create-from-backup-timestamp, create-from-clone, create-refreshable-clone, update``

* Support for cloud VM cluster resources on autonomous dedicated databases in the Database service
  
  * ``oci db autonomous-container-database create  --cloud-autonomous-vm-cluster-id --peer-cloud-autonomous-vm-cluster-id``
  * ``oci db autonomous-container-database list --cloud-autonomous-vm-cluster-id``
  * ``oci db cloud-autonomous-vm-cluster``
  * ``oci db cloud-vm-cluster create | update --ocpu-count``
  * ``oci db vm-cluster create | udpate --data-storage-size-in-gbs --ocpu-count``

* Support for external Hive metastores in the Big Data service
  
  * ``oci bds bds-metastore-configuration``

* [Breaking] Support for batch detection/inference in the AI Language service
  
  * ``oci ai language batch*``

* Support for invoice operations in the Account Management service
  
  * ``oci osp-gateway``

* Support for custom CA trust stores in the API Gateway service
  
  * ``oci api-gateway gateway create --ca-bundles``
  * ``oci api-gateway gateway update --ca-bundles`` 
    
* Support for generating scoped database token to be used to authorize Identity Service users to OCI database services
  
  * ``oci iam db-token get`` 

* Support for database passwords for users, for logging into database accounts, in the Identity service
  
  * ``oci iam user create-db-credential``
  * ``oci iam user delete-db-credential``
  * ``oci iam user list-db-credentials``
  * ``oci iam user update --db-user-name``
  * ``oci iam user update-user-capabilities --can-use-db-credentials``


3.3.3 - 2021-12-07
------------------
Added
~~~~~

* Support for Resource Discovery and Monitoring service

  * ``oci appmgmt-control``

* Support for finding and listing locations of all default OCI CLI installs.

  * ``oci setup find-installations``

* Support for the following in the Log Analytics service

  * Log analytics categories

    * ``oci log-analytics category``

  * List entity topology

    * ``oci log-analytics entity-topology list``

  * Verify Scheduled Task

    * ``oci log-analytics scheduled-task verify``

* Support for the following in the Java Management service

  * Retrieve the inventory of JMS resources in the specified compartment.

    * ``oci jms fleet summarize-resource-inventory --compartment-id``

  * List Java Runtime usage in a specified host filtered by query parameters.

    * ``oci jms jre-usage list --compartment-id --host-id``

* Support for RAC Databases in GoldenGate Service

  * ``oci goldengate database-registration create --session-mode``
  * ``oci goldengate database-registration update --session-mode``

Changed
~~~~~~~~~

* New parameter for listing Java Runtime usage in a fleet.

  * ``oci jms jre-usage summarize --jre-security-status``

Fixed
~~~~~~~

* Bug while upgrading OCI CLI autocomplete

  * ``oci setup autocomplete``

3.3.2 - 2021-11-30
------------------
Added
~~~~~

* Support for custom IPSecConnection Tunnel Internet Key Exchange phase 1 and phase 2 encryption algorithms in the Network service

  * ``oci network allowed-ike-ip-sec-parameters get``
  * ``oci network ip-sec-connection-tunnel-error-details get-ip-sec-connection-tunnel-error``
  * ``oci network tunnel-route list-ip-sec-connection``
  * ``oci network tunnel-security-association list-ip-sec-connection``

* Database Management service

  * Support for listing and retrieving user details

    * ``oci database-management managed-database list-users``
    * ``oci database-management managed-database get-user``
    * ``oci database-management managed-database list-roles``
    * ``oci database-management managed-database list-system-privileges``
    * ``oci database-management managed-database list-object-privileges``
    * ``oci database-management managed-database list-consumer-group-privileges``
    * ``oci database-management managed-database list-proxy-users``
    * ``oci database-management managed-database list-proxied-for-users``
    * ``oci database-management managed-database list-data-access-containers``

  * Support for SQL Tuning Advisors

    * ``oci database-management sql-tuning-task``

* Support for enabling and disabling Database Management features in the Autonomous Database service

  * ``oci db autonomous-database enable-autonomous-database-management``
  * ``oci db autonomous-database disable-autonomous-database-management``

* Support for listing and retrieving deployment backups in the GoldenGate service

  * ``oci goldengate deployment-backup list``
  * ``oci goldengate deployment-backup get``

* Support for standard tags in the Identity service

  * ``oci iam tag import-standard-tags``
  * ``oci iam tag get-standard-tag-template``
  * ``oci iam tag list-standard-tag-namespaces``

* Support for Solaris platform in the Management Agent service

  * ``oci management-agent agent list --platform-type SOLARIS``
  * ``oci management-agent plugin list --platform-type SOLARIS``

* Support for cross-compartment support in the Operations Insights service

  * ``oci opsi <group> <command> --compartment-id-in-subtree``

* Support for pagination when listing work requests and new lifecycle state `DELETED` in the APM service

  * ``oci apm-control-plane work-request list-apm-domain --limit, --page``
  * ``oci apm-control-plane apm-domain list --lifecycle-state DELETED``

* Support for fetching problems for `DELETED` targets in the Cloud Guard service

  * ``oci cloud-guard problem update-bulk-problem-status --status DELETED``
  * ``oci cloud-guard problem update-problem-status --status DELETED``
  * ``oci cloud-guard problem list --status DELETED``

* Support for upgrading a platform instance and choosing version when creating a platform instance in the Blockchain service

  * ``oci blockchain blockchain-platform upgrade``
  * ``oci blockchain blockchain-platform create --platform-version``

Fixed
~~~~~
* Bug when using the install script with both --optional-features and --oci-cli-version parameters. Please see `github issue #370 <https://github.com/oracle/oci-cli/issues/370>`_ for more details.

3.3.1 - 2021-11-17
------------------
Added
~~~~~

* Support for Object Storage integration with the Big Data service

  * ``oci bds bds-api-key``

* Support for the GetSubnetTopology API in the Networking Topology Service

  * ``oci network subnet-topology get``

* Support for Cloud Advisor V2 features as a part of the Cloud Advisor Service

  * ``oci optimizer profile-level-summary list-profile-levels``
  * ``oci optimizer queryable-field-summary list-resource-action-queryable-fields``
  * ``oci optimizer resource-action-summary filter-resource-actions``

* FastConnect Service

  * Support for MACSEC in the below commands

    * ``oci network cross-connect create --macsec-properties``
    * ``oci network cross-connect update --macsec-properties``
    * ``oci network cross-connect-group create --macsec-properties``
    * ``oci network cross-connect-group update --macsec-properties``

  * Support for MTU in the below commands

    * ``oci network virtual-circuit create --ip-mtu``
    * ``oci network virtual-circuit update --ip-mtu``

* Support for Service Manager Proxy aimed at having SaaS environments that implement Service Manager API contract.

  * ``oci service-manager-proxy service-environment``

Changed
~~~~~~~

* Database service

  * The required parameter --backup-tde-password is now optional in the below commands

    * ``oci db database create-from-backup``
    * ``oci db database create-from-database``


  * The parameter --backup-tde-password is now optional in the below commands

    * ``oci db system launch-from-backup``
    * ``oci db database launch-from-database``


  * The parameters --pdb-admin-password, --tde-wallet-password and --target-tde-wallet-password are now optional and a new parameter --is-pdb-admin-acc-locked is introduced in the below commands

    * ``oci db pluggable-database create``
    * ``oci db pluggable-database local-clone``
    * ``oci db pluggable-database remote-clone``


3.3.0 - 2021-11-09
------------------
Added
~~~~~

* Support for Drilldown configuration in the Management Dashboard service
  
  * ``oci management-dashboard dashboard create | update --drilldown-config``
  * ``oci management-dashboard saved-search create | update --drilldown-config``

* Support for Autonomous Database Dedicated on Cloud at Customer Infrastructure in the Operator Access Control Service

  * ``oci opctl access-request approve --time-of-user-creation``
  * ``oci opctl access-request list --resource-type, --time-end, --time-start``
  * ``oci opctl access-request review``
  * ``oci opctl operator-action list --resource-type``
  * ``oci opctl operator-control create --resource-type``
  * ``oci opctl operator-control list  --resource-type``
  * ``oci opctl operator-control-assignment create --is-auto-approve-during-maintenance --is-log-forwarded --remote-syslog-server-address --remote-syslog-server-ca-cert --remote-syslog-server-port``
  * ``oci opctl operator-control-assignment list  --resource-type``
  * ``oci opctl operator-control-assignment update --resource-type --is-auto-approve-during-maintenance --is-log-forwarded --remote-syslog-server-address --remote-syslog-server-ca-cert --remote-syslog-server-port``
  * [Breaking] Fields ``--approver-groups-list``, ``--is-fully-pre-approved`` are now required for ``oci opctl operator-control create``
  * [Breaking] Field ``--is-enforced-always`` is now required for ``oci opctl operator-control-assignment update``
  * [Breaking] Fields ``--approver-groups-list``, ``--is-fully-pre-approved``, ``--operator-control-name`` are now required for ``oci opctl operator-control update``
  * [Breaking] Fields ``--is-enforced-always``, ``--resource-type`` are now required for ``oci opctl operator-control-assignment create``

* Support for verifying the checksum for the python installer script from within the shell and powershell installer scripts

3.2.2 - 2021-11-02
------------------
Added
~~~~~

* Support for Domains in the Identity Service 

  * ``oci iam domain`` 

* Support for redeemable user and support rewards in the Usage Service
 
  * ``oci usage monthly-reward-summary list-rewards``
  * ``oci usage product-summary list-products``
  * ``oci usage redeemable-user create``
  * ``oci usage redeemable-user delete``
  * ``oci usage redeemable-user-summary list-redeemable-users``

* Support for the Database Tools service

  * ``oci dbtools``

* Support for scan listener port TCP and TCP SSL on cloud VM clusters in the Database service
  
  * ``oci db cloud-vm-cluster create --scan-listener-port-tcp --scan-listener-port-tcp-ssl`` 

* Support for user-defined functions and libraries, as well as scheduling and orchestration, in the Data Integration service

  * ``oci data-integration user-defined-function``
  * ``oci data-integration user-defined-function-validation``
  * ``oci data-integration schedule create-custom-frequency | create-monthly-rule-frequency | create-weekly-frequency``
  * ``oci data-integration schedule update-custom-frequency | update-monthly-rule-frequency | update-weekly-frequency``
  * ``oci data-integration function-library``
  * ``oci data-integration data-entity create-entity-shape-from-sql`` 

* Support for calling Oracle Cloud Infrastructure services in the Singapore (``--region ap-singapore-1``) and Marseille (``--region eu-marseille-1``) regions

Changed
~~~~~~~

* Endpoint for Identity service changed to include ".oci" subdomain

* Handle merge case when empty contexts/clusters/users is null and not empty string in the Container Engine commands

* Version checks in install.sh and install.py 


3.2.1 - 2021-10-26
------------------
Added
~~~~~
* Support for OCI Certificates service

  * ``oci certs-mgmt``
  * ``oci certificates``

* Support for the following features in Devops service

  * Support for build services

    * ``oci devops build-pipeline``
    * ``oci devops build-run``
    * ``oci devops connection``

  * Support for creating and managing repositories and triggers

    * ``oci devops repository``
    * ``oci devops trigger``

* Support for creating child tenancies and managing subscription in Organizations service

  * ``oci organizations organization``
  * ``oci organizations organization-tenancy``
  * ``oci organizations child-tenancy``
  * ``oci organizations assigned-subscription``
  * ``oci organizations subscription-mapping``
  * ``oci organizations subscription``

* Support for the following features in Operations Insights service

  * Support for resource lifecycle operations on Enterprise Manager-based Exadata targets and capacity analytics

    * ``oci opsi exadata-insights``

  * Support for creating Enterprise Manager-based Host targets

    * ``oci opsi host-insights create-em-external-host``

* Support for creating esxi-hosts outside of the same AD in Oracle Cloud VMWare Solution service

  * ``oci ocvs esxi-host create --compute-availability-domain``


3.2.0 - 2021-10-19
------------------
Added
~~~~~
* Support for Node subsetting feature for vmcluster resources for ExaCC in Database Service

  * ``oci db vm-cluster add --db-servers``
  * ``oci db vm-cluster create --db-servers``
  * ``oci db vm-cluster remove --db-servers``

* Support for convert to pdb, rollback, sync, sync-rollback, list-pdb-conversion-history, get-pdb-conversion-history in Database Service

  * ``oci db database convert-to-new-pdb``
  * ``oci db database convert-to-new-pdb-precheck``
  * ``oci db database convert-to-pdb-sync``
  * ``oci db database convert-to-pdb-sync-rollback``
  * ``oci db database list-pdb-conversion-history``
  * ``oci db pdb-conversion-history get --history-id``

* Support to optionally provide peer database unique name AND SID prefix during database creation in ExaCS and ExaCC in Database Service

  * ``oci db database create --sid-prefix``
  * ``oci db database create-from-backup --sid-prefix``
  * ``oci db data-guard-association create from-existing-db-system --peer-db-unique-name  --peer-sid-prefix``
  * ``oci db data-guard-association create from-existing-vm-cluster --peer-db-unique-name  --peer-sid-prefix``

* Support for a parameter for creating db system from the backup with database software image in Database Service

  * ``oci db system launch-from-backup --database-software-image-id``

* Support for preference get/update/remove in Log Analytics Service

  * ``oci log-analytics preference get``
  * ``oci log-analytics preference update``
  * ``oci log-analytics preference remove``

* Support for unprocessed data bucket in Log Analytics Service

  * ``oci log-analytics upload set-unprocessed-bucket``
  * ``oci log-analytics upload get-unprocessed-bucket``
  * ``oci log-analytics source disable-auto-assoc``

* Support for new parameter ``object-name-filters`` to object collection rule in Log Analytics Service

  * ``oci log-analytics object-collection-rule create --object-name-filters``

Changed
~~~~~~~

* Logic for CLI retries.

  * Number of attempts is now 8 (previously 5)
  * Maximum time for retries is now 600s (previously 300s)
  * Exponential backoff with de-correlated jitter is used

3.1.2 - 2021-10-12
------------------
Added
~~~~~
* Support for Web Application Firewall service

  * ``oci waf``

* Support for Application Performance Monitoring Configuration service

  * ``oci apm-config``

* Support for Data Labeling Service Control Plane

  * ``oci data-labeling-service``

* Support for Data Labeling Service Data Plane

  * ``oci data-labeling-service-dataplane``

* Log Analytics service

  * Support for partitioning/searching data via logset

    * ``oci log-analytics storage get-log-sets-count``

  * Support for filtering by log-set-name-contains from the existing list-log-sets API

    * ``oci log-analytics storage list-log-sets --log-set-name-contains``

* Application Performance Monitoring Synthetic service

  * Support for run once feature in monitor.

    * ``oci apm-synthetics monitor create-rest-monitor --is-run-once``

  * Support for enabling network data collection on the monitor by providing a network configuration

    * ``oci apm-synthetics monitor create-browser-monitor --configuration-network-configuration``

3.1.1 - 2021-10-05
------------------
Added
~~~~~
* Management Agent service

  * Support for set-auto-upgradable-config and get-auto-upgradable-config

    * ``oci management-agent agent set-auto-upgradable-config``
    * ``oci management-agent agent get-auto-upgradable-config``

  * Support for additional -install-type parameters for List Management Agents, Images and Count operations

    * ``oci management-agent agent list --install-type``
    * ``oci management-agent agent summarize-agent-counts --install-type``
    * ``oci management-agent agent-image list --install-type``

* Support for configuring Binlog variables in the MySQL Database service

  * ``oci mysql configuration create --variables '{"binlogRowMetadata": "<MINIMAL|FULL>"}'``
  * ``oci mysql configuration create --variables '{"binlog-row-value-options": "PARTIAL_JSON"}'``
  * ``oci mysql configuration create --variables '{"binlog-transaction-compression": <true|false>}'``

* Support for new creation type `OPERATOR` when listing MDS backups in MySQL service

  * ``oci mysql backup list --creation-type OPERATOR``

* Support for deployment upgrade operations and cancelling deployment backups in Golden Gate service

  * ``oci goldengate deployment-upgrade get|list``
  * ``oci goldengate deployment-backup cancel``

* Database Migration service

  * Support for getting job advisor reports and listing migration object types

    * ``oci database-migration job get-advisor-report``
    * ``oci database-migration migration-object-type-summary list``

  * Support for advisor settings for migration create and update operations

    * ``oci database-migration migration update --advisor-settings``
    * ``oci database-migration migration create --advisor-settings``

  * Support for including objects when cloning or creating a database migration job

    * ``oci database-migration migration clone --include-objects``
    * ``oci database-migration migration create --include-objects``


Changed
~~~~~~~

* Removed --display-name param from work-request operations and --compartment-id param from agent update operation in Database Migration service

  * ``oci database-migration work-request list``
  * ``oci database-migration work-request-error list``
  * ``oci database-migration work-request-logs list``
  * ``oci database-migration agent update``

3.1.0 - 2021-09-28
-------------------
Added
~~~~~
* Support for One-way TLS Connections in Database service

  * Support for creating autonomous database and clones on shared infrastructure that do not require mTLS

    * ``oci db autonomous-database create --is-mtls-connection-required false``

  * Support for updating autonomous database and clones on shared infrastructure to not require mTLS

    * ``oci db autonomous-database update --is-mtls-connection-required false``

  * Support to check if an autonomous database on shared infrastructure requires mTLS, with added field isMtlsRequired

    * ``oci db autonomous-database get --autonomous-database-id <ocid>``

  * Support to get connection string profiles for an autonomous database on shared infrastructure, with added field profiles in connectionStrings

    * ``oci db autonomous-database get --autonomous-database-id <ocid>``

* Support for Server side encryption using object specific KMS key in Object Storage Service

  * New parameter --opc-sse-kms-key-id has been added to the below commands for passing kms key id

    * ``oci os object put --opc-sse-kms-key-id <target_key_id>``
    * ``oci os object copy --opc-sse-kms-key-id <target_key_id>``

* Allow filter based on operating system family and sort by operating system name in JMS service

  * ``oci jms application-usage summarize --os-family --sort-by``
  * ``oci jms installation-usage summarize --os-family --sort-by``
  * ``oci jms jre-usage summarize --os-family --sort-by``
  * ``oci jms managed-instance-usage summarize --os-family --sort-by``

* Support for using Network Security Groups with API Gateway service

  * ``oci api-gateway gateway create --network-security-group-ids``
  * ``oci api-gateway gateway update --network-security-group-ids``

* Support for Network Security Groups in Functions service

  * ``oci fn application create --network-security-group-ids``

* Support for a new parameter ``image-policy-config`` for Applications in Functions service

  * ``oci fn application create --image-policy-config``
  * ``oci fn application update --image-policy-config``

* Support for a new optional field "messageFormat" which will enable customers to chose the format of alert message while creating and updating alarms in Monitoring service

  * ``oci monitoring alarm create --message-format``
  * ``oci monitoring alarm update --message-format``

* Support for DataSafe User and Security Assessment features in Data Safe service

  * ``oci data-safe security-assessment``
  * ``oci data-safe user-assessment``

* Support for upto micro-second precision for datatime parameters

Changed
~~~~~~~~~
* [BREAKING] Remove redundant request-summarized operations.

  * ``oci jms application-usage request-summarized``
  * ``oci jms installation-usage request-summarized``
  * ``oci jms jre-usage request-summarized``
  * ``oci jms managed-instance-usage request-summarized``

* Fixed bug in Management Dashborad service
  * ``oci management-dashboard dashboard export``

3.0.5 - 2021-09-14
-------------------
Added
~~~~~

* Interactive command for instance principal authentication setup for an existing Compute instance

  * ``oci setup instance-principal``

* Support for browser-based config file creation for CLI commands that are run with a nonexistent config file and api_key auth

* Support for --region, --config-location, and --profile-name options for browser-based CLI config file creation

  * ``oci setup bootstrap --region --config-location --profile-name``

* Support for Shielded Instances in the Compute service

  * ``oci compute measured-boot-report``

* Support for ML Jobs in the Data Science service

  * ``oci data-science job``
  * ``oci data-science job-run``
  * ``oci data-science job-shape``

3.0.4 - 2021-09-07
-------------------
Added
~~~~~

* Support for scheduled jobs in Database Management service

  * Create scheduled jobs for managed databases

    * ``oci database-management job``

  * Update a schedule job

    * ``oci database-management job update``

  * Get summary of job execution status

    * ``oci database-management job-executions-status summarize``

*  Support for a unified way of managing both external and cloud databases in the Database Management service

  * Create private endpoints to be used for managing Cloud databases as part of Database Management service

    * ``oci database-management private-endpoint``

  * List databases that are managed using specified private endpoint

    * ``oci database-management associated-database-summary list-associated-databases``

  * Get metrics for a specified Pluggable Database (PDB) managed by Database Management service

    * ``oci database-management pdb-metrics``

  * Get health metrics for a fleet of databases filtered by database deployment type and database version

    * ``oci database-management fleet-health-metrics``

  * Support for using Secrets for executing a SQL job in Database Management service

    * ``oci database-management job``

  * Filter Managed Databases by their deployment type and management option

    * ``oci database-management managed-database``

* Support for enable, disable, modify in Database Management service

  * ``oci db database enable-database-management``
  * ``oci db database disable-database-management``
  * ``oci db database modify-database-management``

* Support for getting the detailed log content of a job in the Resource Manager service

  * ``oci resource-manager job get-job-detailed-log-content``

* Support for ``--max-wait-seconds``, ``--wait-for-state``, ``--wait-interval-seconds`` to Management Dashboard service

  * ``oci management-dashboard dashboard change-compartment``
  * ``oci management-dashboard saved-search change-compartment``

Changed
~~~~~~~

* Support for terraform advanced options (detailed log level, refresh, and parallelism) on jobs in the Resource Manager service

  * ``oci resource-manager job create-plan-job --terraform-advanced-options``
  * ``oci resource-manager job create-apply-job --terraform-advanced-options``
  * ``oci resource-manager job create-destroy-job --terraform-advanced-options``

* Support for forced cancellation when cancelling jobs in the Resource Manager service

  * ``oci resource-manager job cancel --is-forced``

* Updated fallback virtualenv url in install.py script

* Updated install.py for "root" user to be able to install cli on ubuntu without sudo.

3.0.3 - 2021-08-31
-------------------
Added
~~~~~
* Prompt to create a config file with a profile using API key pair authentication if a CLI command is run with a nonexistent config file and api_key auth

* Support for Oracle Analytics Cloud and OCI Vault integration on connections in Data Catalog service

  * ``oci data-catalog data-asset parse-connection --wallet-secret-id, --wallet-secret-name``

* Support for critical event monitoring in the OS Management service
  
  * ``oci os-management event``
  * ``oci os-management managed-instance install-all-updates --update-type``
  * ``oci os-management managed-instance install-all-windows-updates --update-type``
  * ``oci os-management managed-instance-group install-all-updates``
  * ``oci os-management scheduled-job list --is-restricted``
  * ``oci os-management update-managed-instance-details update-managed-instance``
  * ``oci os-management work-request-summary``

Changed
~~~~~~~
* Modified supported version for the following package: arrow (>=1.0.0), cryptography (>=3.2.1, <=3.4.7)

* Configparser has been removed from the requirements

3.0.2 - 2021-08-24
-------------------
Added
~~~~~
* Support to generate recommended vm cluster network and create vm cluster network with given customer listener port in the Database service

  * ``oci db exadata-infrastructure generate-recommended-vm-cluster-network --scan-listener-port-tcp, --scan-listener-port-tcp-ssl``
  * ``oci db vm-cluster-network create --scans``

* Prompt to create a config file with a CLI session profile if a CLI command is run with a nonexistent config file and --auth security_token

* Prompt to re-authenticate a CLI session profile if a CLI command is run with an expired session token and --auth security_token

Changed
~~~~~~~
* Modified supported versions for the following packages: cryptography (>3.2.1, <=3.4.7), click (7.1.2).

3.0.1 - 2021-08-17
-------------------
Added
~~~~~
* Support for identifying Management Agent hosts eligible to create Operations Insights Host resources on

  * ``oci opsi host-insights list-importable-agent-entities``

* Support for summarize-agen-counts and summarize-plugin-counts in Management Agent service

  * ``oci management-agent agent summarize-agent-counts``
  * ``oci management-agent agent summarize-plugin-counts``

* Support for additional filters when listing management agents in Management Agent service

  * ``oci management-agent agent list --availability-status, --host-id, --is-customer-deployed``

Changed
~~~~~~~

* Modified supported versions for the following packages: six (>=0.15.0).

* Check the bucket exists before bulk and sync operations in Object Storage service

  * ``oci os object bulk-upload``
  * ``oci os object bulk-download``
  * ``oci os object sync``

* Session authentication now has no private key passphrase prompt by default; private key passphrase can be provided by running session authenticate with --use-passphrase option

  * ``oci session authenticate``

3.0.0 - 2021-08-03
-------------------
[BREAKING] Drop support for Python 2

Added
~~~~~
* Support for ``os object sync`` command that synchronizes a filesystem directory with an Object Storage bucket in the Object Storage service.

  * ``oci os object sync``

* Support for --availability-domain option when listing VNICs attached to an instance in the Compute service

  * ``oci compute instance list-vnics --availability-domain``

* Support for Autonomous Database Create with Early Patching via a new parameter (maintenance-schedule-type) in the Database service.

  * ``oci db autonomous-database create --maintenance-schedule-type``
  * ``oci db autonomous-database create-adb-cross-region-data-guard-details --maintenance-schedule-type``
  * ``oci db autonomous-database create-from-backup-id --maintenance-schedule-type``
  * ``oci db autonomous-database create-from-backup-timestamp --maintenance-schedule-type``
  * ``oci db autonomous-database create-from-clone --maintenance-schedule-type``
  * ``oci db autonomous-database create-virtual-clone --maintenance-schedule-type``

* Support for non-default config file locations for the below commands

  * ``oci session refresh``
  * ``oci session export``
  * ``oci session import``

* Support for Model Catalog v2.0 features including Provenance, Metadata, Schema, Artifact introspection

  * ``oci data-science model``

* Support for new parameter --metastore-id to specify external hive metastore for Application in the Data Flow service

  * ``oci data-flow application create --metastore-id``
  * ``oci data-flow application update --metastore-id``

* Support for manual copy of volume group backups across regions in the Block Storage service

  * ``oci bv volume-group-backup copy``

* Support for MDS Backup Change Compartment in MySql service

  * ``oci mysql backup change-compartment``

Changed
~~~~~~~

* Block volume backup copy operations now wait for their associated work requests to complete

  * ``oci bv boot-volume-backup copy``
  * ``oci bv backup copy``

2.26.4 - 2021-07-27
-------------------
Added
~~~~~

* Support for filtering by tag on capacity planning and SQL warehouse list operations in the Operations Insights service

  * Parameters ``defined-tag-equals``, ``freeform-tag-equals``, ``defined-tag-exists``, ``freeform-tag-exists`` are added for some commands under ``oci opsi database-insights``
  
* Support for creating cross-region autonomous data guards in the Database service
  
*  ``oci db autonomous-database create-cross-region-data-guard``
*  ``oci db autonomous-database fail-over --peer-db-id``
*  ``oci db autonomous-database switchover --peer-db-id``
*  ``oci db autonomous-database update --peer-db-id``

* Support for the customer contacts feature on cloud exadata infrastructure in the Database service

  * ``oci db cloud-exa-infra create --customer-contacts``
  * ``oci db cloud-exa-infra update --customer-contacts``

* Support for cost analysis custom tables in the Usage service

  * ``oci usage-api custom-table``

* Support non-default config file locations for ``oci session validate`` and ``oci session terminate``

* Support to add passphrase for session authentication (``oci session authenticate``)


2.26.3 - 2021-07-20
-------------------
Added
~~~~~

* Support for empty and dry-run options while deleting buckets in Object Storage service

  * ``oci os bucket delete --empty  --dry-run``
  * ``oci os bucket delete --empty``

* Support for schedules and tasks in Data Integration service

  * ``oci data-integration schedule``
  * ``oci data-integration task``

* Database service

  * Support for getting available updates and updating histories for a VM cluster

    * ``oci db vm-cluster get-update --update-id <Update OCID> --vm-cluster-id <VM Cluster OCID>``
    * ``oci db vm-cluster list-updates --vm-cluster-id <VM Cluster OCID> --update-type <GI_PATCH/GI_UPGRADE/OS_UPDATE>``
    * ``oci db vm-cluster get-update-history --update-history-entry-id <UpdateHistory OCID> --vm-cluster-id <VM Cluster OCID>``
    * ``oci db vm-cluster list-update-histories --vm-cluster-id <VM Cluster OCID> --update-type <GI_PATCH/GI_UPGRADE/OS_UPDATE>``

  * Support for updating dataguard

    * ``oci db data-guard-association update``

  * Support for downloading network validation report file for VM Cluster Networks

    * ``oci db vm-cluster-network download-validation-report --exadata-infrastructure-id, --file, --vm-cluster-network-id``

Changed
~~~~~~~

* Support patch and upgrade of Grid Infrastructure (GI) and update of DomU OS software for a VM cluster

  * ``oci db vm-cluster update --update-id <Update OCID> --update-action <PRECHECK/ROLLING_APPLY/ROLLBACK>``

2.26.2 - 2021-07-13
-------------------
Added
~~~~~

* Support for AI Anomaly Detection service

  * ``oci anomaly-detection``

* Support for retrieving a DNS zone as a zone file in DNS service

  * ``oci dns zone get-zone-content --file``

* Support for Search domain type for DHCP options to support multi-level search domain in Network Service.

  * ``oci network dhcp-options create --domain-name-type``
  * ``oci network dhcp-options update --domain-name-type``

* Support for searching Marketplace Listings

  * ``oci marketplace listing-summary search-listings``
  * ``oci marketplace listing-summary search-listings-free-text``
  * ``oci marketplace listing-summary search-listings-structured``

Changed
~~~~~~~~

* Parameter --availability-domain is now optional in create VLAN in Network service.

  * ``oci network vlan create--availability-domain``

2.26.1 - 2021-07-06
-------------------
Added
~~~~~

* Support for Order Activation features in the Organizations Service

  * oci organizations order activate
  * oci organizations order get

* Support new OCE instance license type - Starter Edition in the OCE service. The new license type is: STARTER

  * ``oci oce oce-instance create --instance-license-type STARTER``
  * ``oci oce oce-instance update --instance-license-type STARTER``

* Expanded DRG functionality in the Networking Service

  * More than one VCN can be attached to a DRG
  * Flexible routing inside DRG enables packet flow between any two attachments
  * Routing policy to customize dynamic import/export of routes

* Operations Insights

  * Support for resource principal authorization for enterprise manager bridge resource
  * New lifecycle state "NEEDS_ATTENTION" to indicate issues with the bridge resource, and new field "objectStorageBucketStatusDetails" to provide detail

    * ``oci opsi host-insights list --lifecycle-state NEEDS_ATTENTION``
    * ``oci opsi enterprise-manager-bridges list --lifecycle-state NEEDS_ATTENTION``
    * ``oci opsi database-insights list --lifecycle-state NEEDS_ATTENTION``

Changed
~~~~~~~

* Changed ``oci setup autocomplete`` to create a symlink pointing to current CLI version oci_autocomplete.sh script

Fixed
~~~~~

* Issue with environment based config throwing ``FileNotFoundError:`` for a non-required config

2.26.0 - 2021-06-29
-------------------
Added
~~~~~

* Support for passing in private key content as a environment variable. A private key file is not required if this variable is set

  * Export ``OCI_CLI_KEY_CONTENT`` with the private key content enclosed with single quotes

* Support for the DevOps service

  * ``oci devops``

* Support for configuring network security groups for node pools in the container engine for Kubernetes service

  * ``oci ce node-pool create --nsg-ids``
  * ``oci ce node-pool update --nsg-ids``

* Support for optionally specifying CPU core count and data storage size when creating autonomous databases in the Database service

  * ``oci db autonomous-database create --data-storage-size-in-gbs``

*  Support for metastore and initial data asset import/export in the Data Catalog service

  * ``oci data-catalog metastore``
  * ``oci data-catalog data-asset import``
  * ``oci data-catalog data-asset synchronous-export``
  * [Breaking] ``DISPLAYNAME`` removed from --sort-by option

* Support for Email Domain in the Email Delivery service

  * ``oci email domain change-compartment --compartment-id --email-domain-id``
  * ``oci email domain create --compartment-id --name``
  * ``oci email domain delete --email-domain-id``
  * ``oci email domain get --email-domain-id``
  * ``oci email domain list --compartment-id``
  * ``oci email domain update --email-domain-id``

* Support for Domain Key Identified Mail in the Email Delivery service

  * ``oci email dkim create --email-domain-id``
  * ``oci email dkim delete --dkim-id``
  * ``oci email dkim get --dkim-id``
  * ``oci email dkim list --email-domain-id``
  * ``oci email dkim update --dkim-id``

* Support for new API to list work requests for Email Domain and DKIM in the Email Delivery service

  * ``oci email work-request get --work-request-id``
  * ``oci email work-request list --compartment-id``
  * ``oci email work-request-error-collection list --work-request-id``
  * ``oci email work-request-log list --work-request-id``

* Support for ``--domain`` field in the response for ``oci email sender`` in the Email Delivery service

* Support for changing the number of retries for a CLI command (``--max-retries``)

2.25.4 - 2021-06-22
-------------------
Added
~~~~~

* Users can authenticate the CLI with only environment variables, a config does not need to exist

  * The following environment variables need to be set, OCI_CLI_USER, OCI_CLI_TENANCY, OCI_CLI_FINGERPRINT, OCI_CLI_KEY_FILE, OCI_CLI_REGION
  * Optional variable for passphrase, OCI_CLI_PASSPHRASE

* Support for VMBM Pluggable Database feature as a part of the Database Service

  * ``oci db pluggable-database``

Changed
~~~~~~~

* Support for cross-tenancy volume clone in Block Storage service

  * ``oci bv volume create --source-volume-id``
  * ``oci bv boot-volume create --source-volume-id``

* Changed allowed versions of cryptography package to a range from 3.2.1 to 3.4.7

* Following updates in installer scripts:
  
  * Use dnf, if available, to install python
  * Updated check for ubuntu/debian systems to use ID_LIKE/ID instead of NAME in /etc/os-release

Fixed
~~~~~

* oci setup bootstrap was causing a ``AttributeError: module 'oci' has no attribute 'identity'``

2.25.3 - 2021-06-15
-------------------
Added
~~~~~~~~

* Support for migrating an OKE cluster not integrated with your VCN to a VCN-Native cluster in Container Engine

  * ``oci ce cluster cluster-migrate-to-native-vcn``
  * ``oci ce cluster cluster-migrate-to-native-vcn-status``

* Support for filtering of applications based on spark version in Data Flow service

  * ``oci data-flow application list --spark-version``

* Support for registration and management of target databases in Data Safe service.

  * ``oci data-safe target-database create``

* Support for Elastic Storage feature for Exadata Infrastructure resources for ExaCC in Database service.

  * ``oci db exadata-infrastructure create --compute-count``
  * ``oci db exadata-infrastructure update --additional-storage-count``
  * ``oci db exadata-infrastructure add --exadata-infrastructure-id``

* New parameter --parameters-config has been added to the below commands in Management Dashboard service

  * ``oci management-dashboard dashboard create --parameters-config``
  * ``oci management-dashboard dashboard update``
  * ``oci management-dashboard saved-search create``
  * ``oci management-dashboard saved-search update``

Changed
~~~~~~~

* PyYAML version requirement relaxed from PyYAML==5.4.1 to PyYAML>=5.4,<6

* Default thread count for multipart upload/download using ``oci os object put | get`` is 10.

* Multipart download is now default for ``oci os object get``. Please use ``--no-multipart`` to disable multipart download.

* Changed multipart download chunk size to maximum instead of 1Mb

Fixed
~~~~~~~
* Parameter --compartment-id was existing twice in change compartment for rove node in Rover service

  * ``oci rover node change-compartment --compartment-id``

* Issue with multipart download - progress bar was only showing 50% even though full file was uploaded.

2.25.2 - 2021-06-08
-------------------
Added
~~~~~

* Support for Java Management Service

  * ``oci jms``

* Support to update iscsi Login State for a Volume Attachment in Compute service

  * ``oci compute volume-attachment update --iscsi-login-state``

* Support for 'host-name' and 'is-database-instance-level-metrics' query parameters in Operations Insights service

  * ``oci opsi database-insights summarize-database-insight-resource-capacity-trend``
  * ``oci opsi database-insights summarize-database-insight-resource-forecast-trend``
  * ``oci opsi database-insights summarize-database-insight-resource-statistics``
  * ``oci opsi database-insights summarize-database-insight-resource-usage``
  * ``oci opsi database-insights summarize-database-insight-resource-usage-trend``
  * ``oci opsi database-insights summarize-database-insight-resource-utilization-insight``
  * ``oci opsi database-insights summarize-sql-insights``
  * ``oci opsi database-insights summarize-sql-statistics``
  * ``oci opsi database-insights summarize-sql-statistics-time-series``

* Support for listing database configurations in Operations Insights service

  * ``oci opsi database-insights list-database-configurations``

* Added support for a new type of Source called Import for use with the Export tool in Application Migration service

  * ``oci application-migration source create-source-import-source-details``
  * ``oci application-migration source update-source-import-source-details``

2.25.1 - 2021-06-01
-------------------
Added
~~~~~

* Support for configuration of autonomous database KMS keys in the Database service

  * ``oci db autonomous-database configure-autonomous-database-vault-key``

* Support for creating database software images from an existing database home in the Database service

  * ``oci db database-software-image create --source-db-home-id``

* Support for creating database software images with any supported RUs in the Database service

  * ``oci db database-software-image create --database-version [optional], --patch-set[optional]``

*  ``--is-desupported-version`` flag is added to take customer acknowledgment for creating database-software images with release older than N-3

  * ``oci db database create --is-desupported-version``
  * ``oci db database create-from-backup --is-desupported-version``
  * ``oci db database create-from-database --is-desupported-version``
  * ``oci db db-home create --is-desupported-version``

* Support for listing all NSGs associated with a given VLAN in the Networking service

  * ``oci network nsg list --compartment-id [optional]``

Changed
~~~~~~~

* Services are now dynamically imported for autocomplete, speeding up completion time

Fixed
~~~~~~~

* Previous release had a bug causing some CLI commands to error with 'KeyError'. Please see `github issue #415 <https://github.com/oracle/oci-cli/issues/415>`_ for more details

2.25.0 - 2021-05-25
-------------------
Added
~~~~~
* [Breaking] For CLI installations running on Python 3.5 or lower, warning message to upgrade Python to v3.6+ and reinstall CLI before August 1st, 2021 will be seen. 
 
  * To disable the warning message, set environment variable ``OCI_CLI_ALLOW_PYTHON2=True``

* O is a wrapper for oci-cli, providing an alternate interface with shortcuts to all commands, parameters, resource IDs, and output fields. 
  
  * O can be found on `GitHub <https://github.com/oracle/oci-cli/blob/master/scripts/examples/project_o>`__.

* Support for Generic Artifacts Service (``oci artifacts``)

* Support for Bastion Service (``oci bastion``)

* Support to provide visualization to view the Automatic Workload Repository (AWR) data for external database in Database Management Service

  * ``oci database-management get-awr-db-report``
  * ``oci database-management get-awr-db-sql-report``
  * ``oci database-management list-awr-db-snapshots``
  * ``oci database-management list-awr-dbs``
  * ``oci database-management summarize-awr-db-cpu-usages``
  * ``oci database-management summarize-awr-db-metrics``
  * ``oci database-management summarize-awr-db-parameter-changes``
  * ``oci database-management summarize-awr-db-parameters``
  * ``oci database-management summarize-awr-db-snapshot-ranges``
  * ``oci database-management summarize-awr-db-sysstats``
  * ``oci database-management summarize-awr-db-top-wait-events``
  * ``oci database-management summarize-awr-db-wait-event-buckets``
  * ``oci database-management summarize-awr-db-wait-events``

* Support for VM.Standard.E3.Flex Flexible Compute Shape with customizable OCPUs and memory for Data Science Notebooks
  
  * ``oci data-science notebook-session create --configuration-details``
  * ``oci data-science notebook-session update --configuration-details``

* Support for HCX Enterprise Add-on for Oracle Cloud VMware Solution 

  * ``oci ocvs sddc cancel-downgrade-hcx``
  * ``oci ocvs sddc downgrade-hcx``
  * ``oci ocvs sddc refresh-hcx-license-status``
  * ``oci ocvs sddc upgrade-hcx``
  * ``current-sku`` parameter in ``oci ocvs esxi-host create`` is now optional
  * ``initial-sku`` parameter in ``oci ocvs sddc create`` is now optional
  
* Support for Secrets Read By Name as part of Secrets in Vault Service

  * ``oci secrets secret-bundle get-secret-bundle-by-name`` 

* Support for ``isDynamic`` field in the response for ``oci limits definition list``

Changed
~~~~~~~

* Service modules are now dynamically imported at runtime, speeding up CLI invocations

2.24.5 - 2021-05-18
-------------------
Added
~~~~~
* Sample scripts are available for every command on the `CLI public doc page <https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/>`__ and man pages

* Support for Object storage configuration source in the Resource Manager service

  * ``oci resource-manager stack create-from-object-storage``
  * ``oci resource-manager stack update-from-object-storage``

* Support for spark-submit compatible options in the Data Flow service

  * ``oci data-flow run submit``

Fixed
~~~~~
* Wait for state parameter for the following commands were returning an error on valid states

  * ``oci mysql db-system start/stop --wait-for-state``
  * ``oci resource-manager stack create --wait-for-state``

* Fixed list commands in Artifacts service

  * ``oci artifacts container image list``
  * ``oci artifacts container image-signature list``
  * ``oci artifacts container repository list``

2.24.4 - 2021-05-11
-------------------
Added
~~~~~
* Support for database maintenance run patchMode feature as a part of the Database Service

  * ``oci db maintenance-run``

Fixed
~~~~~

* PyYAML was upgraded to version 5.4.1 to address a vulnerability identified on GitHub as CVE-2020-14343

* Py was upgraded to version 1.10.0 to address a vulnerability identified on GitHub as CVE-2020-29651. Py isn't used in our run-time system but as part of our documentation build process.

2.24.3 - 2021-05-04
-------------------
Added
~~~~~
* Options for configuring config path and profile name for session authentication

  * ``oci session authenticate --profile-name --config-location``

* Support for the Operator Access Control service

 * ``oci opctl``

* Support for the Service Catalog service

 * ``oci service-catalog``

* Support for the AI Language service

 * ``oci ai language``

Fixed
~~~~~
* Wait for state parameter for the following database commands were returning on incorrect states

  * oci db database create --wait-for-state
  * oci db database create-from-backup --wait-for-state
  * oci db database create-from-database --wait-for-state
  * oci db db-home create --wait-for-state

2.24.2 - 2021-04-27
-------------------
Added
~~~~~

* Support for data masking and other enhancements in the Cloud Guard service

  * ``oci cloud-guard data-mask-rule``
  * ``oci cloud-guard policy-summary list-policies``
  * ``oci cloud-guard problem update-bulk-problem-status --comment``
  
* Support for opting out of DNS records during instance launch, as well as attaching secondary VNICs, in the Compute service

  * ``oci compute instance attach-vnic --assign-private-dns-record``
  * ``oci compute instance launch --assign-private-dns-record``

* Support for mutable sizes on cluster networks in the Compute Management service. Argument (instance-pools) allows to specify updates to the underlying instance pool(s) of a cluster network.
  
  * ``oci compute-management cluster-network update --instance-pools`` 

* Support for auto-tiering on buckets in the Object Storage service

  * ``oci os bucket create --auto-tiering``
  * ``oci os bucket update --auto-tiering``

Changed
~~~~~~~

* VCN id parameter is now optional on list operation in the Networking service

  * ``oci network vlan list --vcn-id``

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

  * ``oci analytics analytics-instance create-private-access-channel``
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
~~~~~~~

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
