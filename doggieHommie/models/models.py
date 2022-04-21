from cgitb import text
from datetime import date
from distutils import extension
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User

#Se crea entidad usuario
class User(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="nurse",null=True)
    TIPO_DOCUMENTOS = (
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extrajería'),
    )
    second_name = models.CharField(max_length=30)
    second_lastname = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    tipo_documento = models.CharField(max_length=30, choices= TIPO_DOCUMENTOS)
    numero_documento = models.CharField(max_length=10)
    pais = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.numero_documento)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"
        

#class Admin(models.Model):

class Veterinary(models.Model):
    fecha_graduacion = models.DateField()
    universidad = models.CharField(max_length= 60)
    fecha_registro = models.DateField()
    calificacion = models.FloatField()
    numero_tarjeta_profesional = models.IntegerField()
    
    def __str__(self):
        return str(self.numero_tarjeta_profesional)
    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = "Veterinarios"

class Speciality(models.Model):
    nombre = models.CharField(max_length= 60)
    descripcion =  models.CharField(max_length= 90)
    veterinaries = models.ManyToManyField(Veterinary,blank=True)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = "Especialidades"

class Veterinary_files(models.Model):
    nombre = models.CharField(max_length= 60)
    extension = models.CharField(max_length= 60)
    archivo = models.CharField(max_length= 1000)
    veterinary = models.ForeignKey(Veterinary, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'archivo_vet'
        verbose_name_plural = "archivos_vet"

class Rol(models.Model):
    nombre = models.CharField(max_length= 60)
    descripcion = models.CharField(max_length=100)
    user = models.ManyToManyField(User,blank=True)
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = "roles"

class Functionality(models.Model):
    nombre = models.CharField(max_length = 60)
    url = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 100)
    rol = models.ManyToManyField(Rol,blank=True)
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'funcionalidad'
        verbose_name_plural = "funcionalidades"

class Post(models.Model):
    title = models.CharField(max_length = 120)
    text = models.TextField()
    date = models.DateField()
    grade = models.IntegerField()

    def __str__(self):
        #return str(self.)
        pass
    
    class Meta: 
        pass

class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    

    def __str__(self):
        #return str(self.)
        pass
    

class Image(models.Model):
    #id
    name = models.CharField(max_length=60)
    extension = models.CharField(max_length=10)
    file = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        #return str(self.)
        pass
    
    













