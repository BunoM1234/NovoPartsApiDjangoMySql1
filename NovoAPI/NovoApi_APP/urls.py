from django.urls import  path
from .views import NovoView

urlpatterns=[
    path('novo/', NovoView.as_view(), name='Novo_list'),
    path('boms/', NovoView.as_view(), name='boms')
]