# Generated by Django 4.0.4 on 2022-06-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0003_auto_20220509_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='duration_num',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='duration_str',
        ),
        migrations.AddField(
            model_name='spell',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='spell',
            name='area',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='spell',
            name='area_shape',
            field=models.CharField(blank=True, choices=[('cone', 'Cone'), ('sphere', 'Sphere'), ('square', 'Square'), ('line', 'Line'), ('feet2', 'Feet²'), ('flat_square', 'Flat Square'), ('cylinder', 'Cylinder')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='range',
            field=models.IntegerField(default=0),
        ),
    ]
