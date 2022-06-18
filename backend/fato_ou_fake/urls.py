from .api import ListFatoFake

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', ListFatoFake.as_view(), name='fatos'),
]