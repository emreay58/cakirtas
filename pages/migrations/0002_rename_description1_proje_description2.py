# Generated by Django 4.1.5 on 2023-01-30 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proje',
            old_name='description1',
            new_name='description2',
        ),
    ]
