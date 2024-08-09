# Generated by Django 5.0.7 on 2024-08-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('post_blog', models.TextField(max_length=5000)),
                ('post_image', models.ImageField(upload_to='')),
                ('date_of_post', models.DateField()),
                ('post_category', models.CharField(max_length=30)),
                ('post_user_name', models.CharField(max_length=30)),
                ('post_user_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
