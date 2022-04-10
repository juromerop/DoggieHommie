from django.db import models

#Se crea entidad usuario
class Usuario(models.Model):
    TIPO_DOCUMENTOS = (
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extrajería'),
    )
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    correo_electronico = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    tipo_documento = models.CharField(max_length=30, choices= TIPO_DOCUMENTOS)
    numero_documento = models.CharField(max_length=10)
    pais = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)


