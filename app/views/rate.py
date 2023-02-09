from django.db.models import Q
from django.core.exceptions import BadRequest
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse

from ..models import Sobun, SobunRate, SobunStatus
from ..forms import SobunRateForm

# 게시글 조회
class RateListView(LoginRequiredMixin, generic.ListView):
    model = SobunRate
    ordering = '-created_at'
    context_object_name = 'rates'
    paginate_by = 10
    template_name = 'app/rate/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(Q(user_to__pk=self.kwargs["pk"]) | Q(user_from__pk=self.kwargs["pk"]))

# request 유저 조회
class RateUserListView(LoginRequiredMixin, generic.ListView):
    model = SobunRate
    ordering = '-created_at'
    context_object_name = 'rates'
    paginate_by = 10
    template_name = 'app/rate/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(Q(user_to=self.request.user) | Q(user_from=self.request.user))

class RateCreateView(LoginRequiredMixin, generic.CreateView):
    model = SobunRate
    form_class = SobunRateForm
    template_name = 'app/rate/create.html'
    context_object_name = 'form'

    def form_valid(self, form):
        # 완료된 소분 내역이 없을시 + 요청 유저가 둘 중 하나가 아닐시
        sobun_query = Sobun.objects.filter(
            Q(user=self.request.user.id) | Q(post__user=self.request.user.id),
            pk=self.kwargs['sobun_id'], status=SobunStatus.COMPLETE)
        if not sobun_query.exists():
            raise BadRequest("This sobun can't be rated")

        # 평가 내역이 있을시
        rate_query = SobunRate.objects.filter(user_from=self.request.user, sobun__pk=self.kwargs['sobun_id'])
        if rate_query.exists():
            raise BadRequest("Already rated")

        sobun = Sobun.objects.get(pk=self.kwargs['sobun_id'])

        post_user = sobun.post.user
        sobun_user = sobun.user

        # 두명이 같을시, 다만 DEBUG 상태에서는 무시.
        if sobun_user == post_user and not settings.DEBUG:
            raise BadRequest("User can't not be rate this sobun as it is same user")

        form.instance.user_from = self.request.user
        form.instance.user_to = post_user if sobun_user == self.request.user else sobun_user
        form.instance.sobun = sobun

        return super().form_valid(form)

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        pk = self.object.id
        return reverse("app:rate", kwargs={"pk": pk})


class RateDetailView(LoginRequiredMixin, generic.DetailView):
    model = SobunRate
    context_object_name = 'rate'
    template_name = 'app/rate/view.html'
