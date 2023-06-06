from django.core.cache import cache
from django.db.models import Count

from phones.models import Brand

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:

    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        brands = cache.get('brands')
        if not brands:
            brands = Brand.objects.annotate(Count('phone'))
            cache.set('brands', brands, 60)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['brands'] = brands
        if 'brand_selected' not in context:
            context['brand_selected'] = 0
        return context
