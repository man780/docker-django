from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pages/', include('pages.urls')),
    path('api-auth/', include('djoser.urls')),
    path('api-auth/', include('djoser.urls.jwt')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Ucell New site"
admin.site.site_header = "Ucell site admin panel"
admin.site.site_title = "Ucell site"
