# Generated by Django 4.0.4 on 2022-05-30 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sce', '0014_asignature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignature',
            old_name='is_exempt_interships',
            new_name='is_exempted_interships',
        ),
    ]