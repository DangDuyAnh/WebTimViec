from rest_framework import serializers
from .models import Province
 
class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'area_code']
