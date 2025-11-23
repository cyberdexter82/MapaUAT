from django.contrib import admin
from .models import Ubicacion

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pos_x', 'pos_y')
    # Esto define qué campos salen y en qué orden
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'como_llegar')
        }),
        ('Coordenadas (Haz clic en el mapa de abajo)', {
            'fields': ('pos_x', 'pos_y', 'color'),
        }),
    )