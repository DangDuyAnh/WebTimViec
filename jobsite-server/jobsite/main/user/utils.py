import datetime
import jwt
from django.conf import settings

from .model import User


def generate_access_token(user: User):
    date_time_now = datetime.datetime.utcnow()
    access_token_payload = {
        'user_id': user.id,
        'exp': date_time_now + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
        'iat': date_time_now,
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256')

    return access_token, access_token_payload['exp']


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
        'user_info': {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username
        }
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256').decode('utf-8')

    return refresh_token