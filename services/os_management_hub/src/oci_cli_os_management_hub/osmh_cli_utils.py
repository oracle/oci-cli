import json
from typing import Iterable, List, Optional, Sequence, Union

import click

_ALLOWED_UPDATE_TYPES = {
    "SECURITY",
    "BUGFIX",
    "ENHANCEMENT",
    "OTHER",
    "KSPLICE_KERNEL",
    "KSPLICE_USERSPACE",
    "ALL",
}


def normalize_update_types(
    update_types: Union[None, str, Sequence[str]]
) -> Optional[List[str]]:
    """
    Normalize update types input for os-management-hub "update all packages" commands.

    Accepts:
    - JSON array: '["SECURITY","BUGFIX"]'
    - JSON string: '"SECURITY"'
    - Plain value: 'SECURITY'
    - Comma-separated: 'SECURITY,BUGFIX'
    - Repeated flags (Click multiple=True): --update-types SECURITY --update-types BUGFIX
    """
    if update_types is None:
        return None

    if isinstance(update_types, str):
        raw_values: Iterable[str] = [update_types]
    else:
        raw_values = list(update_types)

    collected: List[str] = []
    invalid: List[str] = []

    for raw in raw_values:
        if raw is None:
            continue

        raw_str = str(raw).strip()
        if not raw_str:
            continue

        parts = _split_update_types(raw_str)
        for part in parts:
            token = str(part).strip().strip('"').strip("'").strip()
            if not token:
                continue

            token_upper = token.upper()
            if token_upper not in _ALLOWED_UPDATE_TYPES:
                invalid.append(token)
                continue

            if token_upper not in collected:
                collected.append(token_upper)

    if invalid:
        allowed = ", ".join(sorted(_ALLOWED_UPDATE_TYPES))
        bad = ", ".join(invalid)
        raise click.UsageError(
            f"Invalid --update-types value(s): {bad}. Allowed values: {allowed}."
        )

    return collected or None


def _split_update_types(raw: str) -> List[str]:
    s = raw.strip()

    # Allow JSON array/string forms (common in OCI CLI for list parameters)
    if s[:1] in ("[", '"'):
        try:
            parsed = json.loads(s)
        except Exception:
            parsed = None

        if isinstance(parsed, list):
            return [str(x) for x in parsed]
        if isinstance(parsed, str):
            return [parsed]

    # Allow comma-separated without requiring JSON
    if "," in s:
        return [p.strip() for p in s.split(",") if p.strip()]

    return [s]
