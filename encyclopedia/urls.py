from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("editPage/<str:TITLE>", views.editPage, name="editPage"),
    path("random", views.randomPage, name="randomPage")
]
