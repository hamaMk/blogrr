# Generated by Django 4.1.7 on 2023-03-28 12:41

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_blogpostadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
