#from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import supplier_stock
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

class NovoView(View):
    
    @method_decorator(csrf_exempt) #nos exonera de esta restriccion, para que no salte esta restriccion
    def  dispatch(self, request, *args, **kwargs): #despachar o enviar y se ejecuta cada vez que hacemos una peticion
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        #'BC817RAZ'
        novop = list(supplier_stock.objects.values_list('id', 'stock'))
        #novop = serializers.serialize('json', supplier_stock.objects.raw('SELECT id, code FROM alexandria.supplier_stock LIMIT 0, 1000'))
        if len(novop) > 0:
            datos = {"novop": novop}
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