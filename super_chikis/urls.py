from django.contrib import admin
from django.urls import path
from django.conf import settings # <-- Importar settings
from django.conf.urls.static import static # <-- Importar static
from lista import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('marcar/<int:producto_id>/', views.marcar_comprado, name='marcar_comprado'),
]

# Esto es SOLO para desarrollo. En producción, Nginx o Apache lo manejan.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)