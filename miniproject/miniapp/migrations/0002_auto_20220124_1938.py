# Generated by Django 2.2.5 on 2022-01-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]