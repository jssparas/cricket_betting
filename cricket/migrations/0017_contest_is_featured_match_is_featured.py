# Generated by Django 4.1 on 2024-01-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0016_match_delayed_time_alter_tournament_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
