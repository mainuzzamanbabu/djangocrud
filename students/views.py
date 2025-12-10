from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q  # 🆕 Import Q for OR conditions
from .models import Student
from .forms import StudentForm


# ========== LIST VIEW (with Search, Filter, Sorting & Pagination) ==========
def student_list(request):
    """Display students with search, filter, sorting and pagination"""
    
    # Start with all students
    students = Student.objects.all()
    
    # 🔍 SEARCH FUNCTIONALITY
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |           # Search in name
            Q(roll_number__icontains=search_query) |    # Search in roll
            Q(email__icontains=search_query)            # Search in email
        )
    
    # 🎛️ FILTER BY CLASS
    class_filter = request.GET.get('class', '')
    if class_filter:
        students = students.filter(student_class=class_filter)
    
    # ↕️ SORTING
    sort_by = request.GET.get('sort', '-created_at')  # Default: newest first
    # Validate sort field to prevent errors
    allowed_sort_fields = ['name', '-name', 'roll_number', '-roll_number', 
                           'student_class', '-student_class', 'created_at', '-created_at']
    if sort_by in allowed_sort_fields:
        students = students.order_by(sort_by)
    else:
        students = students.order_by('-created_at')
    
    # 📄 PAGINATION (10 per page)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    
    # 📦 Pass everything to template
    context = {
        'students': students,
        'search_query': search_query,
        'class_filter': class_filter,
        'sort_by': sort_by,
        'class_choices': Student.CLASS_CHOICES,  # For dropdown
    }
    return render(request, 'students/student_list.html', context)


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
