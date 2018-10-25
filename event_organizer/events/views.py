from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})


def hola(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        return HttpResponseRedirect('/')


class IndexView(generic.TemplateView):
    template_name = 'index.html'
