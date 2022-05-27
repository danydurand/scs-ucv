# Generated by Django 4.0.4 on 2022-05-27 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sce', '0008_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professors', to='sce.department'),
        ),
    ]
