from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Student
from .forms import StudentForm


# ========== LIST VIEW (with Pagination) ==========
def student_list(request):
    """Display all students with pagination (10 per page)"""
    student_queryset = Student.objects.all()
    
    # Pagination: 10 items per page
    paginator = Paginator(student_queryset, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {
        'students': students
    })


# ========== ADD VIEW ==========
def student_add(request):
    """Add a new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add New Student'
    })


# ========== EDIT VIEW ==========
def student_edit(request, pk):
    """Edit an existing student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student',
        'student': student
    })


# ========== DELETE VIEW ==========
def student_delete(request, pk):
    """Delete a student with confirmation"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    
    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })
