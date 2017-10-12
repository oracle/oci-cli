$ociTopLevelCommands = @(
    'bv', 'compute', 'db', 'iam', 'network', 'os', 'setup'
)

$ociSubcommands = @{
    'bv' = 'volume backup'
    'bv backup' = 'list get create update delete'
    'bv volume' = 'list get create update delete'
    'compute' = 'instance shape instance-console-connection console-history volume-attachment vnic-attachment image'
    'compute console-history' = 'list get get-content delete capture'
    'compute image' = 'list get export delete create import update'
    'compute image export' = 'to-object to-object-uri'
    'compute image import' = 'from-object from-object-uri'
    'compute instance' = 'list detach-vnic get action attach-vnic get-windows-initial-creds list-vnics launch terminate update'
    'compute instance-console-connection' = 'list get create delete'
    'compute shape' = 'list'
    'compute vnic-attachment' = 'list get'
    'compute volume-attachment' = 'list get detach attach'
    'db' = 'database system-shape node system version'
    'db database' = 'list get create delete'
    'db node' = 'list get soft-reset stop start reset'
    'db system' = 'list launch get terminate update'
    'db system-shape' = 'list'
    'db version' = 'list'
    'iam' = 'compartment customer-secret-key availability-domain policy region-subscription user region group'
    'iam availability-domain' = 'list'
    'iam compartment' = 'list get create update'
    'iam customer-secret-key' = 'list create update delete'
    'iam group' = 'list get add-user delete create remove-user update list-users'
    'iam policy' = 'list get create update delete'
    'iam region' = 'list'
    'iam region-subscription' = 'list create'
    'iam user' = 'list get update-user-state ui-password list-groups delete swift-password create api-key update'
    'iam user api-key' = 'list upload delete'
    'iam user swift-password' = 'list create update delete'
    'iam user ui-password' = 'create-or-reset'
    'network' = 'internet-gateway drg cpe vcn private-ip ip-sec-connection dhcp-options drg-attachment security-list vnic subnet route-table'
    'network cpe' = 'list get create update delete'
    'network dhcp-options' = 'list get create update delete'
    'network drg' = 'list get create update delete'
    'network drg-attachment' = 'list get create update delete'
    'network internet-gateway' = 'list get create update delete'
    'network ip-sec-connection' = 'list get get-config get-status delete create update'
    'network private-ip' = 'list get update delete'
    'network route-table' = 'list get create update delete'
    'network security-list' = 'list get create update delete'
    'network subnet' = 'list get create update delete'
    'network vcn' = 'list get create update delete'
    'network vnic' = 'unassign-private-ip get assign-private-ip update'
    'os' = 'bucket ns multipart object preauth-request'
    'os bucket' = 'list get create update delete'
    'os multipart' = 'list abort'
    'os ns' = 'get'
    'os object' = 'list resume-put get head bulk-download bulk-delete delete put bulk-upload'
    'os preauth-request' = 'list get create delete'
    'setup' = 'config keys autocomplete'
}
$script:ociSubcommandKeys = $ociSubcommands.Keys -join '|'

$ociCommandsToLongParams = @{
    'bv backup create' = 'from-json display-name generate-param-json-input volume-id help generate-full-command-json-input'
    'bv backup delete' = 'volume-backup-id if-match from-json force generate-param-json-input help generate-full-command-json-input'
    'bv backup get' = 'volume-backup-id generate-param-json-input from-json help generate-full-command-json-input'
    'bv backup list' = 'from-json page generate-param-json-input volume-id compartment-id help generate-full-command-json-input limit'
    'bv backup update' = 'volume-backup-id if-match from-json display-name generate-param-json-input help generate-full-command-json-input'
    'bv volume create' = 'volume-backup-id from-json availability-domain display-name generate-param-json-input size-in-mbs compartment-id help generate-full-command-json-input'
    'bv volume delete' = 'if-match from-json force generate-param-json-input volume-id help generate-full-command-json-input'
    'bv volume get' = 'generate-param-json-input volume-id from-json help generate-full-command-json-input'
    'bv volume list' = 'from-json availability-domain page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'bv volume update' = 'if-match from-json display-name generate-param-json-input volume-id help generate-full-command-json-input'
    'compute console-history capture' = 'generate-param-json-input instance-id help from-json generate-full-command-json-input'
    'compute console-history delete' = 'instance-console-history-id if-match from-json force generate-param-json-input help generate-full-command-json-input'
    'compute console-history get' = 'instance-console-history-id generate-param-json-input from-json help generate-full-command-json-input'
    'compute console-history get-content' = 'instance-console-history-id from-json length file generate-param-json-input offset help generate-full-command-json-input'
    'compute console-history list' = 'from-json availability-domain page generate-param-json-input instance-id compartment-id help generate-full-command-json-input limit'
    'compute image create' = 'from-json image-source-details display-name generate-param-json-input instance-id compartment-id help generate-full-command-json-input'
    'compute image delete' = 'if-match from-json image-id force generate-param-json-input help generate-full-command-json-input'
    'compute image export to-object' = 'if-match namespace from-json image-id name generate-param-json-input bucket-name help generate-full-command-json-input'
    'compute image export to-object-uri' = 'if-match from-json image-id generate-param-json-input uri help generate-full-command-json-input'
    'compute image get' = 'image-id generate-param-json-input from-json help generate-full-command-json-input'
    'compute image import from-object' = 'namespace from-json name display-name generate-param-json-input bucket-name compartment-id help generate-full-command-json-input'
    'compute image import from-object-uri' = 'from-json display-name generate-param-json-input uri compartment-id help generate-full-command-json-input'
    'compute image list' = 'from-json page operating-system display-name generate-param-json-input compartment-id help generate-full-command-json-input limit operating-system-version'
    'compute image update' = 'if-match from-json image-id display-name generate-param-json-input help generate-full-command-json-input'
    'compute instance action' = 'if-match action from-json generate-param-json-input instance-id help generate-full-command-json-input'
    'compute instance attach-vnic' = 'vnic-display-name from-json hostname-label private-ip wait generate-param-json-input instance-id subnet-id help generate-full-command-json-input assign-public-ip skip-source-dest-check'
    'compute instance detach-vnic' = 'from-json force generate-param-json-input compartment-id help generate-full-command-json-input vnic-id'
    'compute instance get' = 'generate-param-json-input instance-id help from-json generate-full-command-json-input'
    'compute instance get-windows-initial-creds' = 'generate-param-json-input instance-id help from-json generate-full-command-json-input'
    'compute instance launch' = 'shape vnic-display-name from-json availability-domain image-id private-ip ssh-authorized-keys-file ipxe-script-file extended-metadata display-name generate-param-json-input assign-public-ip compartment-id subnet-id metadata generate-full-command-json-input help hostname-label skip-source-dest-check user-data-file'
    'compute instance list' = 'from-json availability-domain page display-name generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'compute instance list-vnics' = 'from-json page generate-param-json-input instance-id help generate-full-command-json-input limit'
    'compute instance terminate' = 'if-match from-json force generate-param-json-input instance-id help generate-full-command-json-input'
    'compute instance update' = 'if-match from-json display-name generate-param-json-input instance-id help generate-full-command-json-input'
    'compute instance-console-connection create' = 'from-json ssh-public-key-file generate-param-json-input instance-id help generate-full-command-json-input'
    'compute instance-console-connection delete' = 'if-match from-json force instance-console-connection-id generate-param-json-input help generate-full-command-json-input'
    'compute instance-console-connection get' = 'generate-param-json-input help generate-full-command-json-input from-json instance-console-connection-id'
    'compute instance-console-connection list' = 'from-json page generate-param-json-input instance-id compartment-id help generate-full-command-json-input limit'
    'compute shape list' = 'from-json availability-domain image-id page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'compute vnic-attachment get' = 'vnic-attachment-id generate-param-json-input from-json help generate-full-command-json-input'
    'compute vnic-attachment list' = 'from-json availability-domain page generate-param-json-input instance-id compartment-id help generate-full-command-json-input vnic-id limit'
    'compute volume-attachment attach' = 'from-json display-name generate-param-json-input instance-id volume-id help generate-full-command-json-input type'
    'compute volume-attachment detach' = 'if-match from-json force generate-param-json-input volume-attachment-id help generate-full-command-json-input'
    'compute volume-attachment get' = 'generate-param-json-input volume-attachment-id help from-json generate-full-command-json-input'
    'compute volume-attachment list' = 'from-json availability-domain page generate-param-json-input instance-id volume-id compartment-id help generate-full-command-json-input limit'
    'db database create' = 'from-json pdb-name db-system-id admin-password character-set ncharacter-set generate-param-json-input help db-version generate-full-command-json-input db-name db-workload'
    'db database delete' = 'from-json force generate-param-json-input database-id help generate-full-command-json-input'
    'db database get' = 'generate-param-json-input database-id from-json help generate-full-command-json-input'
    'db database list' = 'from-json db-system-id generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'db node get' = 'generate-param-json-input help generate-full-command-json-input from-json db-node-id'
    'db node list' = 'from-json db-system-id page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'db node reset' = 'if-match from-json db-node-id generate-param-json-input help generate-full-command-json-input'
    'db node soft-reset' = 'if-match from-json db-node-id generate-param-json-input help generate-full-command-json-input'
    'db node start' = 'if-match from-json db-node-id generate-param-json-input help generate-full-command-json-input'
    'db node stop' = 'if-match from-json db-node-id generate-param-json-input help generate-full-command-json-input'
    'db system get' = 'db-system-id generate-param-json-input from-json help generate-full-command-json-input'
    'db system launch' = 'pdb-name ssh-authorized-keys-file admin-password display-name compartment-id shape availability-domain database-edition help db-version generate-full-command-json-input db-workload from-json data-storage-percentage character-set ncharacter-set cluster-name backup-subnet-id db-name hostname domain disk-redundancy generate-param-json-input cpu-core-count subnet-id'
    'db system list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'db system terminate' = 'if-match from-json db-system-id force generate-param-json-input help generate-full-command-json-input'
    'db system update' = 'if-match from-json db-system-id ssh-authorized-keys-file force generate-param-json-input cpu-core-count help generate-full-command-json-input'
    'db system-shape list' = 'from-json availability-domain page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'db version list' = 'db-system-shape from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam availability-domain list' = 'generate-param-json-input compartment-id from-json help generate-full-command-json-input'
    'iam compartment create' = 'from-json description name generate-param-json-input compartment-id help generate-full-command-json-input'
    'iam compartment get' = 'generate-param-json-input compartment-id from-json help generate-full-command-json-input'
    'iam compartment list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam compartment update' = 'if-match from-json description name generate-param-json-input compartment-id help generate-full-command-json-input'
    'iam customer-secret-key create' = 'user-id from-json display-name generate-param-json-input help generate-full-command-json-input'
    'iam customer-secret-key delete' = 'if-match user-id from-json force generate-param-json-input help generate-full-command-json-input customer-secret-key-id'
    'iam customer-secret-key list' = 'generate-param-json-input user-id help from-json generate-full-command-json-input'
    'iam customer-secret-key update' = 'if-match user-id from-json display-name generate-param-json-input help generate-full-command-json-input customer-secret-key-id'
    'iam group add-user' = 'user-id from-json generate-param-json-input help group-id generate-full-command-json-input'
    'iam group create' = 'from-json description name generate-param-json-input compartment-id help generate-full-command-json-input'
    'iam group delete' = 'if-match from-json force generate-param-json-input help group-id generate-full-command-json-input'
    'iam group get' = 'generate-param-json-input help from-json group-id generate-full-command-json-input'
    'iam group list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam group list-users' = 'from-json page generate-param-json-input compartment-id help group-id generate-full-command-json-input limit'
    'iam group remove-user' = 'user-id from-json force generate-param-json-input compartment-id help group-id generate-full-command-json-input'
    'iam group update' = 'if-match from-json description generate-param-json-input help group-id generate-full-command-json-input'
    'iam policy create' = 'version-date description from-json name generate-param-json-input compartment-id help generate-full-command-json-input statements'
    'iam policy delete' = 'if-match from-json policy-id force generate-param-json-input help generate-full-command-json-input'
    'iam policy get' = 'generate-param-json-input help generate-full-command-json-input from-json policy-id'
    'iam policy list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam policy update' = 'if-match version-date description policy-id from-json force generate-param-json-input help generate-full-command-json-input statements'
    'iam region list' = 'generate-param-json-input help from-json generate-full-command-json-input'
    'iam region-subscription create' = 'tenancy-id from-json region-key generate-param-json-input help generate-full-command-json-input'
    'iam region-subscription list' = 'generate-param-json-input tenancy-id help from-json generate-full-command-json-input'
    'iam user api-key delete' = 'if-match user-id from-json force generate-param-json-input help fingerprint generate-full-command-json-input'
    'iam user api-key list' = 'generate-param-json-input user-id help from-json generate-full-command-json-input'
    'iam user api-key upload' = 'user-id from-json key generate-param-json-input help generate-full-command-json-input'
    'iam user create' = 'from-json description name generate-param-json-input compartment-id help generate-full-command-json-input'
    'iam user delete' = 'if-match user-id from-json force generate-param-json-input help generate-full-command-json-input'
    'iam user get' = 'generate-param-json-input user-id help from-json generate-full-command-json-input'
    'iam user list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam user list-groups' = 'user-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'iam user swift-password create' = 'user-id from-json description generate-param-json-input help generate-full-command-json-input'
    'iam user swift-password delete' = 'if-match user-id swift-password-id from-json force generate-param-json-input help generate-full-command-json-input'
    'iam user swift-password list' = 'generate-param-json-input user-id help from-json generate-full-command-json-input'
    'iam user swift-password update' = 'if-match user-id swift-password-id description from-json generate-param-json-input help generate-full-command-json-input'
    'iam user ui-password create-or-reset' = 'generate-param-json-input user-id help from-json generate-full-command-json-input'
    'iam user update' = 'if-match user-id from-json description generate-param-json-input help generate-full-command-json-input'
    'iam user update-user-state' = 'if-match user-id from-json generate-param-json-input blocked help generate-full-command-json-input'
    'network cpe create' = 'ip-address from-json display-name generate-param-json-input compartment-id help generate-full-command-json-input'
    'network cpe delete' = 'if-match from-json force generate-param-json-input help cpe-id generate-full-command-json-input'
    'network cpe get' = 'generate-param-json-input help from-json cpe-id generate-full-command-json-input'
    'network cpe list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network cpe update' = 'if-match from-json display-name generate-param-json-input help cpe-id generate-full-command-json-input'
    'network dhcp-options create' = 'vcn-id from-json options display-name generate-param-json-input compartment-id help generate-full-command-json-input'
    'network dhcp-options delete' = 'if-match from-json force generate-param-json-input help dhcp-id generate-full-command-json-input'
    'network dhcp-options get' = 'generate-param-json-input help from-json dhcp-id generate-full-command-json-input'
    'network dhcp-options list' = 'vcn-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network dhcp-options update' = 'if-match from-json options force display-name generate-param-json-input help dhcp-id generate-full-command-json-input'
    'network drg create' = 'from-json display-name generate-param-json-input compartment-id help generate-full-command-json-input'
    'network drg delete' = 'if-match drg-id from-json force generate-param-json-input help generate-full-command-json-input'
    'network drg get' = 'generate-param-json-input drg-id help from-json generate-full-command-json-input'
    'network drg list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network drg update' = 'if-match drg-id from-json display-name generate-param-json-input help generate-full-command-json-input'
    'network drg-attachment create' = 'vcn-id drg-id from-json display-name generate-param-json-input help generate-full-command-json-input'
    'network drg-attachment delete' = 'if-match from-json force generate-param-json-input drg-attachment-id help generate-full-command-json-input'
    'network drg-attachment get' = 'generate-param-json-input drg-attachment-id help from-json generate-full-command-json-input'
    'network drg-attachment list' = 'vcn-id drg-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network drg-attachment update' = 'if-match from-json display-name generate-param-json-input drg-attachment-id help generate-full-command-json-input'
    'network internet-gateway create' = 'vcn-id from-json is-enabled display-name generate-param-json-input compartment-id help generate-full-command-json-input'
    'network internet-gateway delete' = 'if-match from-json force generate-param-json-input help generate-full-command-json-input ig-id'
    'network internet-gateway get' = 'generate-param-json-input ig-id help from-json generate-full-command-json-input'
    'network internet-gateway list' = 'vcn-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network internet-gateway update' = 'if-match from-json is-enabled display-name generate-param-json-input help generate-full-command-json-input ig-id'
    'network ip-sec-connection create' = 'drg-id from-json display-name generate-param-json-input static-routes compartment-id help cpe-id generate-full-command-json-input'
    'network ip-sec-connection delete' = 'if-match from-json force generate-param-json-input ipsc-id help generate-full-command-json-input'
    'network ip-sec-connection get' = 'generate-param-json-input ipsc-id help from-json generate-full-command-json-input'
    'network ip-sec-connection get-config' = 'generate-param-json-input ipsc-id help from-json generate-full-command-json-input'
    'network ip-sec-connection get-status' = 'generate-param-json-input ipsc-id help from-json generate-full-command-json-input'
    'network ip-sec-connection list' = 'drg-id from-json page generate-param-json-input compartment-id help cpe-id generate-full-command-json-input limit'
    'network ip-sec-connection update' = 'if-match from-json display-name generate-param-json-input ipsc-id help generate-full-command-json-input'
    'network private-ip delete' = 'if-match from-json private-ip-id force generate-param-json-input help generate-full-command-json-input'
    'network private-ip get' = 'generate-param-json-input help generate-full-command-json-input from-json private-ip-id'
    'network private-ip list' = 'ip-address from-json page generate-param-json-input subnet-id help generate-full-command-json-input vnic-id limit'
    'network private-ip update' = 'if-match from-json private-ip-id display-name generate-param-json-input help generate-full-command-json-input hostname-label'
    'network route-table create' = 'vcn-id from-json route-rules display-name generate-param-json-input compartment-id help generate-full-command-json-input'
    'network route-table delete' = 'rt-id if-match from-json force generate-param-json-input help generate-full-command-json-input'
    'network route-table get' = 'generate-param-json-input rt-id help from-json generate-full-command-json-input'
    'network route-table list' = 'vcn-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network route-table update' = 'rt-id if-match from-json route-rules force display-name generate-param-json-input help generate-full-command-json-input'
    'network security-list create' = 'vcn-id from-json egress-security-rules display-name generate-param-json-input compartment-id help generate-full-command-json-input ingress-security-rules'
    'network security-list delete' = 'if-match from-json force generate-param-json-input security-list-id help generate-full-command-json-input'
    'network security-list get' = 'generate-param-json-input security-list-id help from-json generate-full-command-json-input'
    'network security-list list' = 'vcn-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network security-list update' = 'if-match from-json egress-security-rules force display-name generate-param-json-input security-list-id help generate-full-command-json-input ingress-security-rules'
    'network subnet create' = 'vcn-id dhcp-options-id from-json availability-domain security-list-ids route-table-id cidr-block display-name generate-param-json-input prohibit-public-ip-on-vnic compartment-id help dns-label generate-full-command-json-input'
    'network subnet delete' = 'if-match from-json force generate-param-json-input subnet-id help generate-full-command-json-input'
    'network subnet get' = 'generate-param-json-input subnet-id from-json help generate-full-command-json-input'
    'network subnet list' = 'vcn-id from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network subnet update' = 'if-match from-json display-name generate-param-json-input subnet-id help generate-full-command-json-input'
    'network vcn create' = 'from-json cidr-block display-name generate-param-json-input compartment-id help dns-label generate-full-command-json-input'
    'network vcn delete' = 'if-match vcn-id from-json force generate-param-json-input help generate-full-command-json-input'
    'network vcn get' = 'generate-param-json-input vcn-id help from-json generate-full-command-json-input'
    'network vcn list' = 'from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'network vcn update' = 'if-match vcn-id from-json display-name generate-param-json-input help generate-full-command-json-input'
    'network vnic assign-private-ip' = 'ip-address from-json hostname-label display-name generate-param-json-input help generate-full-command-json-input vnic-id unassign-if-already-assigned'
    'network vnic get' = 'generate-param-json-input vnic-id help from-json generate-full-command-json-input'
    'network vnic unassign-private-ip' = 'ip-address from-json generate-param-json-input help generate-full-command-json-input vnic-id'
    'network vnic update' = 'if-match from-json hostname-label display-name generate-param-json-input help generate-full-command-json-input vnic-id skip-source-dest-check'
    'os bucket create' = 'public-access-type namespace from-json name generate-param-json-input compartment-id help metadata generate-full-command-json-input'
    'os bucket delete' = 'if-match namespace from-json name force generate-param-json-input help generate-full-command-json-input'
    'os bucket get' = 'if-match namespace from-json name if-none-match generate-param-json-input help generate-full-command-json-input'
    'os bucket list' = 'namespace from-json page generate-param-json-input compartment-id help generate-full-command-json-input limit'
    'os bucket update' = 'if-match namespace public-access-type from-json name generate-param-json-input help metadata generate-full-command-json-input'
    'os multipart abort' = 'namespace from-json force object-name bucket-name generate-param-json-input upload-id help generate-full-command-json-input'
    'os multipart list' = 'namespace from-json page bucket-name generate-param-json-input help generate-full-command-json-input limit'
    'os ns get' = 'generate-param-json-input help from-json generate-full-command-json-input'
    'os object bulk-delete' = 'namespace from-json force dry-run delimiter bucket-name generate-param-json-input help generate-full-command-json-input prefix'
    'os object bulk-download' = 'namespace from-json overwrite no-overwrite download-dir bucket-name delimiter generate-param-json-input help generate-full-command-json-input prefix'
    'os object bulk-upload' = 'exclude namespace include object-prefix overwrite generate-full-command-json-input from-json no-overwrite content-type bucket-name content-encoding parallel-upload-count disable-parallel-uploads generate-param-json-input help metadata no-multipart content-language part-size src-dir'
    'os object delete' = 'if-match namespace from-json name force bucket-name generate-param-json-input help generate-full-command-json-input'
    'os object get' = 'if-match namespace from-json file name bucket-name if-none-match range generate-param-json-input help generate-full-command-json-input'
    'os object head' = 'if-match namespace from-json name bucket-name if-none-match generate-param-json-input help generate-full-command-json-input'
    'os object list' = 'namespace from-json end delimiter bucket-name generate-param-json-input fields start help generate-full-command-json-input limit prefix'
    'os object put' = 'if-match namespace content-md5 generate-full-command-json-input from-json file name force content-type bucket-name content-encoding parallel-upload-count generate-param-json-input help metadata no-multipart content-language part-size disable-parallel-uploads'
    'os object resume-put' = 'namespace generate-full-command-json-input from-json file name bucket-name generate-param-json-input parallel-upload-count upload-id help disable-parallel-uploads part-size'
    'os preauth-request create' = 'namespace opc-client-request-id access-type from-json time-expires name object-name bucket-name generate-param-json-input help generate-full-command-json-input'
    'os preauth-request delete' = 'namespace opc-client-request-id from-json force bucket-name generate-param-json-input help generate-full-command-json-input par-id'
    'os preauth-request get' = 'namespace opc-client-request-id from-json bucket-name generate-param-json-input help generate-full-command-json-input par-id'
    'os preauth-request list' = 'namespace opc-client-request-id generate-full-command-json-input from-json page bucket-name generate-param-json-input help limit object-name-prefix'
    'setup autocomplete' = 'help'
    'setup config' = 'help'
    'setup keys' = 'overwrite passphrase-file key-name help passphrase output-dir'
}
$script:ociCommandsWithLongParams = $ociCommandsToLongParams.Keys -join '|'

$ociCommandsToShortParams = @{
    'bv backup create' = '? h'
    'bv backup delete' = '? h'
    'bv backup get' = '? h'
    'bv backup list' = '? h c'
    'bv backup update' = '? h'
    'bv volume create' = '? h c'
    'bv volume delete' = '? h'
    'bv volume get' = '? h'
    'bv volume list' = '? h c'
    'bv volume update' = '? h'
    'compute console-history capture' = '? h'
    'compute console-history delete' = '? h'
    'compute console-history get' = '? h'
    'compute console-history get-content' = '? h'
    'compute console-history list' = '? h c'
    'compute image create' = '? h c'
    'compute image delete' = '? h'
    'compute image export to-object' = '? h ns bn'
    'compute image export to-object-uri' = '? h'
    'compute image get' = '? h'
    'compute image import from-object' = '? h ns bn c'
    'compute image import from-object-uri' = '? h c'
    'compute image list' = '? h c'
    'compute image update' = '? h'
    'compute instance action' = '? h'
    'compute instance attach-vnic' = '? h'
    'compute instance detach-vnic' = '? h c'
    'compute instance get' = '? h'
    'compute instance get-windows-initial-creds' = '? h'
    'compute instance launch' = '? h c'
    'compute instance list' = '? h c'
    'compute instance list-vnics' = '? h'
    'compute instance terminate' = '? h'
    'compute instance update' = '? h'
    'compute instance-console-connection create' = '? h'
    'compute instance-console-connection delete' = '? h'
    'compute instance-console-connection get' = '? h'
    'compute instance-console-connection list' = '? h c'
    'compute shape list' = '? h c'
    'compute vnic-attachment get' = '? h'
    'compute vnic-attachment list' = '? h c'
    'compute volume-attachment attach' = '? h'
    'compute volume-attachment detach' = '? h'
    'compute volume-attachment get' = '? h'
    'compute volume-attachment list' = '? h c'
    'db database create' = '? h'
    'db database delete' = '? h'
    'db database get' = '? h'
    'db database list' = '? h c'
    'db node get' = '? h'
    'db node list' = '? h c'
    'db node reset' = '? h'
    'db node soft-reset' = '? h'
    'db node start' = '? h'
    'db node stop' = '? h'
    'db system get' = '? h'
    'db system launch' = '? h c'
    'db system list' = '? h c'
    'db system terminate' = '? h'
    'db system update' = '? h'
    'db system-shape list' = '? h c'
    'db version list' = '? h c'
    'iam availability-domain list' = '? h c'
    'iam compartment create' = '? h c'
    'iam compartment get' = '? h c'
    'iam compartment list' = '? h c'
    'iam compartment update' = '? h c'
    'iam customer-secret-key create' = '? h'
    'iam customer-secret-key delete' = '? h'
    'iam customer-secret-key list' = '? h'
    'iam customer-secret-key update' = '? h'
    'iam group add-user' = '? h'
    'iam group create' = '? h c'
    'iam group delete' = '? h'
    'iam group get' = '? h'
    'iam group list' = '? h c'
    'iam group list-users' = '? h c'
    'iam group remove-user' = '? h c'
    'iam group update' = '? h'
    'iam policy create' = '? h c'
    'iam policy delete' = '? h'
    'iam policy get' = '? h'
    'iam policy list' = '? h c'
    'iam policy update' = '? h'
    'iam region list' = '? h'
    'iam region-subscription create' = '? h'
    'iam region-subscription list' = '? h'
    'iam user api-key delete' = '? h'
    'iam user api-key list' = '? h'
    'iam user api-key upload' = '? h'
    'iam user create' = '? h c'
    'iam user delete' = '? h'
    'iam user get' = '? h'
    'iam user list' = '? h c'
    'iam user list-groups' = '? h c'
    'iam user swift-password create' = '? h'
    'iam user swift-password delete' = '? h'
    'iam user swift-password list' = '? h'
    'iam user swift-password update' = '? h'
    'iam user ui-password create-or-reset' = '? h'
    'iam user update' = '? h'
    'iam user update-user-state' = '? h'
    'network cpe create' = '? h c'
    'network cpe delete' = '? h'
    'network cpe get' = '? h'
    'network cpe list' = '? h c'
    'network cpe update' = '? h'
    'network dhcp-options create' = '? h c'
    'network dhcp-options delete' = '? h'
    'network dhcp-options get' = '? h'
    'network dhcp-options list' = '? h c'
    'network dhcp-options update' = '? h'
    'network drg create' = '? h c'
    'network drg delete' = '? h'
    'network drg get' = '? h'
    'network drg list' = '? h c'
    'network drg update' = '? h'
    'network drg-attachment create' = '? h'
    'network drg-attachment delete' = '? h'
    'network drg-attachment get' = '? h'
    'network drg-attachment list' = '? h c'
    'network drg-attachment update' = '? h'
    'network internet-gateway create' = '? h c'
    'network internet-gateway delete' = '? h'
    'network internet-gateway get' = '? h'
    'network internet-gateway list' = '? h c'
    'network internet-gateway update' = '? h'
    'network ip-sec-connection create' = '? h c'
    'network ip-sec-connection delete' = '? h'
    'network ip-sec-connection get' = '? h'
    'network ip-sec-connection get-config' = '? h'
    'network ip-sec-connection get-status' = '? h'
    'network ip-sec-connection list' = '? h c'
    'network ip-sec-connection update' = '? h'
    'network private-ip delete' = '? h'
    'network private-ip get' = '? h'
    'network private-ip list' = '? h'
    'network private-ip update' = '? h'
    'network route-table create' = '? h c'
    'network route-table delete' = '? h'
    'network route-table get' = '? h'
    'network route-table list' = '? h c'
    'network route-table update' = '? h'
    'network security-list create' = '? h c'
    'network security-list delete' = '? h'
    'network security-list get' = '? h'
    'network security-list list' = '? h c'
    'network security-list update' = '? h'
    'network subnet create' = '? h c'
    'network subnet delete' = '? h'
    'network subnet get' = '? h'
    'network subnet list' = '? h c'
    'network subnet update' = '? h'
    'network vcn create' = '? h c'
    'network vcn delete' = '? h'
    'network vcn get' = '? h'
    'network vcn list' = '? h c'
    'network vcn update' = '? h'
    'network vnic assign-private-ip' = '? h'
    'network vnic get' = '? h'
    'network vnic unassign-private-ip' = '? h'
    'network vnic update' = '? h'
    'os bucket create' = '? h ns c'
    'os bucket delete' = '? h ns'
    'os bucket get' = '? h ns'
    'os bucket list' = '? h ns c'
    'os bucket update' = '? h ns'
    'os multipart abort' = '? h on ns bn'
    'os multipart list' = '? h ns bn'
    'os ns get' = '? h'
    'os object bulk-delete' = '? h ns bn'
    'os object bulk-download' = '? h ns bn'
    'os object bulk-upload' = '? h ns bn'
    'os object delete' = '? h ns bn'
    'os object get' = '? h ns bn'
    'os object head' = '? h ns bn'
    'os object list' = '? h ns bn'
    'os object put' = '? h ns bn'
    'os object resume-put' = '? h ns bn'
    'os preauth-request create' = '? h on ns bn'
    'os preauth-request delete' = '? h ns bn'
    'os preauth-request get' = '? h ns bn'
    'os preauth-request list' = '? h ns bn'
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