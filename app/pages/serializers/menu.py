from rest_framework.serializers import ModelSerializer
from ..serializers import BaseSerializer
from ..models import Menu


class MenuSerializer(BaseSerializer):
    class Meta:
        model = Menu
        exclude = ('created_time', 'updated_time')


class MenuListSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'slug', 'menu_id', 'sequence', 'status', 'created_time', 'updated_time']


class MenuCreateUpdateSerializer(BaseSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'slug', 'menu_id', 'sequence', 'status']


class MenuDetailSerializer(BaseSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'slug', 'menu_id', 'sequence', 'status', 'created_time', 'updated_time']
