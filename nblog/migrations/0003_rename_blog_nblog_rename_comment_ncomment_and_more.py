# Generated by Django 5.0.6 on 2024-05-14 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nblog', '0002_reply_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='NBlog',
        ),
        migrations.RenameModel(
            old_name='Comment',
            new_name='NComment',
        ),
        migrations.RenameModel(
            old_name='Reply',
            new_name='NReply',
        ),
    ]
