# Generated by Django 5.0.6 on 2024-05-14 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nblog', '0003_rename_blog_nblog_rename_comment_ncomment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nreply',
            old_name='name',
            new_name='reply_name',
        ),
    ]
