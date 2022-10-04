from django.db import models


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

class boards(models.Model):
	class Meta:
		db_table = 'boards' # nombre de la tabla. En este caso boards
	code = models.CharField(max_length=256) # nombre de la columna y tipo. En este caso la columna es code y el tipo es char de limit 256
	description = models.CharField(max_length=256)# nombre de la columna y tipo. En este caso la columna es code y el tipo es char de limit 256
	revision = models.IntegerField() # columna revision con tipo int. 

class parts(models.Model):
	class Meta:
		db_table = 'parts'
	name = models.CharField(max_length=150)


class part_purchase(models.Model):
	class Meta:
		db_table = 'part_purchase'

class bom_parts(models.Model):
	class Meta:
		db_table = 'bom_parts'

class suppliers(models.Model):
	class Meta:
		db_table = 'suppliers'

class manufacturer(models.Model):
	class Meta:
		db_table = 'manufacturer'

class boms(models.Model):
	class Meta:
		db_table = 'boms'

class boms(models.Model):
	class Meta:
		db_table = 'boms'