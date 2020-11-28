# Generated by Django 2.2.5 on 2020-11-23 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
        ('movies', '0002_auto_20201122_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('list_name', models.CharField(default='My favorite list', max_length=30)),
                ('book', models.ManyToManyField(to='books.Book')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ManyToManyField(to='movies.Movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]