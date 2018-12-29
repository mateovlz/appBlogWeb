from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(views.post_list), name='post_list'),
    path('post/<int:pk>/', login_required(views.post_detail), name='post_detail'),
    path('post/new', login_required(views.post_new), name='post_new'),
    path('post/<int:pk>/edit', login_required(views.post_edit), name='post_edit'),

]
