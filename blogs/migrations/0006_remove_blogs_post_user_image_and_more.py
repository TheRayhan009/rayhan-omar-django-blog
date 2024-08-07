# Generated by Django 5.0.7 on 2024-08-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blogs_a_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='post_user_image',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='post_user_name',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_image',
            field=models.ImageField(default=None, null=True, upload_to='blog/'),
        ),
    ]
