import os
import sys
from django.core import serializers
import json
import codecs

# Nombre del archivo JSON de datos que tienes en el servidor
FIXTURE_FILE = 'datos_finales.json'

def load_data_from_json():
    # 1. Configurar Django para hablar con la base de datos
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        import django
        django.setup()
    except Exception as e:
        print(f"Error de configuración de Django: {e}")
        sys.exit(1)
        
    try:
        # 2. Leer el archivo JSON usando la codificación 'latin-1' (la que soluciona el error)
        print(f"Leyendo el archivo {FIXTURE_FILE} con codificación latin-1...")
        
        with codecs.open(FIXTURE_FILE, 'r', encoding='latin-1') as f:
            # Deserializará los datos del JSON
            objects = serializers.deserialize('json', f, ignorenonexistent=True)
            
            count = 0
            for obj in objects:
                obj.save()
                count += 1
            
            print("-" * 40)
            print(f"¡ÉXITO! Se cargaron {count} objetos (ubicaciones y usuarios) en la base de datos de AWS.")
            print("-" * 40)

    except Exception as e:
        print("\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR FATAL AL CARGAR DATOS.")
        print(f"Detalle: {e}")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit(1)

if __name__ == '__main__':
    load_data_from_json()