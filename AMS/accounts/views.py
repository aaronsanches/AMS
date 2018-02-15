from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import PersonCreationForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You're at the accounts index.")


def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:index')
    else:
        form = PersonCreationForm()
    return render(request, 'registration/register.html', {'form': form})
