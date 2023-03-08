from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Estudiante
from .models import Empresa
import json
# Create your views here.

class EstudianteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            estudiantes=list(Estudiante.objects.filter(id=id).values())
            if len(estudiantes)>0:
                estudiante=estudiantes[0]
                datos = {'message': "Success", 'estudiante': estudiante}
                return JsonResponse(datos)
            else:
               datos = {'message': "Estudiante not found..."} 
               return JsonResponse(datos)
        else:
            estudiantes = list(Estudiante.objects.values())
            if len(estudiantes) > 0:
                datos = {'message': "Success", 'estudiantes': estudiantes}
                return JsonResponse(datos)
            else:
                datos = {'message': "Estudiantes not found..."}
                return JsonResponse(datos)
            
    def post(self, request):
       # print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Estudiante.objects.create(nombre=jd['nombre'],apellido_pat=jd['apellido_pat'],apellido_mat=jd['apellido_mat']
                    ,sexo=jd['sexo'],matricula=jd['matricula'],correo_pers=jd['correo_pers']
                    ,correo_inst=jd['correo_inst'],telefono=jd['telefono'],estado=jd['estado']
                    ,nombre_programa=jd['nombre_programa'],usuario=jd['matricula'],contraseña=jd['matricula'])
       datos = {'message':"Succes"}
       return JsonResponse(datos)
        #metodo para enviar los datos y que se guarden 
    def put(self, request,id):
        jd=json.loads(request.body)
        estudiantes=list(Estudiante.objects.filter(id=id).values())
        if len(estudiantes)>0:
            estudiantes=Estudiante.objects.get(id=id)
            estudiantes.nombre=jd['nombre']
            estudiantes.apellido_pat=jd['apellido_pat']
            estudiantes.apellido_mat=jd['apellido_mat']
            estudiantes.sexo=jd['sexo']
            estudiantes.matricula=jd['matricula']
            estudiantes.correo_pers=jd['correo_pers']
            estudiantes.correo_inst=jd['correo_inst']
            estudiantes.telefono=jd['telefono']
            estudiantes.estado=jd['estado']
            estudiantes.nombre_programa=jd['nombre_programa']
            estudiantes.usuario=jd['matricula']
            estudiantes.contraseña=jd['matricula']
            estudiantes.save()
            datos={'message':"Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Estudiantes not found..."}
        return JsonResponse(datos)
    def delete(self, request,id):
        estudiantes=list(Estudiante.objects.filter(id=id).values())
        if len(estudiantes)>0:
            Estudiante.objects.filter(id=id).delete()
            datos={'message':"Success"}
            return JsonResponse(datos)
        else:
            datos={'message':"Estudiante not found..."}
        return JsonResponse(datos)

class EmpresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            empresas=list(Empresa.objects.filter(id=id).values())
            if len(empresas)>0:
                empresa=empresas[0]
                datos = {'message': "Success", 'empresa': empresa}
                return JsonResponse(datos)
            else:
               datos = {'message': "Empresa not found..."} 
               return JsonResponse(datos)
        else:
            empresas = list(Empresa.objects.values())
            if len(empresas) > 0:
                datos = {'message': "Success", 'empresas': empresas}
                return JsonResponse(datos)
            else:
                datos = {'message': "Empresas not found..."}
                return JsonResponse(datos)
            
    def post(self, request):
       # print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Empresa.objects.create(nombre=jd['nombre'],rfc=jd['rfc'],titular=jd['titular']
                    ,cargo=jd['cargo'],correo=jd['correo'],nombre_enlace=jd['nombre_enlace'],telefono=jd['telefono']
                    ,telefono_enlace=jd['telefono_enlace'],correo_enlace=jd['correo_enlace'],estado=jd['estado']
                    ,entidad=jd['entidad'],ciudad=jd['ciudad'],colonia=jd['colonia'],codigo_postal=jd['codigo_postal']
                    ,calle=jd['calle'],numero=jd['numero'],usuario=jd['rfc'], contraseña=jd['rfc'])
       datos = {'message':"Succes"}
       return JsonResponse(datos)
        #metodo para enviar los datos y que se guarden 
    def put(self, request,id):
        jd=json.loads(request.body)
        empresas=list(Empresa.objects.filter(id=id).values())
        if len(empresas)>0:
            empresas=Empresa.objects.get(id=id)
            empresas.nombre=jd['nombre']
            empresas.rfc=jd['rfc']
            empresas.titular=jd['titular']
            empresas.cargo=jd['cargo']
            empresas.correo=jd['correo']
            empresas.telefono['telefono']
            empresas.nombre_enlace=jd['nombre_enlace']
            empresas.telefono_enlace=jd['telefono_enlace']
            empresas.correo_enlace=jd['correo_enlace']
            empresas.estado=jd['estado']
            empresas.entidad=jd['entidad']
            empresas.ciudad=jd['ciudad']
            empresas.colonia=jd['colonia']
            empresas.codigo_postal=jd['codigo_postla']
            empresas.calle=jd['calle']
            empresas.numero=jd['numero']
            empresas.usuario=jd['rfc']
            empresas.contraseña=jd['rfc']
            empresas.save()
            datos={'message':"Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Empresas not found..."}
        return JsonResponse(datos)
    def delete(self, request,id):
        empresas=list(Empresa.objects.filter(id=id).values())
        if len(empresas)>0:
            Empresa.objects.filter(id=id).delete()
            datos={'message':"Success"}
            return JsonResponse(datos)
        else:
            datos={'message':"Empresa not found..."}
        return JsonResponse(datos)