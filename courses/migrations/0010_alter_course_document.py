# Generated by Django 4.1.6 on 2023-02-09 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_course_course_alter_course_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='document',
            field=models.CharField(choices=[('cedula de identidad', 'Cédula de identidad'), ('pasaporte', 'Pasaporte'), ('dni', 'DNI')], max_length=20, verbose_name='Tipo de documento'),
        ),
    ]
