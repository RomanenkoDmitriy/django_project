from django.shortcuts import render


from .forms import UserForm


def registration_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register_user.html', context)
