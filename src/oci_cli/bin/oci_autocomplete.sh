# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

_bmcs_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _BMCS_COMPLETE=complete $1 ) )
    return 0
}

_oci_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _OCI_COMPLETE=complete $1 ) )
    return 0
}

complete -F _bmcs_completion -o default bmcs;
complete -F _oci_completion -o default oci;