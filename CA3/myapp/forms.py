from django import forms
from .models import Feedback, Teacher

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["teacher", "rating", "comments"]
        widgets = {
            "teacher": forms.Select(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-control"}),
            "comments": forms.Textarea(attrs={
                "class": "form-control", "rows": 5,
                "placeholder": "Share constructive feedback (max 1000 characters)..."
            }),
        }

    def clean_comments(self):
        comments = self.cleaned_data["comments"].strip()
        if len(comments) < 10:
            raise forms.ValidationError("Please enter at least 10 characters.")
        return comments

    def clean_teacher(self):
        teacher = self.cleaned_data["teacher"]
        if not Teacher.objects.filter(pk=teacher.pk).exists():
            raise forms.ValidationError("Please select a valid teacher.")
        return teacher
