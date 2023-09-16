from django.contrib import admin
from django.urls import path
from myapp1.views import index_page
from myapp1.sync import synchronize_data  # Импорт функции из sync.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index_page'),
    # Удалите или закомментируйте ссылку на sync_data_with_api
    # path('sync_data/', sync_data_with_api, name='sync_data_with_api'),
]
