from django.contrib import admin
from django.urls import path
from lista import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('marcar/<int:producto_id>/', views.marcar_comprado, name='marcar_comprado'),
    # ESTA ES LA LÍNEA QUE TE FALTA:
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]