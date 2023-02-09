import common.views as commonViews

from .post import PostListView, PostDetailView, PostCreateView
from .request import RequestListView, PostRequestListView, RequestCreateView, RequestDetailView, RequestUpdateView
from .rate import RateCreateView, RateDetailView, RateListView, RateUserListView

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return PostListView.as_view()(request)
    return commonViews.IndexView.as_view()(request)

#FIXME: THIS IS CURSED
def temp_request_chat_create(request, sobun_id):
    from ..models import Sobun, SobunPost, SobunStatus
    from chat.models import ChatRoom, Topic
    from django.utils import timezone
    from django.shortcuts import redirect

    post = SobunPost.objects.get(id=sobun_id)
    req, req_created = Sobun.objects.get_or_create(post=post, user=request.user, defaults={'post': post, 'user': request.user, 'time': timezone.now(), 'status':SobunStatus.REQUESTED})
    if req_created:
        req.save()
    
    room, room_created = ChatRoom.objects.get_or_create(
        participants__in=[request.user, post.user], topic_type=Topic.APP_SOBUN_REQUEST, topic_id=req.pk, 
        defaults={ 
            'topic_type': Topic.APP_SOBUN_REQUEST,
            'topic_id': req.pk,
            'topic_text': ''})
    if room_created:
        room.participants.add(request.user)
        room.participants.add(post.user)
        room.save()

    return redirect('chat:room', pk=room.pk )
