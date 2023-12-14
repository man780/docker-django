from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.menu import MenuViewSet
from .viewsets.page import PageViewSet

app_name = 'pages'

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'page', PageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
