# Generated by Django 5.0.6 on 2024-07-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_videonews_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
