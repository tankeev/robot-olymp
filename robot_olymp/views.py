from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'category.html')