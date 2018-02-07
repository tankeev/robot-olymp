from django.shortcuts import render

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

