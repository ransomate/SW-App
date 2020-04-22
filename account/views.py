from django.shortcuts import render
from datetime import datetime
from .forms import UserUpdateForm


def logout(request):
    return render(request, 'account/base.html', {'section': 'dashboard'})


def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        update_form = form.save(commit=False)
        update_form.last_update_date = datetime.now()
        update_form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'account/update.html', {'form': form})
