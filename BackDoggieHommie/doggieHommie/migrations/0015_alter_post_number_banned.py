# Generated by Django 4.0.3 on 2022-05-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0014_post_number_banned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_banned',
            field=models.IntegerField(null=True),
        ),
    ]