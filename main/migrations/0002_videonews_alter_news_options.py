# Generated by Django 5.0.6 on 2024-07-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videolar',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
    ]
