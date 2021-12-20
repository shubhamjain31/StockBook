from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("add-supplier/", views.supplier, name="supplier"),
    path("edit-supplier/<int:id>", views.supplier, name="supplier"),
    path("delete-supplier/<int:id>", views.delete_supplier, name="delete_supplier"),
    path("supplier-list/", views.all_suppliers, name="all_suppliers"),
]