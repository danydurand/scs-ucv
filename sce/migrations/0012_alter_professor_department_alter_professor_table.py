# Generated by Django 4.0.4 on 2022-05-27 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sce', '0011_alter_professor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professors', to='sce.department'),
        ),
        migrations.AlterModelTable(
            name='professor',
            table=None,
        ),
    ]
