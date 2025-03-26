from django.shortcuts import render
from .models import Project

def dashboard_view(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'projects': projects})
