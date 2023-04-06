from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .classifier import get_dish
from .models import Dish
import json
import os


@method_decorator(csrf_exempt, name='dispatch')
def api(request):
    if request.method == 'POST' and request.FILES:
        try:
            file = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)

            name_dish = get_dish(file_url)
            os.remove(f'.{file_url}')
            recipe_dish = Dish.objects.get(name_dish=name_dish).recept_dish
            data = json.dumps({'name_dish': name_dish, 'recipe_dish': recipe_dish})

            return HttpResponse(data)
        except:
            return HttpResponse(json.dumps({'Error': 'Example request.POST: {"photo": file}'}))

    if request.method == 'GET':
        data = json.dumps({'name_dish': None, 'recipe_dish': None}, indent=2)
        return HttpResponse(data)
