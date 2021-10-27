from django.shortcuts import render

names_list=['Emiliano', 'Paola', 'Nicholas', 'Michael', 'Cassandra']
# Create your views here.
def hello(request, name='world'):
    if request.method == 'GET':
        return render(request, 'hello.html', context = {'name': name, 'users': names_list})

def goodbye(request, name='django'):
    if request.method == 'GET':
        return render(request, 'goodbye.html', context = {'name': name})

