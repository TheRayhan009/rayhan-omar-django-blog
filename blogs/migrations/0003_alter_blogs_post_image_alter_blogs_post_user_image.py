# Generated by Django 5.0.7 on 2024-08-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogs_post_image_alter_blogs_post_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='post_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_user_image',
            field=models.ImageField(upload_to=''),
        ),
    ]