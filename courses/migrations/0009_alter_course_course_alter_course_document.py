# Generated by Django 4.1.6 on 2023-02-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_course_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(choices=[('Curso Pasteleria', 'Curso Pasteleria'), ('Curso Chef', 'Curso Chef')], max_length=20, verbose_name='Curso a elegir'),
        ),
        migrations.AlterField(
            model_name='course',
            name='document',
            field=models.CharField(choices=[('pasaporte', 'Pasaporte'), ('cedula de identidad', 'Cédula de identidad'), ('dni', 'DNI')], max_length=20, verbose_name='Tipo de documento'),
        ),
    ]
