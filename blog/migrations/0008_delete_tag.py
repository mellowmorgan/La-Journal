# Generated by Django 3.2.5 on 2021-08-27 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
