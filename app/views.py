from django.http import HttpResponse
from django.shortcuts import render
import common.views as commonViews
from .models import SobunPost
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return sobun_list(request)
    return commonViews.index(request)
    

def sobun_list(request):
    sobun_post_list = SobunPost.objects.order_by('-updated_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(sobun_post_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }
    return render(request, 'app/sobun/list.html', context)


def sobun_post(request, post_id):
    post = SobunPost.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'app/sobun/post.html', context)