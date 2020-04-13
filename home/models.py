# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mutagen.mp3 import MP3


class TAdmin(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    salt = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_admin'


class TAlbum(models.Model):
    album_title = models.CharField(max_length=50, blank=True, null=True)
    thumbnail_url = models.ImageField(upload_to='album_img')
    author = models.CharField(max_length=50, blank=True, null=True)
    bordcaster = models.CharField(max_length=50, blank=True, null=True)
    chapter_num = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    status = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)

    class Meta:
        db_table = 't_album'


class TAudioChapter(models.Model):
    chapter_name = models.CharField(max_length=50, blank=True, null=True)
    audio_size = models.CharField(max_length=50, blank=True, null=True)
    audio_duration = models.CharField(max_length=50, blank=True, null=True)
    audio_url = models.FileField(upload_to='audio')
    audio_id =  models.CharField(max_length=100, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 't_audio_chapter'


class TArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    thumbnail_url = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    teacher = models.ForeignKey('TTeacher', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pic_urls = models.CharField(max_length=100, blank=True, null=True)
    article_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_article'


class ArticleImg(models.Model):
    img_url = models.ImageField(upload_to='article_img')

    class Meta:
        managed = False
        db_table = "t_article_img"


class TSlidpic(models.Model):
    url = models.ImageField(upload_to='slidpic')
    title = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 't_slidpic'


class TTask(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    task_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_task'


class TTaskCounter(models.Model):
    count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    crate_date = models.DateTimeField(blank=True, null=True)
    task = models.ForeignKey(TTask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_task_counter'


class TTeacher(models.Model):
    thumbnail = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teacher'


class TUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    register_time = models.DateTimeField(auto_now_add=False)
    thumbnail_url = models.ImageField(upload_to='userthumbnail')
    user_info = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    salt = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
