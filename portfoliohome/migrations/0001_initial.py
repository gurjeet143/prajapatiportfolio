# Generated by Django 3.0.6 on 2020-05-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('useremail', models.CharField(max_length=120)),
                ('useraddress', models.CharField(max_length=120)),
                ('usercity', models.CharField(max_length=120)),
                ('userstate', models.CharField(max_length=120)),
                ('userzip', models.CharField(max_length=120)),
                ('userdesc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
