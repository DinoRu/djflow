from django.urls import path
from blog2 import views
from blog2.feeds import LatestPostsFeed

app_name = 'blog2'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('comment/reply/', views.reply_page, name='reply'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_tag'),
    path('about', views.about, name='about'),
]
