"""semester_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from shop import views as shop_views
from cart import views as cart_views
from coupons import views as coupons_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),

#     shop
    url(r'^shop/$', shop_views.product_list, name='product_list'),
    url(r'^(?P<categogy_slug>[-\w]+)/$', shop_views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', shop_views.product_detail, name='product_detail'),


    # cart

    url(r'^shop/cart/$', cart_views.cart_detail, name='cart_detail'),
    url(r'^shop/cart/add/(?P<id>\d+)/$', cart_views.cart_add, name='cart_add'),
    url(r'^shop/cart/remove/(?P<id>\d+)/$', cart_views.cart_remove, name='cart_remove'),

    #coupons
    url(r'^apply/$', coupons_views.coupon_apply, name='apply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)