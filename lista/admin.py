from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Quitamos la barra de "Acción" y el contador
    actions = None
    actions_selection_counter = False
    
    # Configuramos las columnas
    list_display = ('nombre', 'categoria', 'en_casa', 'boton_borrar')
    list_filter = ('en_casa', 'categoria')
    search_fields = ('nombre',)

    # Creamos un botón de borrar estético
    def boton_borrar(self, obj):
        url = reverse('admin:lista_producto_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="background-color: #e74c3c; color: white; border-radius: 8px; padding: 4px 12px; font-weight: bold;">BORRAR</a>',
            url
        )
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }
    
    boton_borrar.short_description = 'Acciones rápidas'

