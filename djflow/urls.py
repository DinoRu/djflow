from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.urls import path, include
from blog2 import views
from blog2.sitemaps import PostSitemap
from blog.sitemaps import ArticleSitemap


sitemaps = {
    'posts': PostSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('djflow/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('blog2/', include('blog2.urls', namespace='blog2')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
