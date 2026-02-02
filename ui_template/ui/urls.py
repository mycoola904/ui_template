from django.urls import path
from . import views

app_name = "ui"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tables/", views.tables, name="tables"),
    path("forms/", views.forms, name="forms"),
    path("tables/demo/", views.table_demo, name="table-demo"),
    path("panels/demo/", views.panel_demo, name="panel-demo"),
    path("accounts/demo/", views.account_detail_demo, name="account-detail-demo"),
]
