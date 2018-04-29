from django.shortcuts import redirect, render

from .forms import PersonCreationForm


def index(request):
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
