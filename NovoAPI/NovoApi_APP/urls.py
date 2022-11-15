from django.urls import  path
from .views import BomsView, ManufacturersView, BoardsView, StockView, UsersView
from django.urls import include


urlpatterns=[
    path('manufacturers/', ManufacturersView.as_view(), name='manufacturers_list'),
    path('boms/', BomsView.as_view(), name='boms_list'),
    path('boards/', BoardsView.as_view(), name='boards_list'),
    path('stock/', StockView.as_view(), name='stock_list'),
    path('users/', UsersView.as_view(), name='users_list'),
    # path('accounts/', include('django.contrib.auth.urls')),

]