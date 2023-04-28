from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .classifier import classify
from .models import Dish

from pathlib import Path
import json
import time
import os


@method_decorator(csrf_exempt, name='dispatch')
def api(request):
    if request.method == 'POST' and request.FILES:
        try:
            image = request.FILES['photo']
            name_dish = classify(image)
            recipe_dish = Dish.objects.get(name_dish=name_dish).recept_dish
            data = json.dumps({'name_dish': name_dish, 'recipe_dish': recipe_dish})
            return HttpResponse(data)
        except Exception as ex:
            return HttpResponse(json.dumps({'Error': f'{ex}'}))

    if request.method == 'GET':
        data = json.dumps({'name_dish': None, 'recipe_dish': None}, indent=2)
        return HttpResponse(data)
