# Generated by Django 4.1.6 on 2023-02-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='document',
            field=models.CharField(choices=[('dni', 'DNI'), ('cedula de identidad', 'Cédula de identidad'), ('pasaporte', 'Pasaporte')], max_length=20, verbose_name='Tipo de documento'),
        ),
    ]