# Generated by Django 4.1 on 2023-10-14 07:23

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_alter_match_association_id_alter_match_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='flag',
            field=models.ImageField(null=True, upload_to=pathlib.PurePosixPath('/Users/paras.gupta/Documents/paras/alltime11-backend/media')),
        ),
    ]
