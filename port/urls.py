from django.urls import path
from port import views

urlpatterns = [
    path('', views.home , name="home" ),
    path('about/',views.about,name="about"),
    path('projects/',views.projects, name="projects"),
    path('contact',views.contact,name="contact"),
    path('success',views.success,name="success"),
]