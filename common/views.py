from django.shortcuts import render, redirect

from .forms import UserForm


# 가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('app:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', { 'form': form })


# 프로필
def profile(request):
    pass