from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'student_class', 'email', 'created_at')
    list_filter = ('student_class',)
    search_fields = ('name', 'roll_number', 'email')
    ordering = ('-created_at',)
