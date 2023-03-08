from django.db import models


#Tabla Estudiante, para el registro de sus datos relevantes
class Estudiante(models.Model):
        id_estudiante = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=20, blank=False)
        apellido_pat = models.CharField(max_length=20, blank=False)
        apellido_mat = models.CharField(max_length=20, blank=False)
        sexo = models.CharField(max_length=20, blank=False)
        matricula = models.CharField(max_length=20, unique=False, blank=False)
        correo_pers = models.EmailField(blank=False)
        correo_inst = models.EmailField(unique=True, blank=False)
        telefono = models.CharField(max_length=20, blank=False)
        estado = models.BooleanField(default=True, blank=False) #Sigue estudiando o se dio de baja
        nombre_programa = models. CharField(max_length=50, blank=False)
        usuario = models.CharField(max_length=40, blank=False)
        contraseña = models.CharField(max_length=20, blank=False)

        def str(self):
           return self.nombre 

#Tabla Usuario para Login
class Personal(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True, blank=False)
    contraseña = models.CharField(max_length=20, blank=False)
    

    def str(self):
       return self.nombre

#tabala Proyecto, datos que la empresa proporciona
class Proyecto(models.Model):
 id_proyecto = models.AutoField(primary_key=True)
 periodo = models.CharField(max_length=50, blank=False)
 año = models.PositiveSmallIntegerField(blank=False)
 vacantes = models.IntegerField(blank=False)
 modalidad = models.CharField(max_length=50, blank=False)
 nombre = models.CharField(max_length=20, blank=False)
 objetivo = models.TextField(blank=False)
 justificación = models.TextField(blank=False)
 asesor = models.CharField(max_length=20, blank=False)
 estado = models.BooleanField(default=True, blank=False) #Activo o no activo el proyecto
 nombre = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True)
 nombre = models.ForeignKey('ProgramaEducativo', on_delete=models.CASCADE, blank=True)
 nombre = models.ForeignKey('Proceso', on_delete=models.CASCADE, blank=True)

 def str(self):
    return self.nombre 

#Tabla Empresa, para el registro de sus datos importantes
class Empresa(models.Model):
            id_empresa = models.AutoField(primary_key=True)
            nombre = models.CharField(max_length=20, unique=True, blank=False)
            rfc = models.CharField(max_length=13, unique=False, blank=False)
            titular = models.CharField(max_length=20, blank=False)
            cargo = models.CharField(max_length=50, blank=False)
            correo = models.EmailField(blank=False)
            nombre_enlace = models.CharField(max_length=20, unique=True, blank=False)
            telefono = models.CharField(max_length=15, unique=True, blank=False)
            telefono_enlace = models.CharField(max_length=15, unique=True, blank=False)
            correo_enlace = models.EmailField(unique=True, blank=False)
            entidad = models.CharField(max_length=20, blank=False) #Estados de Mexico
            ciudad = models.CharField(max_length=20, blank=False)
            colonia = models.CharField(max_length=20)
            codigo_postal = models.IntegerField(max_length=10, blank=False)
            calle = models.CharField(max_length=30, blank=False)
            numero = models.CharField(max_length=50, blank=False) 
            estado = models.BooleanField(default=True, blank=False) #Empresa activa o no activa
            usuario = models.CharField(max_length=40, blank=False)
            contraseña = models.CharField(max_length=20, blank=False)

            def str(self):
               return self.nombre


#Tabla Proceso, Estancia o Estadia
class Proceso(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False)

    def str(self):
       return self.nombre

#Tabla ProyectoEstudiante, creada por el tipo de relacion entre 2 tablas
class ProyectoEstudiante(models.Model): 
    id_proyectoEst = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, blank=True)

    def str(self):
        return self.id_estudiante


#Tabla ProgramaEducativo, donde estaran las carreras con las que cuenta la universidad
class ProgramaEducativo(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank= False)

    def str(self):
       return self.nombre