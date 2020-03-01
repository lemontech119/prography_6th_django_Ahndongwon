from django.contrib import admin
from subject.models import Subject

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'Modified_at')