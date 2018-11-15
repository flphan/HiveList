# Generated by Django 2.1.1 on 2018-11-15 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HiveList', '0024_auto_20181105_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_creator_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
