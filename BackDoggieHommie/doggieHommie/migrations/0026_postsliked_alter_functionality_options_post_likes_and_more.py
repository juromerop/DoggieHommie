# Generated by Django 4.0.3 on 2022-06-16 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0025_postsliked_alter_functionality_options_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='state_user',
            field=models.CharField(max_length=20, null=True),
        )
    ]
