from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    # ... Otras URLs de la aplicación ...
    path('ideas', views.idea_list, name='idea_list'),
]
