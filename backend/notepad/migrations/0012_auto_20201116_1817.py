# Generated by Django 3.1 on 2020-11-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notepad', '0011_note_delete_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='delete_time',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]