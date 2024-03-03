from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def teachers(request):
    return render(request, 'main/about.html')


def lessons(request):
    return render(request, 'main/game.html')



