# Generated by Django 5.0.6 on 2024-06-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='favorite_food',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='major',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='nickname',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.CharField(default=20030303, max_length=8),
            preserve_default=False,
        ),
    ]
