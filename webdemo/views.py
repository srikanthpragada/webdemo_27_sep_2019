from django.http import HttpResponse
import datetime


def welcome(request):
    return HttpResponse("<h1 style='color:red'>Welcome To Django</h1>")


def wish(request):
    # check whether name parameter is passed
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    hour = datetime.datetime.now().hour
    if hour < 12:
        msg = "Good Morning"
    elif hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1 style='color:blue'>{msg} {name}</h1>")
