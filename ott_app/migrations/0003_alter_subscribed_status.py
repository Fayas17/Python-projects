# Generated by Django 3.2.23 on 2024-01-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott_app', '0002_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribed',
            name='status',
            field=models.CharField(default='inactive', max_length=30),
        ),
    ]
