# Generated by Django 3.1.6 on 2022-10-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
                ('text', models.TextField(default='', verbose_name='正文')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '关于网站',
                'verbose_name_plural': '关于网站',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
                ('text', models.TextField(default='', verbose_name='正文')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '个人简历',
                'verbose_name_plural': '个人简历',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
                ('name', models.CharField(default="Lynn's Nest", max_length=64, verbose_name='网站名称')),
                ('url', models.CharField(default='lynnwang.me', max_length=128, verbose_name='网站url')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('image', models.ImageField(null=True, upload_to='image', verbose_name='主页头像')),
                ('bio', models.CharField(default='', max_length=256, verbose_name='简介')),
                ('animation', models.BooleanField(default=True, verbose_name='启用动画')),
                ('blog', models.BooleanField(default=True, verbose_name='启用Blog')),
                ('projects', models.BooleanField(default=True, verbose_name='启用项目展示')),
                ('about', models.BooleanField(default=True, verbose_name='启用介绍')),
                ('resume', models.BooleanField(default=True, verbose_name='启用简历')),
                ('email', models.TextField(blank=True, null=True, verbose_name='邮箱')),
                ('github', models.TextField(blank=True, null=True, verbose_name='GitHub')),
                ('indienova', models.TextField(blank=True, null=True, verbose_name='Indienova')),
                ('facebook', models.TextField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.TextField(blank=True, null=True, verbose_name='Twitter')),
                ('linkedin', models.TextField(blank=True, null=True, verbose_name='LinkIn')),
                ('instagram', models.TextField(blank=True, null=True, verbose_name='Instagram')),
                ('width', models.IntegerField(choices=[(1, 'normal'), (2, 'large')], default=1, verbose_name='布局')),
            ],
            options={
                'verbose_name': '网站设置',
                'verbose_name_plural': '网站设置',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32, verbose_name='名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, 'blog'), (1, 'project')], verbose_name='栏目')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='标题图片')),
                ('content', models.TextField(default='', verbose_name='正文')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '发表内容',
                'verbose_name_plural': '发表内容',
            },
        ),
    ]