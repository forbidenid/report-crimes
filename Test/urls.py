from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('complaints/', include(('complaints.urls', 'complaints'), namespace='complaints'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)