# Generated by Django 4.0.1 on 2022-02-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='skill',
            new_name='skills',
        ),
    ]
