from rest_framework.serializers import ModelSerializer
from ..serializers import BaseSerializer
from ..models import Page


class PageSerializer(BaseSerializer):
    class Meta:
        model = Page
        exclude = ('created_time', 'updated_time')


class PageListSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'menu_id', 'status', 'created_time', 'updated_time']


class PageCreateUpdateSerializer(BaseSerializer):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'menu_id', 'status', 'small_content', 'content']


class PageDetailSerializer(BaseSerializer):
    class Meta:
        model = Page
        fields = [
            'id', 'title', 'slug', 'menu_id', 'sequence', 'status',
            'small_content', 'content', 'created_time', 'updated_time'
        ]
