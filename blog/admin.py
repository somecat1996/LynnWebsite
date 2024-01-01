from django.contrib import admin
from blog.models import SiteSetting, About, Resume, Post, Tag
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "enable", )
    list_editable = ("enable", )

    def save_model(self, request, obj, form, change):
        if obj.enable:
            site_settings = SiteSetting.objects.filter(enable=True)
            for i in range(len(site_settings)):
                site_settings[i].enable = False
                site_settings[i].save()
        super().save_model(request, obj, form, change)


class AboutAdmin(SummernoteModelAdmin):
    list_display = ("time", "enable", )
    list_editable = ("enable", )
    summernote_fields = ("text", )

    def save_model(self, request, obj, form, change):
        if obj.enable:
            abouts = About.objects.filter(enable=True)
            for i in range(len(abouts)):
                abouts[i].enable = False
                abouts[i].save()
        super().save_model(request, obj, form, change)


class ResumeAdmin(SummernoteModelAdmin):
    list_display = ("time", "enable", )
    list_editable = ("enable", )
    summernote_fields = ("text", )
    fields = ("file", )

    def save_model(self, request, obj, form, change):
        if obj.enable:
            resumes = Resume.objects.filter(enable=True)
            for i in range(len(resumes)):
                resumes[i].enable = False
                resumes[i].save()
        super().save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    list_display = ("tag", )


class PostAdmin(SummernoteModelAdmin):
    def show_tag(self, obj):
        tag = []
        for i in obj.tags.all():
            tag.append(i.tag)
        return ' '.join(tag)

    list_display = ("title", "star", "title_image", "category", "show_tag", "time")
    list_editable = ("category", "star", )
    list_filter = ("category", "tags")
    summernote_fields = ("content", "desc", )
    date_hierarchy = 'time'
    fields = ("category", "star", "create_time", "tags", "title", "title_image", "desc", "content")
    filter_horizontal = ('tags',)


admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
