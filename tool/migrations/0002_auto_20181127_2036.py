# Generated by Django 2.1.3 on 2018-11-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Hisory',
        ),
    ]
