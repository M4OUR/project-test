from django.contrib import admin
from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
from adminsortable2.admin import SortableAdminBase

@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'title', 'order')
    readonly_fields = ('order',)

    def admin_thumbnail(self, obj):
        if obj.image:
            # Создание миниатюры с помощью easy-thumbnails
            thumbnail_options = {'size': (150, 150), 'crop': True}
            thumbnail_url = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            return mark_safe(f'<img src="{thumbnail_url}" style="max-width: 150px; height: auto;" />')
        return '-'
    admin_thumbnail.short_description = 'Предпросмотр'
