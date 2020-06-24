





from django.contrib import admin
from django.urls import path,include
from testapp import views
from django.conf.urls import url
from testapp.api.views import TeaCRUD

from rest_framework import routers
router=routers.DefaultRouter()
router.register('teainfo',TeaCRUD)
urlpatterns = [
    url(r'',include(router.urls)),
]