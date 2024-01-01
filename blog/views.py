from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import SiteSetting, About, Resume, Post, Tag


# Create your views here.
def index(request, page=1):
    p = Paginator(Post.objects.filter(star=True), 10)
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "project",
            "shown_title": "Home | Lynn Wang",
        },
        "paginator": p.page(page),
        "current": page,
        "total": p.num_pages,
        "showHeader": True,
    }
    return render(request, 'blog-post.html', context=context)


def about(request):
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "about",
            "shown_title": "About | Lynn Wang",
        },
        "content": About.objects.get(enable=True).text,
        "showHeader": False,
    }
    return render(request, 'page.html', context=context)


def resume(request):
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "resume",
            "shown_title": "Resume | Lynn Wang",
        },
        "content": Resume.objects.get(enable=True),
        "showHeader": True,
    }
    return render(request, 'resume.html', context=context)


def blogs(request, page=1):
    p = Paginator(Post.objects.filter(category=0), 10)
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "blog",
            "shown_title": "Blogs | Lynn Wang",
        },
        "paginator": p.page(page),
        "current": page,
        "total": p.num_pages,
        "showHeader": True,
    }
    return render(request, 'blog-post.html', context=context)


def projects(request, page=1):
    p = Paginator(Post.objects.filter(category=1), 10)
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "project",
            "shown_title": "Projects | Lynn Wang",
        },
        "paginator": p.page(page),
        "current": page,
        "total": p.num_pages,
        "showHeader": True,
    }
    return render(request, 'blog-post.html', context=context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": post.title,
            "shown_title": f"Projects | {post.title}",
            "date": post.time,
            "tags": post.tags,
            "title_image": post.title_image,
        },
        "content": post.content,
        "words": post.content,
        "showHeader": False,
    }
    return render(request, 'post.html', context=context)


def post_name(request, name):
    post = Post.objects.get(title=str.replace(name, "-", " "))
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": post.title,
            "shown_title": f"Projects | {post.title}",
            "date": post.time,
            "tags": post.tags,
            "title_image": post.title_image,
        },
        "content": post.content,
        "words": post.content,
        "showHeader": False,
    }
    return render(request, 'post.html', context=context)


def tags(request, tag="", page=1):
    tag = Tag.objects.get(tag=tag)
    p = Paginator(tag.post_set.all(), 10)
    context = {
        "site": SiteSetting.objects.get(enable=True),
        "page": {
            "title": "project",
            "shown_title": "Projects | Lynn Wang",
        },
        "paginator": p.page(page),
        "current": page,
        "total": p.num_pages,
        "showHeader": True,
    }
    return render(request, 'blog-post.html', context=context)
