# Generated by Django 2.1.1 on 2018-11-04 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0017_auto_20181104_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteInstance',
            fields=[
                ('vote_instance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('vote', models.CharField(blank=True, choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
                ('contributor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Contributor')),
                ('playlist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Playlist')),
            ],
        ),
    ]