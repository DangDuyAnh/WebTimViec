from rest_framework import serializers
from .model import User
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'joined_date']


class UserFullSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 
                'social_account', 'social_account_id', 'social_auth_iss', 'joined_date', 'token', 'token_expires']