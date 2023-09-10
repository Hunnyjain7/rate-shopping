import random
import uuid


def get_uuid():
    return uuid.uuid4


def get_random_number():
    return str(random.randint(0, 99999999))
