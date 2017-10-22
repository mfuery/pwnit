from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = authenticate(username=username)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})
