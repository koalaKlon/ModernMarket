from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

menu = ["sfd", "fsd", "fsdf"]


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    print(f"Received ID: {id}, Slug: {slug}")
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    print(f"Product found: {product}")
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product/detail.html', {'product': product,
                                                         'cart_product_form': cart_product_form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('store:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = AuthenticationForm()
    return render(request=request, template_name="store/login.html", context={"login_form": login_form})


def register_request(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('store:home')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            form = UserRegistrationForm()
            return render(request=request, template_name="store/register.html", context={"register_form": form})
    form = UserRegistrationForm()
    return render(request=request, template_name="store/register.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out. ")
    return redirect("store:home")
