# Generated by Django 3.0.6 on 2020-05-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliohome', '0002_auto_20200530_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='rdesc',
            new_name='desc',
        ),
    ]