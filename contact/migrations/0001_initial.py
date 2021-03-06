# Generated by Django 2.0.2 on 2018-10-25 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('description', models.TextField(default='description default value')),
                ('location', models.TextField(default='my location')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.OneToOneField(default='update', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
