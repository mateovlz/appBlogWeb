from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from apps.blog.views import BlogList , BlogDetail, BlogCreate
urlpatterns = [
    path('', login_required(views.post_list), name='post_list'),
    path('post/<int:pk>/', login_required(views.post_detail), name='post_detail'),
    path('post/new', login_required(views.post_new), name='post_new'),
    path('blog/new', login_required(BlogCreate.as_view()), name='blog_form'),
    path('post/<int:pk>/edit', login_required(views.post_edit), name='post_edit'),
    path('post/blogs', login_required(BlogList.as_view()), name='blog_list'),
    path('post/blogs/<slug:slug>/', login_required(BlogDetail.as_view()), name='blog_detail'),

]
