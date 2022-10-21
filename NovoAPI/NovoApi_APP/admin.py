from django.contrib import admin
from .models import supplier_stock
from .models import suppliers
from .models import supplier_pkg_type
from .models import parts
from .models import manufacturer
from .models import part_purchase

admin.site.register(supplier_stock)
admin.site.register(suppliers)
admin.site.register(supplier_pkg_type)
admin.site.register(parts)
admin.site.register(manufacturer)
admin.site.register(part_purchase)
