from django.contrib import admin
from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin

@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'title', 'order')
    readonly_fields = ('order',)

    def admin_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 150px; height: auto;" />')
        return '-'
    admin_thumbnail.short_description = 'Preview'
    admin_thumbnail.allow_tags = True


class SliderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'move_up_down_links')