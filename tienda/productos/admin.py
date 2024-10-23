from django.contrib import admin
from .models import Fabricante, Producto

# Registrar los modelos en el admin
admin.site.register(Fabricante)
admin.site.register(Producto)
