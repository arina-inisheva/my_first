from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Advertisement
from .Forms import  AdvertisementForm



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

def advertisment(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)