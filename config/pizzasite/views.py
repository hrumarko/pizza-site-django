import json
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from register.models import MyUser
from .models import Cart, Pizza
# from django.urls import reverse_lazy


def index(request):
    """Return first page woth all pizzas"""
    pizzas = Pizza.objects.all()
    cart = ''
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    ctx = {
            'pizzas': pizzas,
            'cart': cart,
    }
    # request.session['fav_color'] = 'blue'
    print(request.session.session_key)
    print(request.user)
    return render(request, 'pizzasite/base.html', ctx)


def res(request):
    b = request.POST
    j = json.loads(b['order'])
    print(j)
    
    
    # print(b['order'['pizza0']['name']])
    return redirect('home')


def add_case_in_cart(request):
    req = request.POST
    json_req = json.loads(req['cas'])
    price_cart = json_req["price_cart"]
    
    user = request.user
    name = json_req['name']
    radius = json_req['radius']
    dough = json_req['dough']
    count = 1
    price = json_req['price']
    img = json_req['img']
    main_price = json_req['main_price']
    
    Cart.objects.create(
            user=user,
            pizza=name,
            radius=radius,
            dough=dough,
            count=count,
            price=price,
            img=img,
            main_price=main_price
            )
    MyUser.objects.filter(
        email=user
    ).update(cart_price=price_cart)
    return HttpResponse("sccs")


def delete_case_from_cart(request):
    req = request.POST
    json_req = json.loads(req['add_case'])
    
    user = request.user
    pizza = json_req['name']
    radius = json_req['radius']
    dough = json_req['dough']
    
    price_cart = json_req['price_cart']
    
    obj = Cart.objects.filter(
            user=user,
            pizza=pizza,
            radius = radius,
            dough=dough
            ).delete()
    MyUser.objects.filter(
        email=user
    ).update(cart_price=price_cart)
    return HttpResponse("fsdf")
    


def update_case_in_cart(request):
    req = request.POST
    json_req = json.loads(req['add_case'])
    
    user = request.user
    pizza = json_req['name']
    radius = json_req['radius']
    count = int(json_req['count'])
    dough = json_req['dough']
    price = json_req['price']
    price_cart = json_req['price_cart']
    print(price)
    obj = Cart.objects.filter(
            user=user,
            pizza=pizza,
            radius = radius,
            dough=dough
            ).update(count=count, price=price)
    MyUser.objects.filter(
        email=user
    ).update(cart_price=price_cart)
    print(obj)
    return HttpResponse("fsdf")

def made_order(request):
    return render(request, 'pizzasite/makeorder.html')
