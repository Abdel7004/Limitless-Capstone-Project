# Generated by Django 4.2.2 on 2023-07-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_bio_workout_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('sets', models.CharField(max_length=150)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='main_app.workout')),
            ],
        ),
    ]
