"""
URL configuration for django_project_nls_load_bad_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp1.views import index_page
from myapp1.views import sync_data_with_api

urlpatterns = [
    path('admin/', admin.site.urls),
     # при обращении к главной странице должна запускаться функция index_page
	path('', index_page),
    path('sync_data/', sync_data_with_api, name='sync_data'),
]
