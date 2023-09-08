"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# projectname/urls.py


from django.contrib import admin
from django.conf import settings
from django.urls import path, include

if not settings.DEBUG:
    # Set APPEND_SLASH to False for non-debug mode
    from django.urls import register_converter
    from django.urls.converters import SlugConverter
    register_converter(SlugConverter, 'slug')
    APPEND_SLASH = False


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kush.urls')), 
]

