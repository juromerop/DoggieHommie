# Generated by Django 4.0.3 on 2022-06-17 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0027_postsliked_alter_functionality_options_post_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doggieHommie.post'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doggieHommie.user'),
        ),
    ]
