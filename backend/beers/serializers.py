from rest_framework import serializers
from .models import BeerModel


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BeerModel
        fields = '__all__'
