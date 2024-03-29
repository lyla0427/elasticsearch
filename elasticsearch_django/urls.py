"""elasticsearch_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers

from apps.views import ArticleDocumentView, ArticleView, ArticleESView

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'articles-drf', ArticleDocumentView, basename='article')
router.register(r'articles-dsl', ArticleView, basename='article')
router.register(r'articles-es', ArticleESView, basename='article')



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls