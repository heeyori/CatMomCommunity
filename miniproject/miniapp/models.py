# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    neutral = models.CharField(max_length=20)
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location')
    appearance = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cat'


class CatBoard(models.Model):
    board_id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Cat, models.DO_NOTHING)
    user_no = models.ForeignKey('User', models.DO_NOTHING, db_column='user_no')
    date_time = models.DateTimeField()
    board_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cat_board'


class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True)
    user_no = models.ForeignKey('User', models.DO_NOTHING, db_column='user_no')
    cat = models.ForeignKey(Cat, models.DO_NOTHING)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Feed'


class Location(models.Model):
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    location3 = models.CharField(max_length=50)
    location4 = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Location'


class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'User'


class UserHasCat(models.Model):
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    cat = models.ForeignKey(Cat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'User_has_Cat'