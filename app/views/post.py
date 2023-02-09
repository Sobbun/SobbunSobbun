from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from functools import reduce
import operator
from django.urls import reverse_lazy
from ..models import SobunPost, GoodsCategory, Sobun
from ..forms import SobunPostForm



class PostListView(LoginRequiredMixin, generic.ListView):
    model = SobunPost
    ordering = '-updated_at'
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'app/sobun/list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search')
        category = self.request.GET.get('category')

        q = Q(is_deleted=False)
        if search:
            q &= reduce(operator.and_, (Q(title__contains=x) for x in search.split() ))
        if category:
            q &= Q(category__name=category)

        return qs.filter(q)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GoodsCategory.objects.all
        context['selected_category'] = self.request.GET.get('category')
        context['searched'] = self.request.GET.get('search')
        return context


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = SobunPost
    context_object_name = 'post'
    template_name = 'app/sobun/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(SobunPost, pk = self.kwargs['pk'])
        if post.is_deleted and not self.request.user.is_superuser:
            raise Http404
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = SobunPost
    form_class = SobunPostForm
    template_name = 'app/sobun/create.html'
    success_url = reverse_lazy('app:list')

    def form_valid(self, form) :
        form.instance.user = self.request.user
        form.instance.is_deleted = False
        return super().form_valid(form)


class PostHistoryListView(LoginRequiredMixin, generic.ListView):
    model = SobunPost
    ordering = '-updated_at'
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'app/sobun/history.html'

    def get_queryset(self):
        sobuns =  Sobun.objects.filter(Q(user=self.request.user) | Q(post__user=self.request.user))
        return SobunPost.objects.filter(sobun__in=sobuns)