from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('news/<int:id>/', views.news, name="news"),
     path('about/', views.about, name="about")
]