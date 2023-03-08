from django.urls import path
from .views import EstudianteView
from .views import EmpresaView
urlpatterns=[
path('estudiantes/', EstudianteView.as_view(), name="estudiantes_list"),
path('estudiantes/<int:id>', EstudianteView.as_view(), name="estudiantes_process"),
path('empresas/', EmpresaView.as_view(), name="empresas_list"),
path('empresas/<int:id>', EmpresaView.as_view(), name="empresas_process"),
]