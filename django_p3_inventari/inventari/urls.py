from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("exemplars/", views.llista_productes, name="exemplars"),
]