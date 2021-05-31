'''
Urls for shortener app urlshortener/urls.py
'''
from django.urls import path

# Import the home view
from link.views import redirect_url, home_view
from django.conf import settings
from django.conf.urls.static import static

appname = "shortener"

urlpatterns = [
    path('', home_view, name="home"),
    path('<str:short_hash>', redirect_url, name='redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
