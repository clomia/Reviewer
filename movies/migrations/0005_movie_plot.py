# Generated by Django 2.2.5 on 2020-11-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201123_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True),
        ),
    ]
