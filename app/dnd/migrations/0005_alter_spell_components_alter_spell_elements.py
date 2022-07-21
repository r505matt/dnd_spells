# Generated by Django 4.0.4 on 2022-06-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0004_remove_spell_duration_num_remove_spell_duration_str_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='components',
            field=models.ManyToManyField(related_name='components', to='dnd.spell_component'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='elements',
            field=models.ManyToManyField(blank=True, related_name='elements', to='dnd.element'),
        ),
    ]