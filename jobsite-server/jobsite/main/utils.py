import string
import random
import secrets
import json

from django.core import serializers


class Utils:
    @staticmethod
    def model_to_dict(obj):
        return json.loads(serializers.serialize('json', [obj]))[0]['fields']

    @staticmethod
    def random_hex(length):
        return secrets.token_hex(length)

    @staticmethod
    def random_string(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))
    