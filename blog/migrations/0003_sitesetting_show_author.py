# Generated by Django 3.1.6 on 2022-10-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221007_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='show_author',
            field=models.BooleanField(default=False, verbose_name='显示作者'),
        ),
    ]
