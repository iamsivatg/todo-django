from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todoitem



def todoView(request):
    siva = Todoitem.objects.all()

    return render(request, 'todo.html', {'king' : siva})


def addTodo(request):
    new = Todoitem(contents = request.POST.get('contents'))
    new.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    r = Todoitem.objects.get(id=todo_id)
    r.delete()
    return HttpResponseRedirect('/todo/')


