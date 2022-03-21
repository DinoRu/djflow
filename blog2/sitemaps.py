from django.contrib.sitemaps import Sitemap
from blog2.models import Post

class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
