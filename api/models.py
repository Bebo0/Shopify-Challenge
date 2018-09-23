from django.db import models

class LineItem(models.Model):
	# product = models.ForeignKey(Product)
	value = models.FloatField()

	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]

class Product(models.Model):
	line_items = models.ManyToManyField(LineItem)
	value = models.FloatField()

	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]

class Order(models.Model):
	line_items = models.ManyToManyField(LineItem)
	value = models.FloatField()

	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]


class Shop(models.Model):
	products = models.ManyToManyField(Product)
	orders = models.ManyToManyField(Order)


	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]





