# Generated by Django 4.1.1 on 2022-09-21 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miportafolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descripcion',
            new_name='description',
        ),
    ]
