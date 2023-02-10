from ..models import Sobun, SobunPost, SobunStatus
from chat.models import ChatRoom, Topic
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseBadRequest


#FIXME: THIS IS CURSED
def temp_request_chat_create(request, sobun_id):

    post = SobunPost.objects.get(id=sobun_id)
    if request.user == post.user and not request.user.is_superuser:
        return HttpResponseBadRequest("Can't request to the same user.")

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


def temp_request_chat_complete(request, sobun_id, chat_id):
    req = get_object_or_404(Sobun, pk=sobun_id)
    if not (
            (req.post is not None and req.post.user == request.user) 
            or req.user == request.user
        ):
        return HttpResponseForbidden("Not allowed")

    req.status = SobunStatus.COMPLETE
    req.save()
    return redirect(reverse('app:rate_create', kwargs={"sobun_id": sobun_id}) + f'?next={reverse("chat:room", kwargs={"pk": chat_id})}')