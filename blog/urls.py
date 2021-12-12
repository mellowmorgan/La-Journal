from . import views
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostUserListView
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', PostListView.as_view(), name = "site-home"),
	path('about/', views.about, name ='site-about'),
	path('help/', views.contactView, name ='site-help'),
	path('success/', views.successView, name ='success'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('blog/<str:username>/', PostUserListView.as_view(), name='user-blog'),
	path('explore/', views.explore, name='explore-page'),
	path('search-results/', views.SearchResults, name='search-results'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

