# Generated by Django 4.2.2 on 2023-07-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_routine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='workouts',
        ),
        migrations.AddField(
            model_name='routine',
            name='sets',
            field=models.ManyToManyField(to='main_app.set'),
        ),
    ]
