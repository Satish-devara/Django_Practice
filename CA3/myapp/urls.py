from django.urls import path
from .views import StudentLoginView, submit_feedback, feedback_confirmation, my_feedback, student_logout

urlpatterns = [
    path("", submit_feedback, name="submit_feedback"),
    path("login/", StudentLoginView.as_view(), name="login"),
    path("logout/", student_logout, name="logout"),
    path("confirmation/<int:feedback_id>/", feedback_confirmation, name="feedback_confirmation"),
    path("my-feedback/", my_feedback, name="my_feedback"),
]
