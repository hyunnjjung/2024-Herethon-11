# Generated by Django 5.0.6 on 2024-07-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='career',
            field=models.ManyToManyField(blank=True, to='myprofile.career', verbose_name='경력'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.ManyToManyField(blank=True, to='myprofile.education', verbose_name='학력'),
        ),
    ]