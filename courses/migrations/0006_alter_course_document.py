# Generated by Django 4.1.6 on 2023-02-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_course_alter_course_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='document',
            field=models.CharField(choices=[('pasaporte', 'Pasaporte'), ('cedula de identidad', 'Cédula de identidad'), ('dni', 'DNI')], max_length=20, verbose_name='Tipo de documento'),
        ),
    ]
