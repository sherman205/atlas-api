# Generated by Django 3.0.3 on 2020-02-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0002_auto_20200218_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='map_search_text',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
