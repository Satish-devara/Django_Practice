from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("set/", views.set),
    path("get/", views.get),
    path("delete/", views.delete),
    path("visit/", views.visit),
    path("visitagain/", views.visitagain),
    path("set_session/", views.set_session),
    path("get_session/", views.get_session),
    path("delete_session/", views.delete_session),
    path("update_session/", views.update_session),
]