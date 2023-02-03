from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, UpdateProfileForm



def index(request):
    return render(request, 'common/index.html')


# 가입
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # 유저 가입             
            user = form.save(commit=False)
            user.save()
            
            user.refresh_from_db()


            return redirect('common:profile_edit')
    else:
        form = SignupForm()
    return render(request, 'common/signup.html', { 'form': form })


# 프로필
@login_required
def profile_update(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            


            return redirect('common:profile_edit')
    else:
        form = UpdateProfileForm()
    return render(request, 'common/profile_update.html', { 'form': form })