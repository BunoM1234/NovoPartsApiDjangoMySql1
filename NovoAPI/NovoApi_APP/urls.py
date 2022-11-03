from django.urls import  path
from .views import BomsView, ManufacturersView, BoardsView, StockView

urlpatterns=[
    path('manufacturers/', ManufacturersView.as_view(), name='manufacturers_list'),
    path('boms/<id>', BomsView.as_view(), name='boms_list'),
    path('boards/<id>', BoardsView.as_view(), name='boards_list'),
    path('stock/', StockView.as_view(), name='stock_list'),
]