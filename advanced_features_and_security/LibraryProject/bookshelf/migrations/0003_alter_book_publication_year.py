# Generated by Django 5.1 on 2024-08-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(),
        ),
    ]
