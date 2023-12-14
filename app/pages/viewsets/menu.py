from rest_framework.viewsets import ModelViewSet

from ..models import Menu
from ..serializers.menu import (
    MenuSerializer,
    MenuDetailSerializer,
    MenuListSerializer,
    MenuCreateUpdateSerializer,
)


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    ordering = ('id',)
    filterset_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return MenuListSerializer
        elif self.action == 'create' or self.action == 'update':
            return MenuCreateUpdateSerializer
        elif self.action == 'retrieve':
            return MenuDetailSerializer
        else:
            return MenuSerializer
