# Generated by Django 3.1 on 2020-10-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notepad', '0006_auto_20201012_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='code',
            field=models.TextField(blank=True, default=None),
        ),
    ]