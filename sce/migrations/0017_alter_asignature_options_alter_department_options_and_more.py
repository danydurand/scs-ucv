# Generated by Django 4.0.4 on 2022-07-21 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sce', '0016_asignature_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignature',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_pensums', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_pensums', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
