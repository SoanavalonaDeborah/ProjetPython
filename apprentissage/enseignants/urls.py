from django.urls import path
from . import views

urlpatterns = [
    path('enseignants/', views.enseignants, name='enseignants'),
]
