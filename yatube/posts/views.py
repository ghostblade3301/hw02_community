from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    title = 'Главная страница'
    template = 'posts/index.html'
    posts = (Post.objects.all()[:settings.POSTS_PER_PAGE])
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all()[:settings.POSTS_PER_PAGE]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
