# Generated by Django 4.1.5 on 2023-02-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_formmodel_email_alter_formmodel_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
