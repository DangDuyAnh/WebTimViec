import string
import random
import secrets
import json
from dateutil.parser import parse as date_parse

from django.core import serializers



class Utils:
    @staticmethod
    def model_to_dict(obj):
        obj = json.loads(serializers.serialize('json', [obj]))[0]
        fields = obj['fields']
        pk =  { 
            #'pk': obj['pk'],
            'id': obj['pk']
        }
        return  pk | fields

    @staticmethod
    def query_set_to_list(query_set):
        arr = []
        for p in query_set.iterator():
            arr.append(Utils.model_to_dict(p))
        return arr

        from dateutil.parser import parse

    @staticmethod
    def date_parse(string, fuzzy=False):
        """
        Return whether the string can be interpreted as a date.

        :param string: str, string to check for date
        :param fuzzy: bool, ignore unknown tokens in string if True
        """
        try: 
            return date_parse(string, fuzzy=fuzzy)
        except ValueError:
            return None

    @staticmethod
    def std_dict(d: dict):
        ret = dict()
        for k, v in d.items():
            if type(v) == str:
                if v.isdigit():
                    ret[k] = int(v)
                    continue
                
                date = Utils.date_parse(v)
                if date is not None:
                    ret[k] = date
                    continue

            ret[k] = v

        return ret

    @staticmethod
    def random_hex(length):
        return secrets.token_hex(length)

    @staticmethod
    def random_string(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))
    