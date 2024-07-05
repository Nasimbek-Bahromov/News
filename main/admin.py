from django.contrib import admin
from .models import News, VideoNews, Human, Contact
from django.urls import reverse
from django.utils.html import format_html


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_details', 'edit_link', 'delete_link']

    def short_details(self, obj):
        if len(obj.details)> 50:
            return obj.details[:45] + '...'
        return obj.details
    short_details.short_description = 'details'

    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True


class VideoNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_body', 'edit_link', 'delete_link']

    def short_body(self, obj):
        if len(obj.body)> 50:
            return obj.body[:45] + '...'
        return obj.body
    short_body.short_description = 'body'

    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True


class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'age', 'short_info', 'edit_link', 'delete_link']

    def short_info(self, obj):
        if len(obj.info)> 50:
            return obj.info[:45] + '...'
        return obj.info
    short_info.short_description = 'info'

    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'email', 'phone_number','message', 'edit_link', 'delete_link']

    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True

admin.site.register(Contact, ContactAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(VideoNews, VideoNewsAdmin)
admin.site.register(Human, HumanAdmin)
