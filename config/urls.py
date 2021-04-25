"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from pybo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    # 프로젝트의 짜임새를 전혀 고려하지 않음 -> urls.py 파일을 따로 구성해서 include로 구조를 잡자 
    # path('pybo/', views.index),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
]

