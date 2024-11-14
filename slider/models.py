from django.db import models
from filer.fields.image import FilerImageField
from adminsortable2.admin import SortableAdminMixin

class SliderItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE, verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, editable=False, verbose_name="Порядок")

    class Meta:
        ordering = ['order']  # Установка порядка объектов по полю 'order'
        verbose_name = "Элемент слайдера"
        verbose_name_plural = "Элементы слайдера"

    def __str__(self):
        return self.title
