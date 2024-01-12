from django.urls import path
from . import views

urlpatterns = [
    path("", views.csv_plotter, name="csv_plotter")
]