from django.shortcuts import render
from .models import Nauczyciel

def nauczyciel_list(request):
    nauczciele = Nauczyciel.objects.all()
    return render(request, 'szkola/nauczyciel_list.html', {'nauczyciele':nauczciele})