# Generated by Django 4.1.6 on 2023-02-07 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipes_image_alter_recipes_ingredients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='recipe',
            new_name='description',
        ),
    ]
