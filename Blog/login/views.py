from django.shortcuts import render
# Create your views here.

def render_login(request):
    return render(request, 'login.html')

def render_registr(request):
    return render(request, 'registration.html')