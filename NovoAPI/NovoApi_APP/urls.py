from django.urls import  path
from .views import BomsView, ManufacturersView, StockView, BoardsView

urlpatterns=[
    path('manufacturers/', ManufacturersView.as_view(), name='manufacturers_list'),
    path('boms/', BomsView.as_view(), name='boms_list'),
    path('stock/', StockView.as_view(), name='stock_list'),
    path('boards/', BoardsView.as_view(), name='boards_list'),


]