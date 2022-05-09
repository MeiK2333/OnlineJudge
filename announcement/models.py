from django.db import models

from account.models import User
from utils.models import RichTextField


class Announcement(models.Model):
    title = models.TextField()
    # HTML
    content = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update_time = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = "announcement"
        ordering = ("-create_time",)


class Carousel(models.Model):
    title = models.TextField()
    file_path = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    # 轮播图自定义播放顺序，大的在前面
    order = models.IntegerField()

    class Meta:
        db_table = "carousel"
        ordering = ("-order",)


class FriendshipLinks(models.Model):
    """ 友情链接 """
    title = models.TextField()
    link = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    order = models.IntegerField()

    class Meta:
        db_table = "friendship_links"
        ordering = ("-order",)
