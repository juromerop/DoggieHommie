from django.db import models

#Se crea entidad usuario
class User(models.Model):
    TIPO_DOCUMENTOS = (
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extrajería'),
    )
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    correo_electronico = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    tipo_documento = models.CharField(max_length=30, choices= TIPO_DOCUMENTOS)
    numero_documento = models.CharField(max_length=10)
    pais = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)

#class Admin(models.Model):

class Veterinary(models.Model):
    fecha_graduacion = models.DateField()
    universidad = models.CharField(max_length= 60)
    fecha_registro = models.DateField()
    calificacion = models.FloatField()
    numero_tarjeta_profesional = models.IntegerField()

class Speciality(models.Model):
    nombre = models.CharField(max_length= 60)
    descripcion =  models.CharField(max_length= 90)
    veterinaries = models.ManyToManyField(Veterinary,blank=True)

class Veterinary_files(models.Model):
    nombre = models.CharField(max_length= 60)
    extension = models.CharField(max_length= 60)
    archivo = models.CharField(max_length= 1000)
    veterinary = models.ForeignKey(Veterinary, on_delete=models.CASCADE)

class Rol(models.Model):
    nombre = models.CharField(max_length= 60)
    descripcion = models.CharField(max_length=100)
    user = models.ManyToManyField(User,blank=True)

class Functionality(models.Model):
    nombre = models.CharField(max_length = 60)
    url = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 100)
    rol = models.ManyToManyField(Rol,blank=True)







