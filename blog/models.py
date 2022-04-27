
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, related_name='post',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='feature_img/%Y/%m/%d', null=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self', related_name='parents', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title + ' ' + self.author

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
