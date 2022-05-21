# Generated by Django 4.0.4 on 2022-05-21 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sce', '0005_faculty_created_by_faculty_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Activa ?'),
        ),
        migrations.AddField(
            model_name='school',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_schools', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activa ?'),
        ),
        migrations.AddField(
            model_name='school',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_schools', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='F. Creacion'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='F. Modificacion'),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='F. Creacion'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='school',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='F. Actualizacion'),
        ),
    ]
