from django.urls import path
from .views import blog_index, blog_detail, blog_category, reply

app_name = 'blog'

urlpatterns = [
    path('', blog_index, name='index'),
    path('<int:pk>/', blog_detail, name='detail'),
    path('<category>/', blog_category, name='category'),
    path('tag/<slug:tag_slug>/', blog_index, name='post_tag'), 
    path('comment/reply/', reply, name='comment_reply'),
]