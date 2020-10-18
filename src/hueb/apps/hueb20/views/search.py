from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def search(request):
    return render(request, "hueb20/search.html")
