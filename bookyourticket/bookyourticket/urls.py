"""bookyourticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from bookticket import urls as bookticket_urls
from api import urls as api_urls
from django.conf import settings 
from django.conf.urls.static import static
from bookticket.googleauth import redirect_view, google_auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("bookticket/",include(bookticket_urls)),
    path("api/",include(api_urls)),
    path("googleauthentication/",google_auth_view),
    path("oauth2redirect/", redirect_view)
]
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
