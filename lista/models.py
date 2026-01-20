from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

# 1. DEFINIMOS LA CONSTANTE QUE FALTABA
CATEGORIAS = [
    ('BASICO', 'Básico'),
    ('OCASIONAL', 'Ocasional'),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS) # <--- Ahora ya existe
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    en_casa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    # MÉTODO PARA COMPRIMIR LA IMAGEN (Ahorro de espacio en Railway)
    def save(self, *args, **kwargs):
        if self.imagen:
            # Abrimos la imagen con Pillow
            img = Image.open(self.imagen)
            
            # 1. Redimensionar si es muy grande (max 800px)
            if img.height > 800 or img.width > 800:
                img.thumbnail((800, 800))
            
            # 2. Comprimir y convertir a JPEG para ahorrar espacio
            buffer = BytesIO()
            img = img.convert('RGB') 
            img.save(buffer, format='JPEG', quality=70) # 70% de calidad es el punto dulce
            
            # 3. Reemplazar la imagen original con la procesada
            nombre_archivo = os.path.splitext(self.imagen.name)[0] + '.jpg'
            self.imagen.save(nombre_archivo, ContentFile(buffer.getvalue()), save=False)
            
        super().save(*args, **kwargs)