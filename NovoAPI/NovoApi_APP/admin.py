from django.contrib import admin
from .models import supplier_stock
from .models import suppliers
from .models import supplier_pkg_type
from .models import parts
from .models import manufacturers
from .models import part_purchase
# from .models import Userstest




admin.site.register(supplier_stock)
admin.site.register(suppliers)
admin.site.register(supplier_pkg_type)
admin.site.register(parts)
admin.site.register(manufacturers)
admin.site.register(part_purchase)
# admin.site.register(Userstest)



