from django.urls import  path
from .views import BomsView, ManufacturersView, StockView

urlpatterns=[
    path('manufacturers/', ManufacturersView.as_view(), name='Manufacturers_list'),
    path('boms/', BomsView.as_view(), name='boms_list'),
    path('stock/', StockView.as_view(), name='stock_list'),

]