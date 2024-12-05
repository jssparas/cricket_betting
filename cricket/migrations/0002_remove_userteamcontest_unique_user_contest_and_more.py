# Generated by Django 4.1 on 2023-10-07 05:31

import alltime11.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userteamcontest',
            name='unique_user_contest',
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='is_all_rounder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='is_batsman',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='is_bowler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='is_vice_captain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userteam',
            name='keeper_count',
            field=models.IntegerField(default=0, validators=[alltime11.validators.validate_keeper_count]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userteamcontest',
            name='entry_type',
            field=models.CharField(choices=[('unique', 'unique'), ('multiple', 'multiple')], default='unique', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='batting_style',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='player',
            name='bowling_style',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddConstraint(
            model_name='userteamcontest',
            constraint=models.UniqueConstraint(condition=models.Q(('entry_type', 'unique')), fields=('user', 'contest', 'entry_type'), name='unique_user_contest'),
        ),
    ]
