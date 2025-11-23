from django.db import models
from django.contrib.auth.models import User

# Modelo de Usuario (Ya lo tenías, lo dejamos igual pero extendido si quisieras)
# Django usa su propio modelo User por defecto, así que no necesitamos redefinirlo 
# a menos que queramos agregar campos extra. Por ahora usamos el de Django.

# --- MODELO PARA EL MAPA ---
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Lugar")
    descripcion = models.TextField(verbose_name="Descripción / Qué hay aquí")
    como_llegar = models.TextField(verbose_name="Ruta / Cómo llegar", blank=True)
    
    # Coordenadas para el mapa (en Porcentaje % para que sea responsivo)
    pos_x = models.IntegerField(help_text="Posición Horizontal (0 a 100%)", default=50)
    pos_y = models.IntegerField(help_text="Posición Vertical (0 a 100%)", default=50)
    
    # Color del pin (Opcional)
    color = models.CharField(max_length=20, default="#d32f2f", help_text="Ej: #d32f2f (rojo), #1976d2 (azul)")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ubicación del Mapa"
        verbose_name_plural = "Ubicaciones del Mapa"