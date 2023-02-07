from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse

from ..models import Sobun, SobunPost
from ..forms import SobunForm

class RequestListView(LoginRequiredMixin, generic.ListView):
    model = Sobun
    ordering = '-updated_at'
    context_object_name = 'requests'
    template_name = 'app/request/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            Q(user__pk=self.request.user.id) | Q(post__user__pk=self.request.user.id)
        )


class PostRequestListView(LoginRequiredMixin, generic.ListView):
    model = Sobun
    ordering = '-updated_at'
    context_object_name = 'requests'
    template_name = 'app/request/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            Q(post__user__pk=self.request.user.id) | Q(user__pk=self.request.user.id),
            post__pk=self.kwargs['post_id'],
        )

class RequestCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sobun
    form_class = SobunForm
    template_name = 'app/request/edit.html'
    context_object_name = 'form'

    def form_valid(self, form):
        if form.instance.status != 1:
            raise Exception("BadRequest")

        post = get_object_or_404(SobunPost, pk = self.kwargs['post_id'])
        if post.is_deleted:
            raise Http404

        form.instance.post = post
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
       pk = self.object.id
       return reverse("app:request", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "create"
        return context

class RequestUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Sobun
    form_class = SobunForm
    template_name = 'app/request/edit.html'
    context_object_name = 'form'

    available_options = [
        { 'id': 0, 'name': "Denied" },
        { 'id': 1, 'name': "Requested" },
        { 'id': 2, 'name': "Accepted" },
        { 'id': 3, 'name': "Proceed" },
        { 'id': 4, 'name': "Complete" }
    ]

    def form_valid(self, form):
        # 거절 이외에는 상태가 아래로 내려갈 수 없다.
        if form.instance.status != 0 and form.instance.status < self.object.status:
            raise Exception("BadRequest")
        
        # 게시글 삭제시 미진행.
        if self.object.post.is_deleted:
            raise Http404

        return super().form_valid(form)

    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse("app:rate", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "update"
        # 거절은 따로 처리.
        context["available_option"] = list(filter(lambda x: x['id'] >= self.object.status, self.available_options))

        if self.object.status == 4:
            raise Exception("BadRequest")

        return context

class RequestDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sobun
    context_object_name = 'request'
    template_name = 'app/request/view.html'
