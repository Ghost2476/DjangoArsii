from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/',       admin.site.urls),
    path('',             RedirectView.as_view(url='/login/')),
    path('',             include('accounts.urls')),
    path('dashboard/',   include('user_panel.urls')),
    path('management/',  include('admin_panel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)