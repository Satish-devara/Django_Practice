from django.conf import settings
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} — {self.subject}"


class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="submitted_feedback"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, related_name="feedback_entries"
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comments = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student.username} → {self.teacher.name} ({self.rating}/5)"


