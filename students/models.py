from django.db import models


class Student(models.Model):
    """Student model for CRUD operations"""
    
    # Choices for class/grade
    CLASS_CHOICES = [
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
    ]
    
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    student_class = models.CharField(max_length=2, choices=CLASS_CHOICES, default='6')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
    
    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number})"
