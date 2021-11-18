from django.urls import path
from ResultsApp import views

urlpatterns = [
    path('results', views.results, name="results"),
]