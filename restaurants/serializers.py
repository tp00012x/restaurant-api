from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('pk', 'name', 'opening_time', 'closing_time', 'is_open')

    @staticmethod
    def get_is_open(instance):
        return instance.is_open
