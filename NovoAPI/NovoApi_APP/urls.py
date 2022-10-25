from django.urls import  path
from .views import bomsID, manufacturersID, boardsID, stockID

urlpatterns=[
    path('manufacturers/<id>', manufacturersID),
    path('boms/<id>', bomsID),
    path('boards/<id>', boardsID),
    path('stock/<id>', stockID),
]