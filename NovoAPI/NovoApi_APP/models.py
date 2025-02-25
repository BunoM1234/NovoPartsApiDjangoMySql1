from django.db import models
from django.contrib.auth.models import User


class Userstest(models.Model):
	class Meta:
		db_table = 'userstest'
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField()
	is_superuser = models.IntegerField()
	username = models.CharField(max_length=150)
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	email = models.CharField(max_length=254)
	is_staff = models.IntegerField()
	is_active = models.IntegerField()
	date_joined = models.DateTimeField()

class suppliers(models.Model):
	class Meta:
		db_table = 'suppliers'
	name = models.CharField(max_length=100)

class supplier_stock(models.Model):
	class Meta:
		db_table = 'supplier_stock'
	lead_time = models.IntegerField()
	stock = models.PositiveIntegerField()
	code = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=5, decimal_places=3)
	updated_on = models.DateTimeField()
	part = models.ForeignKey('parts', on_delete=models.CASCADE, null = True)
	pkg_type_id = models.IntegerField(blank=True, null=True, default=1)
	supplier_id = models.IntegerField(blank=True, null=True, default=2)

class supplier_pkg_type(models.Model):
	class Meta:
		db_table = 'supplier_pkg_type'
	type = models.CharField(max_length=50)

class parts(models.Model):
	class Meta:
		db_table = 'parts'
	name = models.CharField(max_length=30)
	uuid = models.CharField(max_length=40)
	family = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	ns_code = models.CharField(max_length=14)
	ns_type = models.CharField(max_length=10)
	ns_rating = models.CharField(max_length=50)
	ns_status = models.CharField(max_length=100)
	ns_docs = models.CharField(max_length=20)
	lifecycle = models.CharField(max_length=20)

class part_purchase(models.Model):
	class Meta:
		db_table = 'part_purchase'
	supplier_code = models.CharField(max_length=50)
	manufacturers_code = models.CharField(max_length=50)
	manufacturer_id = models.ForeignKey('manufacturers', on_delete=models.CASCADE, null = True)
	supplier_id = models.ForeignKey('suppliers', on_delete=models.CASCADE, null = True)

class manufacturers(models.Model):
	class Meta:
		db_table = 'manufacturers'
	name = models.CharField(max_length=150)

class boms(models.Model):
	class Meta:
		db_table = 'boms'
	tag = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	board = models.ForeignKey('boards', on_delete=models.CASCADE, null = True)
	type_id = models.PositiveIntegerField()
	uuid = models.CharField(max_length=32)
	variant = models.CharField(max_length=100)
	updated_on = models.DateTimeField()

class bom_types(models.Model):
	class Meta:
		db_table = 'bom_types'
	type = models.CharField(max_length=40)

class bom_parts(models.Model):

	class Meta:
		db_table = 'bom_parts'
	quantity = models.PositiveIntegerField()
	designators = models.CharField(max_length=2000)
	bom = models.ForeignKey('boms', on_delete=models.CASCADE, null = True)
	part_id = models.ForeignKey('parts', on_delete=models.CASCADE, null = True)


class boards(models.Model):
	class Meta:
		db_table = 'boards' # nombre de la tabla. En este caso boards
	code = models.CharField(max_length=256) # nombre de la columna y tipo. En este caso la columna es code y el tipo es char de limit 256
	description = models.CharField(max_length=256)# nombre de la columna y tipo. En este caso la columna es code y el tipo es char de limit 256
	revision = models.IntegerField() # columna revision con tipo int. 


