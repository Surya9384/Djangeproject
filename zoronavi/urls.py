"""
URL configuration for anima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path 
from zoronavi import views

urlpatterns = [ 
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('indextwo', views.indextwo, name='indextwo'),
    path('post_details', views.post_details, name='post_details'),
     path('index', views.index, name='index'),
      path('privacy', views.privacy, name='privacy'),

]
