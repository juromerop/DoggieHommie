# Generated by Django 4.0.3 on 2022-05-20 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0016_remove_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
    ]
