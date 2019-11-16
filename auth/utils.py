import random
import string


def gen_key(key_length: int = 8):
    return str(key_length)
    # key = ''.join(
    #     random.choice(string.ascii_uppercase + string.digits) for _ in range(key_length)
    # )
    # return key
