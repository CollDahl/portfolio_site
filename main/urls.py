from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import main.views as views


urlpatterns = [
    path('', views.index, name='main_index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
