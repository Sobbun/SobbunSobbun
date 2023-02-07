from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from .models import Event

# Create your views here.
def event_list(request):
    event_post_list = Event.objects.filter(is_deleted=False).order_by('-updated_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(event_post_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }
    return render(request, 'event/list.html', context)


def event_post(request, event_id):
    post = get_object_or_404(Event, id=event_id)
    if post.is_deleted and not request.user.is_superuser:
        return HttpResponseNotFound("Not Found")

    context = {
        'post': post
    }
    return render(request, 'event/post.html', context)
