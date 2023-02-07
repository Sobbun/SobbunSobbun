import common.views as commonViews

from .post import PostListView, PostDetailView, PostCreateView
from .request import RequestListView, PostRequestListView, RequestCreateView, RequestDetailView, RequestUpdateView

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return PostListView.as_view()(request)
    return commonViews.index(request)


