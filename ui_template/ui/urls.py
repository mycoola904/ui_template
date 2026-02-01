from django.urls import path
from . import views
from .views import table_demo, panel_demo

app_name = "ui"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tables/", views.tables, name="tables"),
    path("forms/", views.forms, name="forms"),
    path("tables/demo/", table_demo, name="table-demo"),
    path("panels/demo/", panel_demo, name="panel-demo"),
]
