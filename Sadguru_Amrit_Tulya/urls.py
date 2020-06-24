"""Sadguru_Amrit_Tulya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from testapp import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.TeaList_view.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', views.TeaDetail_view.as_view(), name='detail'),
    url(r'^create/', views.Teacreateview.as_view()),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateTea.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.Tea_Delete_view.as_view()),
    url(r'^api/', include('testapp.api.urls'))

]
