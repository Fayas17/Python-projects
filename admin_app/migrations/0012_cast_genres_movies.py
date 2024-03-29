# Generated by Django 3.2.23 on 2024-01-02 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_auto_20240102_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default='no value')),
                ('language', models.CharField(max_length=25)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters')),
                ('trailer_video', models.FileField(blank=True, null=True, upload_to='add_trailer')),
                ('movie_video', models.FileField(blank=True, null=True, upload_to='add_movies')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movie_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='cast')),
                ('movie_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.movies')),
            ],
        ),
    ]
