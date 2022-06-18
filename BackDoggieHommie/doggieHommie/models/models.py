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
    number_banned = models.IntegerField( null = True)

    
    def __str__(self):
        return str(self.numero_documento)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"

class BankAccounts(models.Model):
    BANK_NAMES = (("Nequi","Nequi"), ("Paypal","Paypal"), ("Daviplata" ,"Daviplata")) 
    bank_name = models.CharField(max_length = 120, choices = BANK_NAMES)
    account_number = models.CharField(max_length = 60)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bank_type = models.CharField(max_length = 40, null=True)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    date = models.DateField()
    grade = models.IntegerField()
    isDonation = models.BooleanField()
    state = models.CharField(max_length = 20, null = True)
    number_banned = models.IntegerField( null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bankAccounts = models.ManyToManyField(BankAccounts,blank = True)
    images = models.TextField(blank = True, null = True)
    likes =  models.ManyToManyField(User, blank = True ,through="PostsLiked",related_name="likes")
    state_user = models.CharField(max_length = 20, null = True)
    def __str__(self):
        #return str(self.title)
        pass

    class Meta: 
        pass

        
class PostsLiked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return "ok"
        #return str(str(self.user) + "," + str(self.post))
        
    class Meta: 
        pass

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
        

# class likedPosts(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date = models.DateField()

class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments', null = True)
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = "Comentarios"
    

class Image(models.Model):
    
    name = models.CharField(max_length = 60)
    extension = models.CharField(max_length = 10)
    file = models.ImageField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        #return str(self.name)
        pass
    

class Image_field(models.Model):
    image = models.ImageField(upload_to = 'images/')

class Post_Image(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image = models.ForeignKey(Image_field, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.post)
    
class Notification(models.Model):
    text = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE,null=True, blank=True)
    def __str__(self):
        return str(self.text)