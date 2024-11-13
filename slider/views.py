from django.shortcuts import render
from .models import SliderItem

def home_view(request):
    slider_items = SliderItem.objects.all()  # Получаем все элементы слайдера
    return render(request, 'main/base.html', {'slider_items': slider_items})
