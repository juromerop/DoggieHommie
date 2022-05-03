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
        User, on_delete=models.CASCADE, related_name = "nurse",null=True)
    telefono = models.CharField(max_length = 10)
    numero_documento = models.CharField(max_length = 10)
    pais = models.CharField(max_length = 40)
    ciudad = models.CharField(max_length = 40)
    estado = models.CharField(max_length = 40)
    
    def __str__(self):
        return str(self.numero_documento)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"
        

#class Admin(models.Model):

class Veterinary(models.Model):
    fecha_graduacion = models.DateField()
    universidad = models.CharField(max_length = 60)
    fecha_registro = models.DateField()
    calificacion = models.FloatField()
    numero_tarjeta_profesional = models.IntegerField()
    associated_user = models.ForeignKey(User, on_delete = models.CASCADE,null = True)
    
    def __str__(self):
        return str(self.numero_tarjeta_profesional)
    
    class Meta:
        verbose_name = 'Veterinario' 
        verbose_name_plural = "Veterinarios"

class Speciality(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion =  models.CharField(max_length = 90)
    veterinaries = models.ManyToManyField(Veterinary,blank = True)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = "Especialidades"

class Veterinary_files(models.Model):
    nombre = models.CharField(max_length = 60)
    extension = models.CharField(max_length = 60)
    archivo = models.CharField(max_length = 1000)
    veterinary = models.ForeignKey(Veterinary, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'archivo_vet'
        verbose_name_plural = "archivos_vet"

class Rol(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion = models.CharField(max_length = 100)
    user = models.ManyToManyField(User,blank = True)
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = "roles"

class Functionality(models.Model):
    nombre = models.CharField(max_length = 60)
    url = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 100)
    rol = models.ManyToManyField(Rol,blank = True)
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'funcionalidad'
        verbose_name_plural = "funcionalidades"
        

# class Solicitud(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     banksAccountList = models.
#     telephoneList
#      título, descripción, lista de cuentas bancarias, números celulares, fotos adjuntas, documentos adjuntos.


class Post(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    date = models.DateField()
    grade = models.IntegerField()
    isDonation = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #banck_accounts_list : pienso que puede ser una lista de 2-tuplas, donde cada 2-tupla sea (nombre banco, # cuenta)

    

    def __str__(self):
        #return str(self.title)
        pass
    
    class Meta: 
        pass


class BankAccounts(models.Model):
    bank_name = models.CharField(max_length = 120)
    account_number = models.CharField(max_length = 60)
    #post =  models.ManyToManyField(Post,blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)
    



class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    

    def __str__(self):
        #return str(self.user + ": " + self.text )
        pass
    

class Image(models.Model):
    
    name = models.CharField(max_length = 60)
    extension = models.CharField(max_length = 10)
    file = models.ImageField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        #return str(self.name)
        pass
    
    













