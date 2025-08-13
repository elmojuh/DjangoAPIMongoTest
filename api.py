#!/usr/bin/env python
import os
import sys
from django.urls import path, include
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from .mongo import get_db


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()

def home(request):
    return JsonResponse({"welcome": "Welcome to the world of Mongo!"})

def get_animals(request):
    db = None
    try:
        db = get_db()
        animals_cursor = db.animal_tb.find()
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in animals_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    finally:
        if db:
            db.client.close()

def get_wild_animals(request):
    db = None
    try:
        db = get_db()
        wild_cursor = db.animal_tb.find({"type": "Wild"})
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in wild_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    finally:
        if db:
            db.client.close()

urlpatterns = [
    path('', include('animals.urls')),
    path('', home, name='home'),
    path('animals', get_animals, name='get_animals'),
    path('animals/wild', get_wild_animals, name='get_wild_animals'),
]

def home(request):
    return JsonResponse({"welcome": "Welcome to the world of Mongo!"})

def get_animals(request):
    db = None
    try:
        db = get_db()
        animals_cursor = db.animal_tb.find()
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in animals_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    finally:
        if db:
            db.client.close()

def get_wild_animals(request):
    db = None
    try:
        db = get_db()
        wild_cursor = db.animal_tb.find({"type": "Wild"})
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in wild_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    finally:
        if db:
            db.client.close()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Verifique se está instalado."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()