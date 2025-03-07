# Generated by Django 4.1 on 2023-11-28 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0010_contest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userteam',
            name='name',
            field=models.CharField(default='T1', max_length=5),
        ),
        migrations.AlterField(
            model_name='userteamcontest',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userteams', to='cricket.contest'),
        ),
        migrations.AlterField(
            model_name='userteamcontest',
            name='user_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='cricket.userteam'),
        ),
    ]
