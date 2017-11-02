$ociTopLevelCommands = @(
    'bv', 'compute', 'db', 'iam', 'network', 'os', 'setup'
)

$ociSubcommands = @{
    'bv' = 'backup volume'
    'bv backup' = 'create delete get list update'
    'bv volume' = 'create delete get list update'
    'compute' = 'console-history image instance instance-console-connection shape vnic-attachment volume-attachment'
    'compute console-history' = 'capture delete get get-content list update'
    'compute image' = 'create delete export get import list update'
    'compute image export' = 'to-object to-object-uri'
    'compute image import' = 'from-object from-object-uri'
    'compute instance' = 'action attach-vnic detach-vnic get get-windows-initial-creds launch list list-vnics terminate update'
    'compute instance-console-connection' = 'create delete get list'
    'compute shape' = 'list'
    'compute vnic-attachment' = 'get list'
    'compute volume-attachment' = 'attach detach get list'
    'db' = 'data-guard-association database node system system-shape version'
    'db data-guard-association' = 'create failover get list reinstate switchover'
    'db data-guard-association create' = 'from-existing-db-system'
    'db database' = 'create delete get list'
    'db node' = 'get list reset soft-reset start stop'
    'db system' = 'get launch list terminate update'
    'db system-shape' = 'list'
    'db version' = 'list'
    'iam' = 'availability-domain compartment customer-secret-key group policy region region-subscription user'
    'iam availability-domain' = 'list'
    'iam compartment' = 'create get list update'
    'iam customer-secret-key' = 'create delete list update'
    'iam group' = 'add-user create delete get list list-users remove-user update'
    'iam policy' = 'create delete get list update'
    'iam region' = 'list'
    'iam region-subscription' = 'create list'
    'iam user' = 'api-key create delete get list list-groups swift-password ui-password update update-user-state'
    'iam user api-key' = 'delete list upload'
    'iam user swift-password' = 'create delete list update'
    'iam user ui-password' = 'create-or-reset'
    'network' = 'cpe dhcp-options drg drg-attachment internet-gateway ip-sec-connection private-ip route-table security-list subnet vcn vnic'
    'network cpe' = 'create delete get list update'
    'network dhcp-options' = 'create delete get list update'
    'network drg' = 'create delete get list update'
    'network drg-attachment' = 'create delete get list update'
    'network internet-gateway' = 'create delete get list update'
    'network ip-sec-connection' = 'create delete get get-config get-status list update'
    'network private-ip' = 'delete get list update'
    'network route-table' = 'create delete get list update'
    'network security-list' = 'create delete get list update'
    'network subnet' = 'create delete get list update'
    'network vcn' = 'create delete get list update'
    'network vnic' = 'assign-private-ip get unassign-private-ip update'
    'os' = 'bucket multipart ns object preauth-request'
    'os bucket' = 'create delete get list update'
    'os multipart' = 'abort list'
    'os ns' = 'get'
    'os object' = 'bulk-delete bulk-download bulk-upload delete get head list put resume-put'
    'os preauth-request' = 'create delete get list'
    'setup' = 'autocomplete config keys'
}
$script:ociSubcommandKeys = $ociSubcommands.Keys -join '|'

$ociCommandsToLongParams = @{
    'bv backup create' = 'display-name from-json generate-full-command-json-input generate-param-json-input help volume-id'
    'bv backup delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match volume-backup-id'
    'bv backup get' = 'from-json generate-full-command-json-input generate-param-json-input help volume-backup-id'
    'bv backup list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page volume-id'
    'bv backup update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match volume-backup-id'
    'bv volume create' = 'availability-domain compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help size-in-gbs size-in-mbs volume-backup-id'
    'bv volume delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match volume-id'
    'bv volume get' = 'from-json generate-full-command-json-input generate-param-json-input help volume-id'
    'bv volume list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'bv volume update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match volume-id'
    'compute console-history capture' = 'display-name from-json generate-full-command-json-input generate-param-json-input help instance-id'
    'compute console-history delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match instance-console-history-id'
    'compute console-history get' = 'from-json generate-full-command-json-input generate-param-json-input help instance-console-history-id'
    'compute console-history get-content' = 'file from-json generate-full-command-json-input generate-param-json-input help instance-console-history-id length offset'
    'compute console-history list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help instance-id limit page'
    'compute console-history update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match instance-console-history-id'
    'compute image create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help image-source-details instance-id'
    'compute image delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match image-id'
    'compute image export to-object' = 'bucket-name from-json generate-full-command-json-input generate-param-json-input help if-match image-id name namespace'
    'compute image export to-object-uri' = 'from-json generate-full-command-json-input generate-param-json-input help if-match image-id uri'
    'compute image get' = 'from-json generate-full-command-json-input generate-param-json-input help image-id'
    'compute image import from-object' = 'bucket-name compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help name namespace'
    'compute image import from-object-uri' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help uri'
    'compute image list' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help limit operating-system operating-system-version page'
    'compute image update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match image-id'
    'compute instance action' = 'action from-json generate-full-command-json-input generate-param-json-input help if-match instance-id'
    'compute instance attach-vnic' = 'assign-public-ip from-json generate-full-command-json-input generate-param-json-input help hostname-label instance-id private-ip skip-source-dest-check subnet-id vnic-display-name wait'
    'compute instance detach-vnic' = 'compartment-id force from-json generate-full-command-json-input generate-param-json-input help vnic-id'
    'compute instance get' = 'from-json generate-full-command-json-input generate-param-json-input help instance-id'
    'compute instance get-windows-initial-creds' = 'from-json generate-full-command-json-input generate-param-json-input help instance-id'
    'compute instance launch' = 'assign-public-ip availability-domain compartment-id display-name extended-metadata from-json generate-full-command-json-input generate-param-json-input help hostname-label image-id ipxe-script-file metadata private-ip shape skip-source-dest-check ssh-authorized-keys-file subnet-id user-data-file vnic-display-name'
    'compute instance list' = 'availability-domain compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help limit page'
    'compute instance list-vnics' = 'from-json generate-full-command-json-input generate-param-json-input help instance-id limit page'
    'compute instance terminate' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match instance-id'
    'compute instance update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match instance-id'
    'compute instance-console-connection create' = 'from-json generate-full-command-json-input generate-param-json-input help instance-id ssh-public-key-file'
    'compute instance-console-connection delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match instance-console-connection-id'
    'compute instance-console-connection get' = 'from-json generate-full-command-json-input generate-param-json-input help instance-console-connection-id'
    'compute instance-console-connection list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help instance-id limit page'
    'compute shape list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help image-id limit page'
    'compute vnic-attachment get' = 'from-json generate-full-command-json-input generate-param-json-input help vnic-attachment-id'
    'compute vnic-attachment list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help instance-id limit page vnic-id'
    'compute volume-attachment attach' = 'display-name from-json generate-full-command-json-input generate-param-json-input help instance-id type volume-id'
    'compute volume-attachment detach' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match volume-attachment-id'
    'compute volume-attachment get' = 'from-json generate-full-command-json-input generate-param-json-input help volume-attachment-id'
    'compute volume-attachment list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help instance-id limit page volume-id'
    'db data-guard-association create from-existing-db-system' = 'creation-type database-admin-password database-id from-json generate-full-command-json-input generate-param-json-input help peer-db-system-id protection-mode transport-type'
    'db data-guard-association failover' = 'data-guard-association-id database-admin-password database-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db data-guard-association get' = 'data-guard-association-id database-id from-json generate-full-command-json-input generate-param-json-input help'
    'db data-guard-association list' = 'database-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'db data-guard-association reinstate' = 'data-guard-association-id database-admin-password database-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db data-guard-association switchover' = 'data-guard-association-id database-admin-password database-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db database create' = 'admin-password character-set db-name db-system-id db-version db-workload from-json generate-full-command-json-input generate-param-json-input help ncharacter-set pdb-name'
    'db database delete' = 'database-id force from-json generate-full-command-json-input generate-param-json-input help'
    'db database get' = 'database-id from-json generate-full-command-json-input generate-param-json-input help'
    'db database list' = 'compartment-id db-system-id from-json generate-full-command-json-input generate-param-json-input help limit'
    'db node get' = 'db-node-id from-json generate-full-command-json-input generate-param-json-input help'
    'db node list' = 'compartment-id db-system-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'db node reset' = 'db-node-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db node soft-reset' = 'db-node-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db node start' = 'db-node-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db node stop' = 'db-node-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db system get' = 'db-system-id from-json generate-full-command-json-input generate-param-json-input help'
    'db system launch' = 'admin-password availability-domain backup-subnet-id character-set cluster-name compartment-id cpu-core-count data-storage-percentage database-edition db-name db-version db-workload disk-redundancy display-name domain from-json generate-full-command-json-input generate-param-json-input help hostname initial-data-storage-size-in-gb license-model ncharacter-set node-count pdb-name shape ssh-authorized-keys-file subnet-id'
    'db system list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'db system terminate' = 'db-system-id force from-json generate-full-command-json-input generate-param-json-input help if-match'
    'db system update' = 'cpu-core-count data-storage-size-in-gb db-system-id force from-json generate-full-command-json-input generate-param-json-input help if-match ssh-authorized-keys-file'
    'db system-shape list' = 'availability-domain compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'db version list' = 'compartment-id db-system-shape from-json generate-full-command-json-input generate-param-json-input help limit page'
    'iam availability-domain list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help'
    'iam compartment create' = 'compartment-id description from-json generate-full-command-json-input generate-param-json-input help name'
    'iam compartment get' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help'
    'iam compartment list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'iam compartment update' = 'compartment-id description from-json generate-full-command-json-input generate-param-json-input help if-match name'
    'iam customer-secret-key create' = 'display-name from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam customer-secret-key delete' = 'customer-secret-key-id force from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'iam customer-secret-key list' = 'from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam customer-secret-key update' = 'customer-secret-key-id display-name from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'iam group add-user' = 'from-json generate-full-command-json-input generate-param-json-input group-id help user-id'
    'iam group create' = 'compartment-id description from-json generate-full-command-json-input generate-param-json-input help name'
    'iam group delete' = 'force from-json generate-full-command-json-input generate-param-json-input group-id help if-match'
    'iam group get' = 'from-json generate-full-command-json-input generate-param-json-input group-id help'
    'iam group list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'iam group list-users' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input group-id help limit page'
    'iam group remove-user' = 'compartment-id force from-json generate-full-command-json-input generate-param-json-input group-id help user-id'
    'iam group update' = 'description from-json generate-full-command-json-input generate-param-json-input group-id help if-match'
    'iam policy create' = 'compartment-id description from-json generate-full-command-json-input generate-param-json-input help name statements version-date'
    'iam policy delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match policy-id'
    'iam policy get' = 'from-json generate-full-command-json-input generate-param-json-input help policy-id'
    'iam policy list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'iam policy update' = 'description force from-json generate-full-command-json-input generate-param-json-input help if-match policy-id statements version-date'
    'iam region list' = 'from-json generate-full-command-json-input generate-param-json-input help'
    'iam region-subscription create' = 'from-json generate-full-command-json-input generate-param-json-input help region-key tenancy-id'
    'iam region-subscription list' = 'from-json generate-full-command-json-input generate-param-json-input help tenancy-id'
    'iam user api-key delete' = 'fingerprint force from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'iam user api-key list' = 'from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam user api-key upload' = 'from-json generate-full-command-json-input generate-param-json-input help key user-id'
    'iam user create' = 'compartment-id description from-json generate-full-command-json-input generate-param-json-input help name'
    'iam user delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'iam user get' = 'from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam user list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'iam user list-groups' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page user-id'
    'iam user swift-password create' = 'description from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam user swift-password delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match swift-password-id user-id'
    'iam user swift-password list' = 'from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam user swift-password update' = 'description from-json generate-full-command-json-input generate-param-json-input help if-match swift-password-id user-id'
    'iam user ui-password create-or-reset' = 'from-json generate-full-command-json-input generate-param-json-input help user-id'
    'iam user update' = 'description from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'iam user update-user-state' = 'blocked from-json generate-full-command-json-input generate-param-json-input help if-match user-id'
    'network cpe create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help ip-address'
    'network cpe delete' = 'cpe-id force from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network cpe get' = 'cpe-id from-json generate-full-command-json-input generate-param-json-input help'
    'network cpe list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'network cpe update' = 'cpe-id display-name from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network dhcp-options create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help options vcn-id'
    'network dhcp-options delete' = 'dhcp-id force from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network dhcp-options get' = 'dhcp-id from-json generate-full-command-json-input generate-param-json-input help'
    'network dhcp-options list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network dhcp-options update' = 'dhcp-id display-name force from-json generate-full-command-json-input generate-param-json-input help if-match options'
    'network drg create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help'
    'network drg delete' = 'drg-id force from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network drg get' = 'drg-id from-json generate-full-command-json-input generate-param-json-input help'
    'network drg list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'network drg update' = 'display-name drg-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network drg-attachment create' = 'display-name drg-id from-json generate-full-command-json-input generate-param-json-input help vcn-id'
    'network drg-attachment delete' = 'drg-attachment-id force from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network drg-attachment get' = 'drg-attachment-id from-json generate-full-command-json-input generate-param-json-input help'
    'network drg-attachment list' = 'compartment-id drg-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network drg-attachment update' = 'display-name drg-attachment-id from-json generate-full-command-json-input generate-param-json-input help if-match'
    'network internet-gateway create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help is-enabled vcn-id'
    'network internet-gateway delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match ig-id'
    'network internet-gateway get' = 'from-json generate-full-command-json-input generate-param-json-input help ig-id'
    'network internet-gateway list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network internet-gateway update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match ig-id is-enabled'
    'network ip-sec-connection create' = 'compartment-id cpe-id display-name drg-id from-json generate-full-command-json-input generate-param-json-input help static-routes'
    'network ip-sec-connection delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match ipsc-id'
    'network ip-sec-connection get' = 'from-json generate-full-command-json-input generate-param-json-input help ipsc-id'
    'network ip-sec-connection get-config' = 'from-json generate-full-command-json-input generate-param-json-input help ipsc-id'
    'network ip-sec-connection get-status' = 'from-json generate-full-command-json-input generate-param-json-input help ipsc-id'
    'network ip-sec-connection list' = 'compartment-id cpe-id drg-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'network ip-sec-connection update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match ipsc-id'
    'network private-ip delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match private-ip-id'
    'network private-ip get' = 'from-json generate-full-command-json-input generate-param-json-input help private-ip-id'
    'network private-ip list' = 'from-json generate-full-command-json-input generate-param-json-input help ip-address limit page subnet-id vnic-id'
    'network private-ip update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help hostname-label if-match private-ip-id'
    'network route-table create' = 'compartment-id display-name from-json generate-full-command-json-input generate-param-json-input help route-rules vcn-id'
    'network route-table delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match rt-id'
    'network route-table get' = 'from-json generate-full-command-json-input generate-param-json-input help rt-id'
    'network route-table list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network route-table update' = 'display-name force from-json generate-full-command-json-input generate-param-json-input help if-match route-rules rt-id'
    'network security-list create' = 'compartment-id display-name egress-security-rules from-json generate-full-command-json-input generate-param-json-input help ingress-security-rules vcn-id'
    'network security-list delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match security-list-id'
    'network security-list get' = 'from-json generate-full-command-json-input generate-param-json-input help security-list-id'
    'network security-list list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network security-list update' = 'display-name egress-security-rules force from-json generate-full-command-json-input generate-param-json-input help if-match ingress-security-rules security-list-id'
    'network subnet create' = 'availability-domain cidr-block compartment-id dhcp-options-id display-name dns-label from-json generate-full-command-json-input generate-param-json-input help prohibit-public-ip-on-vnic route-table-id security-list-ids vcn-id'
    'network subnet delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match subnet-id'
    'network subnet get' = 'from-json generate-full-command-json-input generate-param-json-input help subnet-id'
    'network subnet list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page vcn-id'
    'network subnet update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match subnet-id'
    'network vcn create' = 'cidr-block compartment-id display-name dns-label from-json generate-full-command-json-input generate-param-json-input help'
    'network vcn delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match vcn-id'
    'network vcn get' = 'from-json generate-full-command-json-input generate-param-json-input help vcn-id'
    'network vcn list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit page'
    'network vcn update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help if-match vcn-id'
    'network vnic assign-private-ip' = 'display-name from-json generate-full-command-json-input generate-param-json-input help hostname-label ip-address unassign-if-already-assigned vnic-id'
    'network vnic get' = 'from-json generate-full-command-json-input generate-param-json-input help vnic-id'
    'network vnic unassign-private-ip' = 'from-json generate-full-command-json-input generate-param-json-input help ip-address vnic-id'
    'network vnic update' = 'display-name from-json generate-full-command-json-input generate-param-json-input help hostname-label if-match skip-source-dest-check vnic-id'
    'os bucket create' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help metadata name namespace public-access-type'
    'os bucket delete' = 'force from-json generate-full-command-json-input generate-param-json-input help if-match name namespace'
    'os bucket get' = 'from-json generate-full-command-json-input generate-param-json-input help if-match if-none-match name namespace'
    'os bucket list' = 'compartment-id from-json generate-full-command-json-input generate-param-json-input help limit namespace page'
    'os bucket update' = 'from-json generate-full-command-json-input generate-param-json-input help if-match metadata name namespace public-access-type'
    'os multipart abort' = 'bucket-name force from-json generate-full-command-json-input generate-param-json-input help namespace object-name upload-id'
    'os multipart list' = 'bucket-name from-json generate-full-command-json-input generate-param-json-input help limit namespace page'
    'os ns get' = 'from-json generate-full-command-json-input generate-param-json-input help'
    'os object bulk-delete' = 'bucket-name delimiter dry-run exclude force from-json generate-full-command-json-input generate-param-json-input help include namespace parallel-operations-count prefix'
    'os object bulk-download' = 'bucket-name delimiter download-dir exclude from-json generate-full-command-json-input generate-param-json-input help include namespace no-overwrite overwrite parallel-operations-count prefix'
    'os object bulk-upload' = 'bucket-name content-encoding content-language content-type disable-parallel-uploads exclude from-json generate-full-command-json-input generate-param-json-input help include metadata namespace no-multipart no-overwrite object-prefix overwrite parallel-upload-count part-size src-dir'
    'os object delete' = 'bucket-name force from-json generate-full-command-json-input generate-param-json-input help if-match name namespace'
    'os object get' = 'bucket-name file from-json generate-full-command-json-input generate-param-json-input help if-match if-none-match name namespace range'
    'os object head' = 'bucket-name from-json generate-full-command-json-input generate-param-json-input help if-match if-none-match name namespace'
    'os object list' = 'bucket-name delimiter end fields from-json generate-full-command-json-input generate-param-json-input help limit namespace prefix start'
    'os object put' = 'bucket-name content-encoding content-language content-md5 content-type disable-parallel-uploads file force from-json generate-full-command-json-input generate-param-json-input help if-match metadata name namespace no-multipart parallel-upload-count part-size'
    'os object resume-put' = 'bucket-name disable-parallel-uploads file from-json generate-full-command-json-input generate-param-json-input help name namespace parallel-upload-count part-size upload-id'
    'os preauth-request create' = 'access-type bucket-name from-json generate-full-command-json-input generate-param-json-input help name namespace object-name opc-client-request-id time-expires'
    'os preauth-request delete' = 'bucket-name force from-json generate-full-command-json-input generate-param-json-input help namespace opc-client-request-id par-id'
    'os preauth-request get' = 'bucket-name from-json generate-full-command-json-input generate-param-json-input help namespace opc-client-request-id par-id'
    'os preauth-request list' = 'bucket-name from-json generate-full-command-json-input generate-param-json-input help limit namespace object-name-prefix opc-client-request-id page'
    'setup autocomplete' = 'help'
    'setup config' = 'help'
    'setup keys' = 'help key-name output-dir overwrite passphrase passphrase-file'
}
$script:ociCommandsWithLongParams = $ociCommandsToLongParams.Keys -join '|'

$ociCommandsToShortParams = @{
    'bv backup create' = '? h'
    'bv backup delete' = '? h'
    'bv backup get' = '? h'
    'bv backup list' = '? c h'
    'bv backup update' = '? h'
    'bv volume create' = '? c h'
    'bv volume delete' = '? h'
    'bv volume get' = '? h'
    'bv volume list' = '? c h'
    'bv volume update' = '? h'
    'compute console-history capture' = '? h'
    'compute console-history delete' = '? h'
    'compute console-history get' = '? h'
    'compute console-history get-content' = '? h'
    'compute console-history list' = '? c h'
    'compute console-history update' = '? h'
    'compute image create' = '? c h'
    'compute image delete' = '? h'
    'compute image export to-object' = '? bn h ns'
    'compute image export to-object-uri' = '? h'
    'compute image get' = '? h'
    'compute image import from-object' = '? bn c h ns'
    'compute image import from-object-uri' = '? c h'
    'compute image list' = '? c h'
    'compute image update' = '? h'
    'compute instance action' = '? h'
    'compute instance attach-vnic' = '? h'
    'compute instance detach-vnic' = '? c h'
    'compute instance get' = '? h'
    'compute instance get-windows-initial-creds' = '? h'
    'compute instance launch' = '? c h'
    'compute instance list' = '? c h'
    'compute instance list-vnics' = '? h'
    'compute instance terminate' = '? h'
    'compute instance update' = '? h'
    'compute instance-console-connection create' = '? h'
    'compute instance-console-connection delete' = '? h'
    'compute instance-console-connection get' = '? h'
    'compute instance-console-connection list' = '? c h'
    'compute shape list' = '? c h'
    'compute vnic-attachment get' = '? h'
    'compute vnic-attachment list' = '? c h'
    'compute volume-attachment attach' = '? h'
    'compute volume-attachment detach' = '? h'
    'compute volume-attachment get' = '? h'
    'compute volume-attachment list' = '? c h'
    'db data-guard-association create from-existing-db-system' = '? h'
    'db data-guard-association failover' = '? h'
    'db data-guard-association get' = '? h'
    'db data-guard-association list' = '? h'
    'db data-guard-association reinstate' = '? h'
    'db data-guard-association switchover' = '? h'
    'db database create' = '? h'
    'db database delete' = '? h'
    'db database get' = '? h'
    'db database list' = '? c h'
    'db node get' = '? h'
    'db node list' = '? c h'
    'db node reset' = '? h'
    'db node soft-reset' = '? h'
    'db node start' = '? h'
    'db node stop' = '? h'
    'db system get' = '? h'
    'db system launch' = '? c h'
    'db system list' = '? c h'
    'db system terminate' = '? h'
    'db system update' = '? h'
    'db system-shape list' = '? c h'
    'db version list' = '? c h'
    'iam availability-domain list' = '? c h'
    'iam compartment create' = '? c h'
    'iam compartment get' = '? c h'
    'iam compartment list' = '? c h'
    'iam compartment update' = '? c h'
    'iam customer-secret-key create' = '? h'
    'iam customer-secret-key delete' = '? h'
    'iam customer-secret-key list' = '? h'
    'iam customer-secret-key update' = '? h'
    'iam group add-user' = '? h'
    'iam group create' = '? c h'
    'iam group delete' = '? h'
    'iam group get' = '? h'
    'iam group list' = '? c h'
    'iam group list-users' = '? c h'
    'iam group remove-user' = '? c h'
    'iam group update' = '? h'
    'iam policy create' = '? c h'
    'iam policy delete' = '? h'
    'iam policy get' = '? h'
    'iam policy list' = '? c h'
    'iam policy update' = '? h'
    'iam region list' = '? h'
    'iam region-subscription create' = '? h'
    'iam region-subscription list' = '? h'
    'iam user api-key delete' = '? h'
    'iam user api-key list' = '? h'
    'iam user api-key upload' = '? h'
    'iam user create' = '? c h'
    'iam user delete' = '? h'
    'iam user get' = '? h'
    'iam user list' = '? c h'
    'iam user list-groups' = '? c h'
    'iam user swift-password create' = '? h'
    'iam user swift-password delete' = '? h'
    'iam user swift-password list' = '? h'
    'iam user swift-password update' = '? h'
    'iam user ui-password create-or-reset' = '? h'
    'iam user update' = '? h'
    'iam user update-user-state' = '? h'
    'network cpe create' = '? c h'
    'network cpe delete' = '? h'
    'network cpe get' = '? h'
    'network cpe list' = '? c h'
    'network cpe update' = '? h'
    'network dhcp-options create' = '? c h'
    'network dhcp-options delete' = '? h'
    'network dhcp-options get' = '? h'
    'network dhcp-options list' = '? c h'
    'network dhcp-options update' = '? h'
    'network drg create' = '? c h'
    'network drg delete' = '? h'
    'network drg get' = '? h'
    'network drg list' = '? c h'
    'network drg update' = '? h'
    'network drg-attachment create' = '? h'
    'network drg-attachment delete' = '? h'
    'network drg-attachment get' = '? h'
    'network drg-attachment list' = '? c h'
    'network drg-attachment update' = '? h'
    'network internet-gateway create' = '? c h'
    'network internet-gateway delete' = '? h'
    'network internet-gateway get' = '? h'
    'network internet-gateway list' = '? c h'
    'network internet-gateway update' = '? h'
    'network ip-sec-connection create' = '? c h'
    'network ip-sec-connection delete' = '? h'
    'network ip-sec-connection get' = '? h'
    'network ip-sec-connection get-config' = '? h'
    'network ip-sec-connection get-status' = '? h'
    'network ip-sec-connection list' = '? c h'
    'network ip-sec-connection update' = '? h'
    'network private-ip delete' = '? h'
    'network private-ip get' = '? h'
    'network private-ip list' = '? h'
    'network private-ip update' = '? h'
    'network route-table create' = '? c h'
    'network route-table delete' = '? h'
    'network route-table get' = '? h'
    'network route-table list' = '? c h'
    'network route-table update' = '? h'
    'network security-list create' = '? c h'
    'network security-list delete' = '? h'
    'network security-list get' = '? h'
    'network security-list list' = '? c h'
    'network security-list update' = '? h'
    'network subnet create' = '? c h'
    'network subnet delete' = '? h'
    'network subnet get' = '? h'
    'network subnet list' = '? c h'
    'network subnet update' = '? h'
    'network vcn create' = '? c h'
    'network vcn delete' = '? h'
    'network vcn get' = '? h'
    'network vcn list' = '? c h'
    'network vcn update' = '? h'
    'network vnic assign-private-ip' = '? h'
    'network vnic get' = '? h'
    'network vnic unassign-private-ip' = '? h'
    'network vnic update' = '? h'
    'os bucket create' = '? c h ns'
    'os bucket delete' = '? h ns'
    'os bucket get' = '? h ns'
    'os bucket list' = '? c h ns'
    'os bucket update' = '? h ns'
    'os multipart abort' = '? bn h ns on'
    'os multipart list' = '? bn h ns'
    'os ns get' = '? h'
    'os object bulk-delete' = '? bn h ns'
    'os object bulk-download' = '? bn h ns'
    'os object bulk-upload' = '? bn h ns'
    'os object delete' = '? bn h ns'
    'os object get' = '? bn h ns'
    'os object head' = '? bn h ns'
    'os object list' = '? bn h ns'
    'os object put' = '? bn h ns'
    'os object resume-put' = '? bn h ns'
    'os preauth-request create' = '? bn h ns on'
    'os preauth-request delete' = '? bn h ns'
    'os preauth-request get' = '? bn h ns'
    'os preauth-request list' = '? bn h ns'
    'setup autocomplete' = '? h'
    'setup config' = '? h'
    'setup keys' = '? h'
}
$script:ociCommandsWithShortParams = $ociCommandsToShortParams.Keys -join '|'

function OciTabExpansion($lastBlock) {
    $res = Oci-Invoke-Utf8ConsoleCommand { OciTabExpansionInternal $lastBlock }
	$res
}

function OciTabExpansionInternal($lastBlock) {
	$ociAliasPattern = GetOciAliasPattern 
	
	switch -regex ($lastBlock -replace "^$($ociAliasPattern) ","") {
		# Handles [oci|bmcs] <top-level command>
		"^(?<cmd>\w+?)$" {
            $com = $matches['cmd']
			$ociTopLevelCommands | Where-Object { $_ -like "$com*" }
		}
	
		# Handles [oci|bmcs] <top-level command> <sub-command> <sub-command> ...
        "^(?<cmd>$ociSubcommandKeys)\s+(?<op>\S*)$" {
            ociCmdOperations $ociSubcommands $matches['cmd'] $matches['op']
        }
		
		# Handles [oci|bmcs] <some level of commands> --<param>
        "^(?<cmd>$ociCommandsWithLongParams).* --(?<param>\S*)$" {
            expandOciLongParams $matches['cmd'] $matches['param']
        }

        # Handles [oci|bmcs] <some level of commands> -<shortparam>
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
	$ociAliases = @("oci", "bmcs") + @(Get-Alias | where { $_.Definition -eq "oci" } | select -Exp Name) + @(Get-Alias | where { $_.Definition -eq "bmcs" } | select -Exp Name)
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
        # Execute OCI/BMCS tab completion
        "^$($ociAliasPattern) (.*)" { OciTabExpansion $lastBlock }

        # Fall back on existing tab expansion
        default {
            if (Test-Path Function:\TabExpansionBackupFromOciAutocomplete) {
                TabExpansionBackupFromOciAutocomplete $line $lastWord
            }
        }
    }
}