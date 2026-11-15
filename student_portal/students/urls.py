from django.urls import path, re_path
from . import views


urlpatterns=[
    path("list/", views.get_students),
    path("form/", views.view_Form),
    path("product/", views.add_product),
    path("success/", views.success, name='success'),
    path("department/", views.dprt),
    path("teachers/", views.teachers),
]