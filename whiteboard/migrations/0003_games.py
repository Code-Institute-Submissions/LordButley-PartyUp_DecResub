# Generated by Django 3.2.14 on 2022-07-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('ref_name', models.CharField(max_length=200)),
            ],
        ),
    ]
