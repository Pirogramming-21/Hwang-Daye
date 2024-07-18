from django.shortcuts import render, redirect
from .models import Develop
from .forms import DevelopForm

def develop_list(request):
    devtools = Develop.objects.all()
    return render(request, 'develop/list.html', {'develop': devtools})

def develop_register(request):
    if request.method == 'POST':
        form = DevelopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('develop:list')
    else:
        form = DevelopForm()
    return render(request, 'develop/register.html', {'form': form})
