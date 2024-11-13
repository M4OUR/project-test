from django.db import models
from filer.fields.image import FilerImageField
from adminsortable2.admin import SortableAdminMixin

class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)  # on_delete корректно указан
    order = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ['order']  # Установка порядка объектов по полю 'order'

    def __str__(self):
        return self.title
