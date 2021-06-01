'''
Urls for shortener app urlshortener/urls.py
'''
from django.urls import path

# Import the home view
from link.views import redirect_url, home_view


appname = "shortener"

urlpatterns = [
    path('', home_view, name="home"),
    path('<str:short_hash>', redirect_url, name='redirect'),
] 
