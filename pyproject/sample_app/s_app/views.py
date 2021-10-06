from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from s_app.models import S_app, S_appForm
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def index(request):
    applist =S_app.objects.all()
    context = {'applist':applist}
    return render(request,'s_app/index.html',context)

def new(request):
    return render(request,'s_app/new.html')

def add(request):
    t= S_app()
    t.todo_id=len(S_app.objects.order_by('-todo_id')) +1
    t.update_date = timezone.now()
    o = S_appForm(request.POST,instance=t)
    o.save()
    return HttpResponseRedirect(reverse('index'))


def detail(request,todo_id):
    s_app = S_app.objects.get(todo_id = todo_id)
    context =  {'s_app':s_app}
    return render(request,'s_app/new.html',context)
     

def update(request,todo_id):
    o = S_app.objects.get(todo_id =todo_id)
    form = S_appForm(request.POST,instance =o) 
    form.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,todo_id):
    o = S_app.objects.get(todo_id =todo_id)
    o.delete()
    return HttpResponseRedirect(reverse('index'))