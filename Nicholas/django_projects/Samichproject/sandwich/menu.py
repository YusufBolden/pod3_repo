from views import ingredients   
menulist = []
for meat in ingredients['meats']:
            for cheese in ingredients['cheeses']:
                for topping in ingredients['toppings']:
                    menulist.append(f'{meat} {cheese} with {topping}')
print(menulist)