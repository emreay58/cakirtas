# Generated by Django 4.1.5 on 2023-02-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_proje_description1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='message',
            field=models.TextField(blank=True, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='İsim Soyisim'),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='telefon',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefon'),
        ),
    ]
