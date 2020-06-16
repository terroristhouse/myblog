from django.shortcuts import render, HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def hello(request):
    return HttpResponse('欢迎使用Django!')


# 首页
def index(request):
    allarticle = Article.objects.all().order_by('-id')[0:10]
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[0:3]
    hot = Article.objects.all().order_by('-views')[0:10]
    link = Link.objects.all()
    return render(request, 'index.html', locals())


# 列表页
def list(request, lid):
    list = Article.objects.filter(category__id=lid)
    cname = Category.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('-views')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__contains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)

    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())

# 公共部分提取
def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui_id=2)[:6]
    tags = Tag.objects.all()
    return locals()
