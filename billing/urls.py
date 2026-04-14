from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .api import InvoiceItemViewSet, InvoiceViewSet, ProductViewSet

app_name = "billing"

# Router pour les endpoints API REST
router = DefaultRouter()
router.register(r"api/products", ProductViewSet, basename="api-product")
router.register(r"api/invoices", InvoiceViewSet, basename="api-invoice")
router.register(r"api/invoice-items", InvoiceItemViewSet, basename="api-invoice-item")

# Routes web classiques (templates HTML)
urlpatterns = [
    path("", views.home_redirect, name="home"),
    path("produits/", views.ProductListView.as_view(), name="product_list"),
    path("produits/creer/", views.ProductCreateView.as_view(), name="product_create"),
    path("produits/<int:pk>/modifier/", views.ProductUpdateView.as_view(), name="product_update"),
    path("produits/<int:pk>/supprimer/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("factures/", views.InvoiceListView.as_view(), name="invoice_list"),
    path("factures/creer/", views.InvoiceCreateView.as_view(), name="invoice_create"),
    path("factures/<int:pk>/", views.InvoiceDetailView.as_view(), name="invoice_detail"),
]

# Ajoute les routes API
urlpatterns += router.urls
