# Generated by Django 4.0.3 on 2022-05-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0020_alter_bankaccounts_bank_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagess',
            field=models.TextField(null=True),
        ),
    ]
