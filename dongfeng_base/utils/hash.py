import hashlib


def md5(string: str) -> str:
    encoder = hashlib.md5()
    encoder.update(str(string).encode(encoding="utf-8"))
    return encoder.hexdigest()
