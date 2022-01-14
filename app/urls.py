from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("add-supplier/", views.supplier, name="supplier"),
    path("edit-supplier/<int:id>", views.supplier, name="supplier"),
    path("delete-supplier/<int:id>", views.delete_supplier, name="delete_supplier"),
    path("supplier-list/", views.all_suppliers, name="all_suppliers"),

    path("add-buyer/", views.buyer, name="buyer"),
    path("edit-buyer/<int:id>", views.buyer, name="buyer"),
    path("buyer-list/", views.all_buyers, name="all_buyers"),
    path("delete-buyer/<int:id>", views.delete_buyer, name="delete_buyer"),


    path("add-season/", views.season, name="season"),
    path("season-list/", views.all_seasons, name="all_seasons"),
    path("edit-season/<int:id>", views.season, name="season"),
    path("delete-season/<int:id>", views.delete_season, name="delete_season"),
]