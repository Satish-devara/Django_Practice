from django.urls import path
from . import views

urlpatterns = [
    path("", views.students_list, name ="students_list"),
    path("add_student/", views.add_student, name="add_student"),
    path("update_detail/<int:id>/", views.update_detail, name="update_detail"),
    path("delete_student/<int:id>/", views.delete_detail, name="delete_detail")

]