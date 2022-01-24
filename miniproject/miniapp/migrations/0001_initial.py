# Generated by Django 2.2.5 on 2022-01-24 04:31

from django.db import migrations, models
import miniapp.utlils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('neutral', models.CharField(max_length=10)),
                ('location1', models.CharField(max_length=50)),
                ('location2', models.CharField(max_length=50)),
                ('location3', models.CharField(max_length=50)),
                ('appearance', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=miniapp.utlils.upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('user_pw', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=100)),
                ('user_nickname', models.CharField(max_length=50)),
                ('user_bitrh', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
            ],
        ),
    ]
