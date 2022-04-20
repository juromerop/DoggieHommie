# Generated by Django 3.1.2 on 2022-04-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cédula de extrajería')], max_length=30)),
                ('numero_documento', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=40)),
                ('departamento', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('contrasenia', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
    ]
