from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages



def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = TaskForm()

    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request=request,template_name='tasks/list.html',context=context)


@login_required(login_url='login')
def update_task(request,pk_test):
    task = Task.objects.get(id=pk_test)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            title =  form.cleaned_data.get('title')
            messages.success(request,f'{title} was updated sucessfully')
        return redirect('home')
    else:
        form = TaskForm(instance=task)
    context={
        'form':form
    }
    return render(request,'tasks/update_task.html',context=context)

@login_required(login_url='login')
def delete_task(request,pk_test):
    task = Task.objects.get(id=pk_test)
    if request.method == 'POST':
        task.delete()
        messages.success(request,f'{task} was deleted successfully')
        return redirect('home')
    context={'item':task}
    return render(request,'tasks/delete.html',context=context)
