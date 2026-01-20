from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Producto(models.Model):
    # ... tus campos actuales ...
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    en_casa = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.imagen:
            # Abrimos la imagen con Pillow
            img = Image.open(self.imagen)
            
            # 1. Redimensionar si es muy grande (max 800px)
            if img.height > 800 or img.width > 800:
                img.thumbnail((800, 800))
            
            # 2. Comprimir y convertir a JPEG
            buffer = BytesIO()
            img = img.convert('RGB') # Asegura compatibilidad
            img.save(buffer, format='JPEG', quality=70) # 70% de calidad es ideal
            
            # 3. Guardar el archivo procesado
            nombre_archivo = os.path.splitext(self.imagen.name)[0] + '.jpg'
            self.imagen.save(nombre_archivo, ContentFile(buffer.getvalue()), save=False)
            
        super().save(*args, **kwargs)