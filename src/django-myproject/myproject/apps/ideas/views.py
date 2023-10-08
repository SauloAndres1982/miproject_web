
# Create your views here.
from django.shortcuts import render
from .models import Idea 

def idea_list(request):
    idea = Idea.objects.all()  # Recupera todas las ideas (esto es un ejemplo, puedes personalizarlo)
    return render(request, 'index.html', {'idea': idea})
