import hashlib
import random
import string


async def gen_key(key_length: int = 8):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(key_length)
    )


async def hash_password(password: str, salt: str):
    salted_pass = password.encode('utf-8') + salt.encode('utf-8')

    hashed_pass = hashlib.sha256()
    hashed_pass.update(salted_pass)

    return hashed_pass.hexdigest()


class Pagination:
    def __init__(self, limit: int = 100, offset: int = 0):
        self.limit = limit
        self.offset = offset

