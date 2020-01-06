import random
import string

from faker import Faker
from faker.providers import BaseProvider

from auth.constants import MIN_LENGTH_PASS, MAX_LENGTH_PASS

fake = Faker()


class Provider(BaseProvider):
    def password(self):
        length = random.randrange(MIN_LENGTH_PASS, MAX_LENGTH_PASS)
        random_source = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!$@#%&*/?;:|][}{~^"

        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice("!$@#%&*/?;:|][}{~^")

        for i in range(length - 4):
            password += random.choice(random_source)

        password = list(password)
        random.shuffle(password)

        return ''.join(password)


fake.add_provider(Provider)
