from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')


def index(request):
    return render(request, 'index.html')