import hashlib

def md5(string: str) -> str:
    result = hashlib.md5(string.encode('utf-8')).hexdigest()
    print(result)
    return result