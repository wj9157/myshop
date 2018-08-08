from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from shop.forms import SignUpForm
from django.contrib.auth.decorators import login_required


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                  'categories': categories, 'products': products})


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                slug=slug,
                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                'shop/product/detail.html',
                {'product': product,
                'cart_product_form': cart_product_form})

class information_veiw(TemplateView):
    template_name = "information.html"
@login_required
def shop(request):
    return render(request, 'shop')
# deffining the sign up specs
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('shop')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

