from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import AdForm
from blog.models import Category, Post, Author, CustomUser, Comments, Ad


def index(request):
    categories = Category.objects.all()
    cat_list = []
    for c in categories:
        post = Post.objects.filter(category_id=c.id)
        if post:
            cat_list.append(c.id)
    cat = categories.filter(id__in=cat_list)
    authors = Author.objects.all()
    users = CustomUser.objects.all()

    params = {'categories': cat,
              'authors': authors,
              'users': users}
    return render(request, 'index.html', params)


def category(request, pk):
    posts = Post.objects.filter(category_id=pk)
    return render(request, 'category.html', locals())


def author(request, pk):
    posts = Post.objects.filter(author_id=pk)
    params = {'posts': posts}
    return render(request, 'posts_by_author.html', locals())

def comments(request, pk):
    categories = Category.objects.all()
    cat_list = []
    for c in categories:
        post = Post.objects.filter(category_id=c.id)
        if post:
            cat_list.append(c.id)
    cat = categories.filter(id__in=cat_list)
    authors = Author.objects.all()
    users = CustomUser.objects.all()
    _comments = Comments.objects.filter(user_id=pk)
    return render(request, 'comments.html', locals())

def create_ad(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                Ad.objects.create(title=cd['title'], description=cd['description'], image=cd['image'], user=request.user)
                return HttpResponse('Ad успешно создан!')
        else:
            form = AdForm()
    else:
        return HttpResponse('Вы не авторизованы')
    return render(request, 'ad.html', {'form': form})