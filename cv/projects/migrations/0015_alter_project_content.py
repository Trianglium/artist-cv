# Generated by Django 4.0.1 on 2022-02-21 18:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_project_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Enter main content', null=True),
        ),
    ]
