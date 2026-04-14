"""
Serializers pour l'API REST Django.
Convertit les modèles Django en JSON et vice-versa.
"""

from rest_framework import serializers

from .models import Invoice, InvoiceItem, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Product.
    Permet de sérialiser les informations des produits.
    """

    class Meta:
        model = Product
        fields = ["id", "name", "price", "expiration_date"]


class InvoiceItemSerializer(serializers.ModelSerializer):
    """
    Serializer pour les articles de facture (InvoiceItem).
    Inclut les informations du produit associé.
    """

    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    line_total = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItem
        fields = ["id", "product", "product_id", "quantity", "line_total"]

    def get_line_total(self, obj):
        """Calcule le total de la ligne (quantité × prix unitaire)"""
        return float(obj.quantity * obj.product.price)


class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Invoice.
    Inclut les articles de facture et les totaux calculés.
    """

    items = InvoiceItemSerializer(many=True, read_only=True)
    total_products = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ["id", "created_at", "items", "total_products", "total_amount"]

    def get_total_products(self, obj):
        """Retourne le nombre total de produits dans la facture"""
        return obj.total_products

    def get_total_amount(self, obj):
        """Retourne le montant total de la facture"""
        return float(obj.total_amount)
