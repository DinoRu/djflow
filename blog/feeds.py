from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from blog.models import Article


class LatestArticlesFeed(Feed):
    title = 'Blog'
    description = 'My blog article'
    link = reverse_lazy('blog:index')

    def items(self):
        return Article.objects.all()[:2]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
