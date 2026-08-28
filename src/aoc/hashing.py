import hashlib


def get_hash(key: str) -> str:
    """Return the hexadecimal MD5 digest of a string."""
    return hashlib.md5(key.encode()).hexdigest()
