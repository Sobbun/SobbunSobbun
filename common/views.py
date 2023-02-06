from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import SignupForm, UpdateProfileForm
from .models import Event



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


def event_list(request):
    event_post_list = Event.objects.order_by('-updated_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(event_post_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }
    return render(request, 'common/event/list.html', context)


def event_post(request, event_id):
    post = Event.objects.get(id=event_id)
    context = {
        'post': post
    }
    return render(request, 'common/event/post.html', context)




# 프로필
@login_required
def profile_update(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            


            return redirect('common:profile_edit')
    else:
        form = UpdateProfileForm()
    return render(request, 'common/profile/edit.html', { 'form': form })