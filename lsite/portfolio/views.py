from django.shortcuts import render
from django.http import Http404


def IndexView(request):
    return render(request, 'portfolio/index.html')
