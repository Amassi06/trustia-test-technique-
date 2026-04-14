"""
Viewsets API REST pour les endpoints CRUD.
Fournit des endpoints complets pour products et invoices.
"""

from rest_framework import viewsets

from .models import Invoice, InvoiceItem, Product
from .serializers import InvoiceItemSerializer, InvoiceSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API ViewSet pour les Produits.
    Fournit les actions CRUD complètes :
    - GET /api/products/ → liste tous les produits
    - POST /api/products/ → crée un produit
    - GET /api/products/{id}/ → récupère un produit
    - PUT /api/products/{id}/ → modifie un produit
    - PATCH /api/products/{id}/ → modifie partiellement un produit
    - DELETE /api/products/{id}/ → supprime un produit
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """
    API ViewSet pour les Articles de Facture.
    Gère les items individuels au sein des factures.
    """

    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API ViewSet pour les Factures.
    Fournit les actions CRUD complètes :
    - GET /api/invoices/ → liste toutes les factures
    - POST /api/invoices/ → crée une facture
    - GET /api/invoices/{id}/ → récupère une facture avec ses articles
    - PUT /api/invoices/{id}/ → modifie une facture
    - PATCH /api/invoices/{id}/ → modifie partiellement une facture
    - DELETE /api/invoices/{id}/ → supprime une facture
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
