# Generated by Django 5.1.3 on 2024-12-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_book_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo_of_book',
        ),
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='kitob rasmini kiriting'),
        ),
    ]