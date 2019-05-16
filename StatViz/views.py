from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)