# Generated by Django 4.2.2 on 2023-07-12 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set',
            old_name='sets',
            new_name='rep',
        ),
    ]
