# Generated by Django 5.0.6 on 2024-07-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='media/', verbose_name='Image')),
                ('create_at', models.TimeField(auto_now=True)),
            ],
        ),
    ]
