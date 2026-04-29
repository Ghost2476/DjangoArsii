from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',       admin.site.urls),
    path('',             include('accounts.urls')),
    path('dashboard/',   include('user_panel.urls')),
    path('management/',  include('admin_panel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
