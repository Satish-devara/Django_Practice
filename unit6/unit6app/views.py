from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(
        request,
        "index.html"
    )


def set(request):
    response = HttpResponse("Cookies Value Set Successfully")
    response.set_cookie("username", count, max_age=60)

    return response
# Create your views here.

def get(request):
    value = request.COOKIES.get("username")
    return HttpResponse(f"Cookies Value is {value}")

def delete(request):
    response = HttpResponse("Cookie Deleted Successfully")
    response.delete_cookie("username")

    return response

def visit(request):
    response = HttpResponse("Cookie value set succesfully")
    response.set_cookie("visit", 0, max_age=60)
    return response

def visitagain(request):
    visit = request.COOKIES.get("visit")
    visit += 1
    response = HttpResponse("Cokkie updated")
    response.set_cookie("visit", visit, max_age=60)
    return response

def set_session(request):
    request.session['studentname'] = 'Satish'
    return HttpResponse("Session data set")

def get_session(request):
    studentname  = request.session.get("studentname", "Guest")
    return render(
        request,
        "get_session.html",
        {
            "studentname": studentname,
        }
    )

def delete_session(request):
    request.session.pop('username', None)
    return render(request, "get_session.html",{"message":"No session is there"})

def update_session(request):
    request.session["username"] = 'Sai'
    return render(request, "get_session.html")