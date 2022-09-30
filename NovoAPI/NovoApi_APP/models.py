from django.db import models

class supplier_stock(models.Model):
	class Meta:
		db_table = 'supplier_stock'
	# class lead_time:
	# 	managed = False
	# class stock:
	# 	managed = False
	# class code:
	# 	managed = False
	# class price:
	# 	managed = False
	# class updated_on:
	# 	managed = False
	# class part_id:
	# 	managed = False
	# class pkg_type_id:
	# 	managed = False
	# class supplier_id:
	# 	managed = False

#class bom_parts(models.Model):
#	Part = models.CharField(max_length=150)
#	Code = models.CharField(max_length=150)
#	Quantity = models.PositiveIntegerField(max_length=150)
#	StockAvailableQuantity = models.PositiveIntegerField(max_length=150)
#	StockAvailableYesNo = models.CharField(max_length=50)
#	Price = models.PositiveIntegerField	(max_length=50)
