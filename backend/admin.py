from django.contrib import admin
from .models import Estudiante
from .models import ProgramaEducativo
from .models import Personal

from .models import Empresa
from .models import Proyecto
from .models import Proceso

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(ProgramaEducativo)
admin.site.register(Personal)
admin.site.register(Proceso)
admin.site.register(Empresa)
admin.site.register(Proyecto)
