# Generated by Django 3.1 on 2020-10-18 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notepad', '0008_auto_20201017_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='file',
        ),
    ]