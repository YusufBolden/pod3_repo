from django.shortcuts import render
from django.http import Http404
import random

# define ingredients outside of view functions
ingredients = {
    'meats':  ['ham', 'salami', 'turkey', 'chicken', 'meatball', 'tempeh'],
    'cheeses': ['cheddar', 'provolone', 'swiss', 'american', 'gruyere'],
    'toppings': ['lettuce', 'tomato', 'pickles', 'onions', 'peppers']
}


def sandwich(request):
    if request.method == 'GET':
        return render(request = request, 
                      template_name = 'sandwich.html', 
                      context = {'ingredients': ingredients.keys()})

def ingredients_list(request, ingredient_type):
    if request.method == 'GET':
        # if ingredient type doesn't exist, raise Http404
        if ingredient_type not in ingredients:
                    raise Http404(f'No such ingredient: {ingredient_type}')

        return render(request = request, template_name = 'ingredients_list.html', 
                      context={ 'ingredients': ingredients[ingredient_type],
                                'ingredient_type': ingredient_type })

def sandwich_generator(request):
    if request.method == 'GET':
        """ Build a random cold-cut sandwich """
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheeses'])
        selected_topping = random.choice(ingredients['toppings'])

        sandwich = f'{selected_meat} & {selected_cheese} with {selected_topping}'
        return render(request, 'sandwich_generator.html', context={ 'sandwich': sandwich })