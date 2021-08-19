from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostUserListView
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name = "site-home"),
	path('about/', views.about, name ='site-about'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('blog/<str:username>/', PostUserListView.as_view(), name="user-blog"),
	#re_path(r'^blog/(?P<username>[\w.@+-]+)/$', PostUserListView.as_view(), name="user-blog"),
]

