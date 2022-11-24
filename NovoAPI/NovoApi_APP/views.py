#from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import boms, manufacturers, supplier_stock, boards, suppliers, Userstest, parts, part_purchase
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
        bomsp = list(boms.objects.values_list('uuid', 'id', 'board_id'))
        if len(bomsp) > 0:
            datos = {"boms": bomsp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)

class PartsView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        partsp = list(parts.objects.values_list('name'))
        if len(partsp) > 0:
            datos = {"parts": partsp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)

class StockView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        stockp = list(supplier_stock.objects.values_list('stock', 'price', 'code'))
        if len(stockp) > 0:
            datos = {"stock": stockp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)

class PartPurchaseView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        partpurchasep = list(part_purchase.objects.values_list('supplier_code'))
        if len(partpurchasep) > 0:
            datos = {"part_purchase": partpurchasep}
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

class UsersView(View):
    
    @method_decorator(csrf_exempt) 
    def  dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        Userstestp = list(Userstest.objects.values_list('username', 'password'))
        if len(Userstestp) > 0:
            datos = {"Userstest": Userstestp}
        else:
            datos = {'message': "Info not found"}
        return JsonResponse(datos)
