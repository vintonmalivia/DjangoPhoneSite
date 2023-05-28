from django import template
from phones.models import *

register = template.Library()


@register.simple_tag()
def get_brands(filter=None):
    if not filter:
        return Brand.objects.all()
    else:
        return Brand.objects.filter(pk=filter)


@register.inclusion_tag('phones/list_brands.html')
def show_brands(sort=None, brand_selected=0):
    if not sort:
        brands = Brand.objects.all()
    else:
        brands = Brand.objects.order_by(sort)
    return {'brands': brands, 'brand_selected': brand_selected}
