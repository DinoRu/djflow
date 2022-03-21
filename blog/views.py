from multiprocessing import context
from operator import ne
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from .models import Article, Category, Comment
from taggit.models import Tag
from .forms import CommentForm

def blog_index(request, tag_slug=None):
    posts = Article.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    query = request.GET.get('q')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    if query:
        posts = Article.objects.filter(Q(title__icontains=query) | Q(categories__name__icontains=query))
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog_index.html', context)


def blog_category(request, category):
    posts = Article.objects.filter(categories__name__contains=category
    ).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/blog_category.html', context)


def blog_detail(request, pk):
    post = Article.objects.get(pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
    else:
        form = CommentForm()
    query = request.GET.get('q')
    if query:
        post = Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(categories__name__icontains=query))
    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Article.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags',)[:6]

    context = {
        'comments': comments,
        'post': post,
        'form': form,
        'similar_posts': similar_posts,
    }
    return render(request, 'blog/blog_detail.html', context)

def reply(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            parent_id = request.POST.get('parent')
            post_url = request.POST.get('post_url')

            reply = form.save(commit=False)
            reply.post = Article(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))
    
    return redirect('/')

        