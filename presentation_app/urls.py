# presentation_app/urls.py
from . import views
from django.urls import path
from .views import presentation

urlpatterns = [
    path('', presentation, name='presentation'),
    path('sl/', views.presentation2, name='presentation2'),
    path('slides/', views.presentation3, name='presentation3'),
    path('slidex/<int:slide_number>/', views.slidex, name='slidex'),
    path('slide/', views.slide, name='slide'),
]
