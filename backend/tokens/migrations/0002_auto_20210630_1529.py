# Generated by Django 3.1 on 2021-06-30 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paswordlesstoken',
            old_name='token',
            new_name='token_id',
        ),
    ]
