from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect





def index(request):
    publicos = flan.objects.filter(is_private = False)
    return render(request, 'index.html', { 
        'publicos' : publicos

    })

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})


def contacto(request):
    if request.method == 'POST':
        print(request.POST)

        form = ContactFormForm(request.POST)

        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito')
    
    else:
        form = ContactForm()
    return render (request, 'contact.html', {'form': form})


def index(request):
    flanes_publicos = flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def bienvenido(request):
    flanes_privados = flan.objects.filter(is_private=True)
    return render(request, 'bienvenido.html', {'flanes': flanes_privados})