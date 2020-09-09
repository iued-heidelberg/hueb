from django.shortcuts import render


def hello(request):
    return render(request, "hueb20/base.html")
