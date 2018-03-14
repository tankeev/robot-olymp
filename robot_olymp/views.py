from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'registration/profile.html')

def category(request):
    return render(request, 'category.html')


def index(request):
    return render(request, 'index.html')
    
def auth_password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


def auth_password_change_done(request):
    return render(request, 'registration/password_change_done.html')


def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')

def sumo(request):
    image_data = open("staticfiles/pdf/1-LEGO_SUMO.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

def lego_line_follower(request):
    image_data = open("staticfiles/pdf/2-LEGO_LINEFOLLOWER.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")


def arduino_line_follower(request):
    image_data = open("staticfiles/pdf/3-ARDUINO_LINEFOLLOWER.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")


def ollo_race(request):
    image_data = open("staticfiles/pdf/4-OLLO_RACE.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

def ollo_ball(request):
    image_data = open("staticfiles/pdf/5-OLLO_BALL.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

def result(request):
    image_data = open("staticfiles/pdf/result.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

