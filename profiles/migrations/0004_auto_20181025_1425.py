# Generated by Django 2.0.2 on 2018-10-25 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20181025_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
    ]