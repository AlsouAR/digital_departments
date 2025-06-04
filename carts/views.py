from django.shortcuts import redirect, render

from goods.models import Products
from carts.models import Cart

def cart_user(request):
    return render(request, 'carts/cart.html')

def cart_checkout(request):
    return render(request, 'carts/checkout.html')

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product).first()
    else:
        session_key = request.session.session_key
        cart = Cart.objects.filter(session_key=session_key, product=product).first()

    if cart:
        action = request.GET.get('action', 'add')  # По умолчанию добавляем

        if action == 'add':
            cart.quantity += 1
        elif action == 'subtract':
            cart.quantity -= 1
            if cart.quantity < 1:
                cart.delete()  # Удаляем товар из корзины, если количество меньше 1
                return redirect(request.META.get('HTTP_REFERER', 'carts:cart_user'))

        cart.save()

    return redirect(request.META.get('HTTP_REFERER', 'carts:cart_user'))

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    return redirect(request.META['HTTP_REFERER'])
