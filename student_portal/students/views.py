from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse, Http404
from .models import student,Product, Department, Teacher
import datetime


def get_students(request):
    students = [
        {
            "name": "Satish",
            "attendance":85
        },
        {
            "name": "Rahul",
            "attendance":65
        },
    ]

    return render(
        request,
        "students/list.html",
        {
            "students": students
        }
    )

def view_Form(request):
    if request.method=='POST':
        name = request.POST.get("name")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        course = request.POST.get("course")

        std = student()
        std.name = name
        std.city = city
        std.phone = phone
        std.course = course
        std.save()
        return render(request,
                    "students/form.html",
                )
        

    return render(request,
                    "students/form.html",
                )

def success(request):
    return HttpResponse("form Submitted")


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        available = request.POST.get("available") == "on"
        
        prd = Product()
        prd.name = name
        prd.description = description
        prd.available = available
        prd.price = price
        
        prd.save()

        return render(request, 
                        "students/product.html")

    return render(request, 
                        "students/product.html")

def dprt(request):
    data = Department.objects.all()
    return render(request, "students/dprt.html", {"data":data})

def teachers(request):
    data1 = Teacher.objects.all()
    return render(request, "students/teacher.html", {"data1":data1})