from . import views
from django.urls import path

urlpatterns = [
	path('', views.home, name = "site-home"),
	path('about/', views.about, name ='site-about')
]

