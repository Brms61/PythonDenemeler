from django.urls import path
from django.contrib import admin

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]