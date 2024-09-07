from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]