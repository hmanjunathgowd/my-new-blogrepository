# Generated by Django 2.1.2 on 2019-07-11 17:52

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0005_auto_20190711_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.Post'),
        ),
    ]
