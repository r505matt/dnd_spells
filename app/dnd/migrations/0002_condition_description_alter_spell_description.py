# Generated by Django 4.0.4 on 2022-05-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='spell',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
