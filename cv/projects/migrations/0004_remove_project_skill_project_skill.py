# Generated by Django 4.0.1 on 2022-02-06 19:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('projects', '0003_remove_project_image_remove_project_sound_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skill',
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
