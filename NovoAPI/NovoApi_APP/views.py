#from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import novo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class NovoView(View):
    
    @method_decorator(csrf_exempt) #nos exonera de esta restriccion, para que no salte esta restriccion
    def  dispatch(self, request, *args, **kwargs): #despachar o enviar y se ejecuta cada vez que hacemos una peticion
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        novop = list(novo.objects.values())
        if len(novop) > 0:
            datos = {'message': "Success!" + novo.objects.values}
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