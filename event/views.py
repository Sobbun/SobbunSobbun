from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Event
class EventListView(generic.ListView):
    model = Event
    ordering = '-updated_at'
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'event/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_deleted=False)


class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'post'
    template_name = 'event/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Event, pk = self.kwargs['pk'])
        if post.is_deleted and not self.request.user.is_superuser:
            raise Http404
        return context
