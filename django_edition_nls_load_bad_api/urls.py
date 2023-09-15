from django.contrib import admin
from django.urls import path
from myapp.views import sync_data_with_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sync/', sync_data_with_api, name='sync_data_with_api'),
]
