# Generated by Django 4.2.4 on 2023-12-18 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sumo', '0001_initial'),
        ('Fight', '0002_alter_fight_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='winner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='Sumo.sumo'),
        ),
    ]
