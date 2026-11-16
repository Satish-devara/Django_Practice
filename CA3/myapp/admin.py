from django.contrib import admin
from .models import Teacher, Feedback

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "department")
    search_fields = ("name", "subject", "department")
    ordering = ("name",)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("student", "teacher", "rating", "created_at")
    list_filter = ("rating", "teacher", "created_at")
    search_fields = ("student__username", "teacher__name", "comments")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
