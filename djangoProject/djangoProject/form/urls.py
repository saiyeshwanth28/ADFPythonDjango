from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration.as_view()),
]