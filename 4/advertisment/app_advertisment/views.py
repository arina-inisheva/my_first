from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')


def main_page(request):
    return render(request, 'index.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register_html(request):
    return render(request, 'register.html')
def login_html(request):
    return render(request, 'login.html' )

def profile_html(request):
    return  render(request, 'profile.html')