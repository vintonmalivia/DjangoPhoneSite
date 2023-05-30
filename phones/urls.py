from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PhoneHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('brand/<slug:brand_slug>/', PhoneBrand.as_view(), name='brand')
]
