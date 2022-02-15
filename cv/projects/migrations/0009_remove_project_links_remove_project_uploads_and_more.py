# Generated by Django 4.0.1 on 2022-02-15 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_content_remove_project_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='uploads',
        ),
        migrations.AddField(
            model_name='content',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='projects',
            field=models.ManyToManyField(help_text='Upload the Content to use with this project post and to store in memory.', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='link',
            name='projects',
            field=models.ManyToManyField(help_text='Copy and Paste the url to the external content you want to include', to='projects.Project'),
        ),
    ]