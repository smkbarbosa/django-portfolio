from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def project_list(request):
    return render(request, 'projects/index.html')
