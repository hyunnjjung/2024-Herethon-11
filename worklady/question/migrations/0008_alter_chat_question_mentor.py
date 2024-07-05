# Generated by Django 5.0.6 on 2024-07-05 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_remove_profile_username_profile_user_and_more'),
        ('question', '0007_remove_chatrating_message_remove_chatrating_rater_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_question',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='myprofile.profile'),
        ),
    ]