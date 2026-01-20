from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('BASICO', 'Básico (Siempre hay)'),
        ('OCASIONAL', 'Ocasional (Desodorante, Talcos, etc.)'),
    ]

    nombre = models.CharField(max_length=100)
    en_casa = models.BooleanField(default=True) 
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='BASICO')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre