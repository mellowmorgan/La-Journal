from . import views
from .views import MultipleModelView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostUserListView
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', MultipleModelView.as_view(), name = "site-home"),
	path('about/', views.about, name ='site-about'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('blog/<str:username>/', PostUserListView.as_view(), name='user-blog'),
	path('explore/', views.explore, name = 'explore-page'),
]

