# project/urls.py
from django.contrib import admin
from slider.views import home_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Путь к главной странице с слайдером
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
