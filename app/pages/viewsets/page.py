from rest_framework.viewsets import ModelViewSet

from ..models import Page
from ..serializers.page import (
    PageSerializer,
    PageDetailSerializer,
    PageListSerializer,
    PageCreateUpdateSerializer,
)


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    ordering = ('id',)
    filterset_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        elif self.action == 'create' or self.action == 'update':
            return PageCreateUpdateSerializer
        elif self.action == 'retrieve':
            return PageDetailSerializer
        else:
            return PageSerializer
