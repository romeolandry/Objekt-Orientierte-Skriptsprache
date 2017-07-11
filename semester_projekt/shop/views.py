from django import forms
from django.shortcuts import render, get_object_or_404

from shop.recommender import Recommender
from .models import Category, Product
from .form import DetailProduct
from django.views.generic.detail import DetailView

# Create your views here.

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404 (Category, slug=category_slug)
        products =products.filter(category = category)

    context ={'category':category, 'categories':categories, 'products':products}
    template = 'home.html'
    return render(request,template,context )


# class ProductFDetailview(DetailView):
#     model = Product
#
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    form = DetailProduct
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    context ={'product':product, 'form':form, 'recommended_products':recommended_products }
    template = 'products_detail.html'
    return  render(request, template, context)