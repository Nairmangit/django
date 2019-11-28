from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

def index(request):
    form = TodoForm()
    todo_list = Todo.objects.order_by('id')
    context = {'todo_list':todo_list, 'form':form}
    return render(request, 'todo/index.html', context)
    
@require_POST
def Add(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new = Todo(text=request.POST['text'])
        new.save()
    return redirect('index')
    
def Complete(request, comp_id):
    comp = Todo.objects.get(pk=comp_id)
    comp.complete = True
    comp.save()
    return redirect('index')
    
def dComplete(request, comp_id):
    comp = Todo.objects.get(pk=comp_id)
    comp.complete = False
    comp.save()
    return redirect('index')
    
def deleteComp(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
    