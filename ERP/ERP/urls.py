"""ERP URL Configuration

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
from django.urls import path, include
from sales.views import sales_index_view
from pur.views import pur_index_view
from accounts.views import accounts_index_view
from sales import urls as sales_urls
from accounts import urls as accounts_urls
from pur import urls as pur_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("sales/",include(sales_urls)),
    path("pur/",include(pur_urls)),
    path("accounts/",include(accounts_urls)),
]
