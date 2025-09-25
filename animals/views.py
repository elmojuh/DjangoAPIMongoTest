from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .services import AnimalService
import logging

logger = logging.getLogger('animals')

@require_http_methods(["GET"])
def home(request):
    """View para página inicial"""
    return JsonResponse({
        "welcome": "Welcome to the world of Mongo!",
        "endpoints": [
            "/animals/",
            "/animals/wild/"
        ]
    })

@require_http_methods(["GET"])
def get_animals(request):
    """View para listar todos os animais"""
    try:
        service = AnimalService()
        animals = service.get_all_animals()
        return JsonResponse({"animals": animals})
    except Exception as e:
        logger.error(f"Erro ao buscar animais: {e}")
        return JsonResponse({"error": "Erro interno do servidor"}, status=500)

@require_http_methods(["GET"])
def get_wild_animals(request):
    """View para listar apenas animais selvagens"""
    try:
        service = AnimalService()
        animals = service.get_animals_by_type("Wild")
        return JsonResponse({"animals": animals})
    except Exception as e:
        logger.error(f"Erro ao buscar animais selvagens: {e}")
        return JsonResponse({"error": "Erro interno do servidor"}, status=500)