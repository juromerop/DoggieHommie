# Generated by Django 4.0.3 on 2022-05-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0011_alter_functionality_options_remove_bankaccounts_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccounts',
            name='bank_type',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
