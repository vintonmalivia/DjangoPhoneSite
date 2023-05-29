from django.http import *
from django.shortcuts import *
from phones.models import *

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Phone.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'brand_selected': 0
    }
    return render(request, 'phones/index.html', context=context)


def about(request):
    return render(request, 'phones/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def login(request):
    return HttpResponse('Авторизация')


def contact(request):
    return HttpResponse('Обратная связь')


def show_post(request, post_slug):
    post = get_object_or_404(Phone, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'brand_selected': post.brand.slug
    }
    return render(request, 'phones/post.html', context=context)


def show_brand(request, brand_slug):
    posts = Phone.objects.filter(brand__slug=brand_slug)

    if len(posts) == 0 and not Brand.objects.filter(slug=brand_slug).exists():
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по брэндам',
        'brand_selected': brand_slug
    }
    return render(request, 'phones/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')

