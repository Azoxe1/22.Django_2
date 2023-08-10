from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def menu(request):
    template_name = 'calculator/home.html'
    main = {
        'Омлет': reverse('omlet'),
        'Макарохи': reverse('pasta'),
        'Бутер': reverse('buter')
    }
    context = {
        'main': main
    }
    return render(request, template_name, context) 

def omlet (request):
    counter = int(request.GET.get("servings", 1))
    context = {
    'recipe': {
    'яйца, шт': (DATA['omlet']['яйца, шт'] * counter),
    'молоко, л': (DATA['omlet']['молоко, л'] * counter),
    'соль, ч.л.': (DATA['omlet']['соль, ч.л.'] * counter),
        }
    }
    return render (request, 'calculator/index.html', context)

def pasta (request):
    counter = int(request.GET.get("servings", 1))
    context = {
    'recipe': {
    'макароны, г': (DATA['pasta']['макароны, г'] * counter),
    'сыр, г': (DATA['pasta']['сыр, г'] * counter),
        }
    }
    return render (request, 'calculator/index.html', context)
    
def buter (request):
    counter = int(request.GET.get("servings", 1))
    context = {
    'recipe': {
    'хлеб, ломтик': (DATA['buter']['хлеб, ломтик'] * counter),
    'колбаса, ломтик': (DATA['buter']['колбаса, ломтик'] * counter),
    'сыр, ломтик': (DATA['buter']['сыр, ломтик'] * counter),
    'помидор, ломтик': (DATA['buter']['помидор, ломтик'] * counter),
        }
    }
    return render (request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
