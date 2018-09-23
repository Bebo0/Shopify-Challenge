import graphene
from graphene_django.types import DjangoObjectType
from .models import LineItem, Shop, Order, Product

class LineItemType(DjangoObjectType):
	class Meta:
		model = LineItem

class ShopType(DjangoObjectType):
	class Meta:
		model = Shop

class OrderType(DjangoObjectType):
	class Meta:
		model = Order

class ProductType(DjangoObjectType):
	class Meta:
		model = Product


class Query(graphene.ObjectType):
	all_lineitems = graphene.List(LineItemType)
	all_shops = graphene.List(ShopType)
	all_orders = graphene.List(OrderType)
	all_products = graphene.List(ProductType)

	def resolve_all_lineitems(self, info, **kwargs):
		return LineItem.objects.all()

	def resolve_all_shops(self, info, **kwargs):
		return Shop.objects.all()

	def resolve_all_orders(self, info, **kwargs):
		return Order.objects.all()

	def resolve_all_products(self, info, **kwargs):
		return Product.objects.all()