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


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_brand(request, brand_id):
    posts = Phone.objects.filter(brand_id=brand_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по брэндам',
        'brand_selected': brand_id
    }
    return render(request, 'phones/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')

