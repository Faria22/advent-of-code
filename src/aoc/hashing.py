import hashlib


def get_hash(key: str) -> str:
    return hashlib.md5(key.encode()).hexdigest()
