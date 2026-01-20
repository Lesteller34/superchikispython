from django.contrib import admin
from django.urls import path
from lista import views
from django.conf import settings # IMPORTANTE
from django.conf.urls.static import static # IMPORTANTE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('marcar/<int:producto_id>/', views.marcar_comprado, name='marcar_comprado'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

# ESTA ES LA PIEZA QUE FALTA PARA QUE SE VEAN LAS FOTOS
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # En Railway, aunque DEBUG sea False, necesitamos servir los media así
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)