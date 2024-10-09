
from django.contrib import admin
from django.urls import path, include
from secondleg_app import views as secondleg_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',secondleg_views.index, name='index'),
    path('secondleg/',include('secondleg_app.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
