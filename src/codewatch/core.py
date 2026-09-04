"""Change tracking for text snapshots."""

def diff(before: str, after: str) -> dict[str, int]:
    """Return simple line-level change counts."""
    old, new = before.splitlines(), after.splitlines()
    common = sum(a == b for a, b in zip(old, new))
    return {"before": len(old), "after": len(new), "changed": max(len(old), len(new)) - common}
