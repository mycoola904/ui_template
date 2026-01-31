from django.urls import path
from . import views

app_name = "ui"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tables/", views.tables, name="tables"),
    path("forms/", views.forms, name="forms"),
]
