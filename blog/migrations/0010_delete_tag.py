# Generated by Django 3.2.5 on 2021-08-27 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
