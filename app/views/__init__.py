import common.views as commonViews

from .post import PostListView, PostDetailView, PostCreateView, PostHistoryListView
from .request import RequestListView, PostRequestListView, RequestCreateView, RequestDetailView, RequestUpdateView
from .rate import RateCreateView, RateDetailView, RateListView, RateUserListView

from .temp import temp_request_chat_complete, temp_request_chat_create

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return PostListView.as_view()(request)
    return commonViews.IndexView.as_view()(request)

