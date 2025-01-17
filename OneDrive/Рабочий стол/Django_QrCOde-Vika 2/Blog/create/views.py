from django.shortcuts import render

def render_free(request):
    return render(request, 'free.html')
# Create your views here.
def render_standard(request):
    return render(request, 'standard.html')

def render_pro(request):
    return render(request, 'pro.html')