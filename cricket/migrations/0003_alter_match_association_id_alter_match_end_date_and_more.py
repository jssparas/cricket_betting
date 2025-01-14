# Generated by Django 4.1 on 2023-10-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0002_remove_userteamcontest_unique_user_contest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='association_id',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='short_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='subtitle',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='target_info',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_a_score',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_b_score',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_info',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='last_scheduled_match_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
