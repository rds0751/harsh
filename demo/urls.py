# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ContactView, contacts

urlpatterns = [
    url(r'^$', ContactView.as_view(), name='demo'),
    url(r'^demos-list/', contacts, name='demos'),
]
