from django.contrib import admin
from django.urls import path
from mainproject.core.views import index, portifolio_details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'index'),
    path('produtos/', portifolio_details, name = 'produtos')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)