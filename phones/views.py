from django.http import *
from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from phones.forms import *
from phones.models import *
from phones.utils import *

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class PhoneHome(DataMixin, ListView):
    model = Phone
    context_object_name = 'posts'
    template_name = 'phones/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Phone.objects.filter(is_published=True)


# def index(request):
#     posts = Phone.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'brand_selected': 0
#     }
#     return render(request, 'phones/index.html', context=context)


def about(request):
    return render(request, 'phones/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#         'form': form
#     }
#     return render(request, 'phones/addpage.html', context=context)

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'phones/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить пост')
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('Авторизация')


def contact(request):
    return HttpResponse('Обратная связь')


# def show_post(request, post_slug):
#     post = get_object_or_404(Phone, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'brand_selected': post.brand.slug
#     }
#     return render(request, 'phones/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Phone
    template_name = 'phones/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].title,
                                      brand_selected=context['post'].brand.slug)
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Phone.objects.filter(is_published=True)


# def show_brand(request, brand_slug):
#     posts = Phone.objects.filter(brand__slug=brand_slug)
#
#     if len(posts) == 0 and not Brand.objects.filter(slug=brand_slug).exists():
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по брэндам',
#         'brand_selected': brand_slug
#     }
#     return render(request, 'phones/index.html', context=context)


class PhoneBrand(DataMixin, ListView):
    model = Phone
    template_name = 'phones/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Брэнд ' + context['posts'][0].brand.name,
                                      brand_selected=self.kwargs['brand_slug'])
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Phone.objects.filter(brand__slug=self.kwargs['brand_slug'], is_published=True)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
