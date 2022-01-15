from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def anons(request):
    return render(request, 'main/anonsment.html')
