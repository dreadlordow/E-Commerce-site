from django.shortcuts import render, redirect

from register.forms import RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context={
            'form': form
        }
        return render(request, 'register/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'register/register.html', context)
