#from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import boms, manufacturers, supplier_stock, boards
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

class ManufacturersView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        manufacturersp = list(manufacturers.objects.values_list('id', 'name'))
        if len(manufacturersp) > 0:
            datos = {"manufacturers": manufacturersp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)


    def post(self, request):
        datos = {'message':'Success'}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass

class BomsView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        bomsp = list(boms.objects.values_list('uuid'))
        if len(bomsp) > 0:
            datos = {"boms": bomsp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)

class StockView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        stockp = list(supplier_stock.objects.values_list('stock', 'code', 'price'))
        if len(stockp) > 0:
            datos = {"stock": stockp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)

class BoardsView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        boardsp = list(boards.objects.values_list('code', 'description'))
        if len(boardsp) > 0:
            datos = {"boards": boardsp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)