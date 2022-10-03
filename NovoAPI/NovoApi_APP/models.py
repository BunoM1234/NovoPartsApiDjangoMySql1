from django.db import models


		# fields = ('part_id', 'price', 'code', 'stock', 'lead_time')
class supplier_stock(models.Model):
	class Meta:
		db_table = 'supplier_stock'
	lead_time = models.CharField(max_length=150)
	stock = models.PositiveIntegerField()
	code = models.CharField(max_length=150)
	price = models.PositiveIntegerField()
	updated_on = models.DateTimeField(auto_now=True)
	part_id = models.IntegerField()
	pkg_type_id = models.IntegerField()
	supplier_id = models.IntegerField()
#class bom_parts(models.Model):
#	Part = models.CharField(max_length=150)
#	Code = models.CharField(max_length=150)
#	Quantity = models.PositiveIntegerField(max_length=150)
#	StockAvailableQuantity = models.PositiveIntegerField(max_length=150)
#	StockAvailableYesNo = models.CharField(max_length=50)
#	Price = models.PositiveIntegerField	(max_length=50)
