# Generated by Django 3.1.2 on 2022-04-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0003_functionality_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='veterinaries',
        ),
        migrations.AddField(
            model_name='rol',
            name='user',
            field=models.ManyToManyField(blank=True, to='doggieHommie.User'),
        ),
    ]