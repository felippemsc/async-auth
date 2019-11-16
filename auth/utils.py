import random
import string


def gen_key(key_length: int = 8):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(key_length)
    )
