from django.shortcuts import render, redirect
from .models import Producto

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')
        
        if nombre:
            Producto.objects.create(
                nombre=nombre, 
                categoria=categoria, 
                imagen=imagen,
                en_casa=True 
            )
        return redirect('index')

    comprar = Producto.objects.filter(en_casa=False)
    en_despensa = Producto.objects.filter(en_casa=True)
    return render(request, 'lista/index.html', {'comprar': comprar, 'en_despensa': en_despensa})

# ¡Asegurate de que esta función NO falte!
def marcar_comprado(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.en_casa = not producto.en_casa
    producto.save()
    return redirect('index')

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('index')