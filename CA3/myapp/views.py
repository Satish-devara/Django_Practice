from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import FeedbackForm
from .models import Feedback, Teacher

class StudentLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

@login_required
def submit_feedback(request):
    initial = {}
    last_teacher_id = request.session.get("last_selected_teacher")
    if last_teacher_id and Teacher.objects.filter(pk=last_teacher_id).exists():
        initial["teacher"] = last_teacher_id

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = request.user
            feedback.save()
            request.session["last_selected_teacher"] = feedback.teacher_id
            request.session.modified = True
            return redirect("feedback_confirmation", feedback_id=feedback.pk)
    else:
        form = FeedbackForm(initial=initial)

    return render(request, "submit_feedback.html", {"form": form})

@login_required
def feedback_confirmation(request, feedback_id):
    feedback = get_object_or_404(
        Feedback, pk=feedback_id, student=request.user
    )
    return render(request, "confirmation.html", {"feedback": feedback})

@login_required
def my_feedback(request):
    
    feedback_list = Feedback.objects.filter(student=request.user).select_related("teacher")
    return render(request, "my_feedback.html", {"feedback_list": feedback_list})

@require_POST
def student_logout(request):
    logout(request)
    return redirect("login")
