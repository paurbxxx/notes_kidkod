# Generated by Django 3.2 on 2022-04-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='delete',
            new_name='delete_status',
        ),
    ]
