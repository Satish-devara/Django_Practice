from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Department
def students_list(request):
    students = Student.objects.all()

    return render(request, 'students.html', {'students':students})


def add_student(request):

    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        cgpa = request.POST.get('cgpa')
        department_id = request.POST.get('department')

        department = Department.objects.get(id=department_id)

        Student.objects.create(
            name = name,
            roll_no = roll_no,
            cgpa = cgpa,
            Department = department
        )
        return render(request, 'students.html')
    
    return render(request, 'add_student.html', {'departments':departments})


def update_detail(request, id):
    student = get_object_or_404(Student, id=id)

    departments = Department.objects.all()

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_no = request.POST.get('roll_no')
        student.cgpa = request.POST.get('cgpa')
        department_id = request.POST.get('department')

        student.Department  = Department.objects.get(id=department_id)

        student.save()

        return redirect('students_list')
    

    return render(request, 'update_details.html', {
        'student':student,
        'departments':departments
    })


def delete_detail(request, id):
    student = get_object_or_404(Student,id=id)

    student.delete()

    return redirect('students_list')






# Create your views here.
