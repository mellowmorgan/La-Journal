# Generated by Django 3.2.5 on 2021-08-25 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_tag_mytag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='myTag',
        ),
    ]