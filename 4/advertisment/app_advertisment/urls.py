from django.urls import path
from .views import index, top_sellers, main_page, advertisement_post, register_html, login_html, profile_html

urlpatterns = [
    path('', index),
    path('start', index),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('main_page', main_page, name='main_page'),
    path('advertisement_post', advertisement_post, name= 'advertisement_post'),
    path('register_html', register_html, name= 'register_html'),
    path('login_html', login_html, name= 'login_html'),
    path('profile_html', profile_html, name= 'profile_html')
]
