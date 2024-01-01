from datetime import datetime
from django.db import models


# Create your models here.
class SiteSetting(models.Model):
    class Meta:
        verbose_name = "网站设置"
        verbose_name_plural = "网站设置"

    enable = models.BooleanField(verbose_name="启用", default=False)

    read_time = models.BooleanField(verbose_name="阅读时间", default=False)
    show_tags = models.BooleanField(verbose_name="显示tag", default=False)
    post_advance_links = models.BooleanField(verbose_name="高级链接", default=False)
    show_author = models.BooleanField(verbose_name="显示作者", default=False)

    name = models.CharField(verbose_name="网站名称", max_length=64, default="Lynn's Nest")
    url = models.CharField(verbose_name="网站url", max_length=128, default="lynnwang.me")
    time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    image = models.ImageField(verbose_name="主页头像", upload_to="image", null=True)
    bio = models.CharField(verbose_name="简介", max_length=256, default="")

    animation = models.BooleanField(verbose_name="启用动画", default=True)
    blog = models.BooleanField(verbose_name="启用Blog", default=True)
    projects = models.BooleanField(verbose_name="启用项目展示", default=True)
    about = models.BooleanField(verbose_name="启用介绍", default=True)
    resume = models.BooleanField(verbose_name="启用简历", default=True)

    email = models.TextField(verbose_name="邮箱", blank=True, null=True)
    github = models.TextField(verbose_name="GitHub", blank=True, null=True)
    indienova = models.TextField(verbose_name="Indienova", blank=True, null=True)
    facebook = models.TextField(verbose_name="Facebook", blank=True, null=True)
    twitter = models.TextField(verbose_name="Twitter", blank=True, null=True)
    linkedin = models.TextField(verbose_name="LinkIn", blank=True, null=True)
    instagram = models.TextField(verbose_name="Instagram", blank=True, null=True)

    width = models.IntegerField(
        verbose_name="布局",
        choices=[
            (1, "normal"),
            (2, "large")
        ],
        default=1)

    def __str__(self):
        return self.name


class About(models.Model):
    class Meta:
        verbose_name = "关于网站"
        verbose_name_plural = "关于网站"

    enable = models.BooleanField(verbose_name="启用", default=False)
    text = models.TextField(verbose_name="正文", default="")
    time = models.DateTimeField(verbose_name="修改时间", auto_now=True)


class Resume(models.Model):
    class Meta:
        verbose_name = "个人简历"
        verbose_name_plural = "个人简历"

    enable = models.BooleanField(verbose_name="启用", default=False)
    text = models.TextField(verbose_name="正文", default="")
    time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    file = models.FileField(verbose_name="简历附件", null=True, blank=True)


class Tag(models.Model):
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    tag = models.CharField(verbose_name="名称", max_length=32)

    def __str__(self):
        return self.tag


class Post(models.Model):
    class Meta:
        verbose_name = "发表内容"
        verbose_name_plural = "发表内容"

    category = models.IntegerField(verbose_name="栏目", choices=((0, "blog"), (1, "project")))
    title = models.CharField(verbose_name="标题", max_length=256)
    title_image = models.ImageField(verbose_name="标题图片", upload_to="image", null=True, blank=True)
    desc = models.TextField(verbose_name="描述", null=True, blank=True)
    content = models.TextField(verbose_name="正文", default="")
    time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now())
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    star = models.BooleanField(verbose_name="主页显示", default=False)
