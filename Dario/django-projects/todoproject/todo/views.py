from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Note

# todo list homepage
def todo(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-task_id')
        form = TodoForm()
        return render(request=request,
                      template_name = 'list.html',
                      context = {'tasks':tasks, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            Todo.objects.create(task=task)
        # "redirect" to the todo homepage   
        return HttpResponseRedirect(reverse('todo'))


def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial = {'task':todo.task})
        return render(request = request,
                      template_name = 'detail.html',
                      context = {
                          'form':form,
                          'task_id': task_id
                      })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        elif 'completed' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(completed=True)
        return HttpResponseRedirect(reverse('todo'))

def notes(request, notes_id):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('notes_id')
        form = NoteForm()
        return render(request=request,
                    template_name = 'notes.html',
                    context = {'notes':notes, 'form':form})

    if request.method == 'POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            notes = form.cleaned_data['notes']
            Note.objects.create(notes=notes)
        # "redirect" to the notes homepage   
        return HttpResponseRedirect(reverse('notes'))