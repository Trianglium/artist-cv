# Generated by Django 4.0.1 on 2022-02-18 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_rename_info_link_alt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='alt',
            field=models.CharField(blank=True, help_text='(Optional) Add a Short Description for this URL. This field is public.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='label',
            field=models.CharField(help_text='Website Name or other label for this link. IE "LinkedIn", "Soundcloud", etc.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(help_text='Enter the URL for the link', max_length=1500, unique=True, validators=[django.core.validators.URLValidator(message='Enter a valid (unqiue) URL')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(blank=True, help_text='Input the main body of text (aka the main content)', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content_upload',
            field=models.ManyToManyField(help_text='Upload the Content to use with this project post and to store in memory. \nUploading media content does not work through the administration panel.', related_name='project_content', to='projects.Content'),
        ),
        migrations.AlterField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(blank=True, help_text='Copy and Paste the url to the external content you want to include', related_name='projects', to='projects.Link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(help_text='Add a brief summary to show as a preview of the main content', max_length=155),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Title for this contentto be used as the headline', max_length=200),
        ),
    ]
