from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """Form for adding and editing students"""
    
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email', 'student_class']
        
        # Add styling to form fields
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter student name'
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter roll number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter email (optional)'
            }),
            'student_class': forms.Select(attrs={
                'class': 'form-input'
            }),
        }
