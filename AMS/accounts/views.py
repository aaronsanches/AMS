from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView

from .forms import PersonCreationForm
from .models import *


# Create your views here.


def index(request):
    # return HttpResponse("Hello, World. You're at the accounts index.")
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile')
    else:
        form = PersonCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


