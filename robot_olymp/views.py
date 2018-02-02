from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def category(request):
    return render(request, 'category.html')