from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event

# Create your views here.
def event_list(request):
    event_post_list = Event.objects.order_by('-updated_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(event_post_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }
    return render(request, 'event/list.html', context)


def event_post(request, event_id):
    post = Event.objects.get(id=event_id)
    context = {
        'post': post
    }
    return render(request, 'event/post.html', context)
