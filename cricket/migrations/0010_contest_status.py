# Generated by Django 4.1 on 2023-11-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0009_alter_tournament_association_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('started', 'Started'), ('completed', 'Completed')], default='not_started', max_length=20),
        ),
    ]
