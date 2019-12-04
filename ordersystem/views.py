# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import InventoryItem, Category, CustomerAccount, Order
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('../')


def ordering_page(request):
    items = InventoryItem.objects.all()
    categories = Category.objects.all()
    return render(request, 'ordering_page.html', {'items': items, 'categories': categories})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('../thankyou')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed.')
            return redirect('change_password')
        else:
            messages.error(request, 'Error in input, please fix')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


@login_required()
def change_settings(request):
    return render(request, 'registration/settings.html')


def thankyou(request):
    return render(request, 'thankyou.html', {})


def admin_page(request):
    users = CustomerAccount.objects.all()
    return render(request, 'admin.html', {"data": users})


def favorites(request):
    return render(request, 'favorites.html',{})


def recent_orders(request):
    orders = Order.objects.all()
    items = InventoryItem.objects.all()
    return render(request, 'recent_orders.html', {"orders": orders, "items": items})


def view_cart(request):
    cart = CustomerAccount.cart
    return render(request, 'view_cart.html', {"cart": cart})


class InventoryView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_items = InventoryItem.objects.all()

        context["menu_items"] = all_items
        context["test"] = "test"

        return context
