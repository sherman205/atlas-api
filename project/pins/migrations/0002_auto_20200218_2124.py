# Generated by Django 3.0.3 on 2020-02-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
