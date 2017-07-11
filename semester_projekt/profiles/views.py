from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from shop.models import Category, Product

# Create your views here.
def home (request,category_slug =None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products}
    template = 'home.html'
    return render(request,template,context)

def about (request):
    context = {}
    template = 'about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template='profile.html'
    return render(request, template,context)