import json
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from register.models import MyUser
from .models import Cart, Pizza, SessionUser, Order
from .forms import DeliveryForm
# from django.urls import reverse_lazy
after_auth = False

def index(request):
    if not request.COOKIES.get('mainsessionid'):
        request.session['user'] = 'anonymous'
        response = redirect('home')
        if request.session.session_key is None:
            return response
        ses_id = request.session.session_key
        SessionUser.objects.create(session_id=ses_id, price='0')
        response.set_cookie('mainsessionid', ses_id, max_age=None)
        return response
    if after_auth:
        return merge_session_and_user_cart(request)
    # form delivery
    delivery_form = DeliveryForm()
    # form 
    mainsessionid = request.COOKIES.get('mainsessionid')
    ses_user = SessionUser.objects.get(session_id=mainsessionid)
    pizzas = Pizza.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    else:
        cart = Cart.objects.filter(session_id=mainsessionid)
    ctx = {
            'pizzas': pizzas,
            'cart': cart,
            'ses_user': ses_user,
            'delivery_form': delivery_form,
    }
    return render(request, 'pizzasite/base.html', ctx)



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
    ses_id = request.COOKIES.get('mainsessionid')
    
    if request.user.is_authenticated:
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
    else:
        print("hello u r aninymous")
        Cart.objects.create(
                session_id=ses_id,
                pizza=name,
                radius=radius,
                dough=dough,
                count=count,
                price=price,
                img=img,
                main_price=main_price
                )
        SessionUser.objects.filter(session_id=ses_id).update(
                price=price_cart
                )
    return HttpResponse("sccs")


def delete_case_from_cart(request):
    req = request.POST
    json_req = json.loads(req['add_case'])
    
    ses_id = request.COOKIES.get('mainsessionid')
    user = request.user
    pizza = json_req['name']
    radius = json_req['radius']
    dough = json_req['dough']
    price_cart = json_req['price_cart']
    
    if request.user.is_authenticated:
        obj = Cart.objects.filter(
                user=user,
                pizza=pizza,
                radius = radius,
                dough=dough
                ).delete()
        MyUser.objects.filter(
            email=user
        ).update(cart_price=price_cart)
    else:
        obj = Cart.objects.filter(
                session_id=ses_id,
                pizza=pizza,
                radius = radius,
                dough=dough
                ).delete()
        SessionUser.objects.filter(
            session_id=ses_id
        ).update(price=price_cart)
    return HttpResponse("fsdf")
    


def update_case_in_cart(request):
    req = request.POST
    json_req = json.loads(req['add_case'])
    
    ses_id = request.COOKIES.get('mainsessionid')
    user = request.user
    pizza = json_req['name']
    radius = json_req['radius']
    count = int(json_req['count'])
    dough = json_req['dough']
    price = json_req['price']
    price_cart = json_req['price_cart']
    print(price_cart)
    if request.user.is_authenticated:
        obj = Cart.objects.filter(
                user=user,
                pizza=pizza,
                radius = radius,
                dough=dough
                ).update(count=count, price=price)
        MyUser.objects.filter(
            email=user
        ).update(cart_price=price_cart)
    else:
        obj = Cart.objects.filter(
                session_id=ses_id,
                pizza=pizza,
                radius = radius,
                dough=dough
                ).update(count=count, price=price)
        SessionUser.objects.filter(
            session_id=ses_id
        ).update(price=price_cart)
        print(ses_id)
    return HttpResponse("fsdf")

def merge_session_and_user_cart(request):
    global after_auth
    after_auth = False
    # add sum of main amounts
    
    ses_id = request.COOKIES.get('mainsessionid')
    ses_user = SessionUser.objects.get(session_id=ses_id)
    user = MyUser.objects.get(email=request.user)
    ses_price = int( ses_user.price.split(" ")[0] )
    user_price = int( user.cart_price.split(" ")[0] )
    result_price = str( ses_price + user_price ) + " ₴"
    user.cart_price = result_price
    ses_user.price = "0"
    ses_user.save()
    user.save()
    sessions_pizza = Cart.objects.filter(session_id=ses_id)
    for s in sessions_pizza:
        
        cart = Cart.objects.filter(
            user=request.user,
            pizza=s.pizza,
            dough=s.dough,
            radius=s.radius).values('count', 'price')
        if cart:
            user_count = cart[0]["count"] 
            user_price = int( cart[0]["price"].split(" ")[0] )
            session_count = s.count
            session_price = int(s.price.split(" ")[0])
            result_count = user_count + session_count
            result_price = user_price + session_price
            cart.update(
                    count=result_count,
                    price=str(result_price) + " ₴"
                    )
            s.delete()
        else:
            Cart.objects.create(
                    user=request.user,
                    pizza=s.pizza,
                    radius=s.radius,
                    dough=s.dough,
                    count=s.count,
                    price=s.price,
                    img=s.img,
                    main_price=s.main_price
                   )
            s.delete()
    response = redirect('home')
    return response
    

def made_order(request):
    order = json.loads(request.POST['order'])
    delivery = json.loads(request.POST['json_delivery'])
    if request.user.is_authenticated:
        Order.objects.create(
                order=order,
                price =delivery['main_price'],
                name=delivery['name'],
                number=delivery['number'],
                commentary=delivery['commentary'],
                user=request.user
                )
    else:
        Order.objects.create(
                order=order,
                price =delivery['main_price'],
                name=delivery['name'],
                number=delivery['number'],
                commentary=delivery['commentary'],
                )
    return redirect('/hello/')


def result_order(request):
    orders = Order.objects.all().values('order')
    result = orders[0]['order'].values()
    list_result = list(result)
    result = list(result)[:-1]
    price = list_result[len(list_result)-1]
    print(price)
    ctx = {
            'orders': result,
            'price': price,
            }
    return render(request, 'pizzasite/makeorder.html', ctx)


def orders(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = Order.objects.get(pk=order_id)
        order.is_finished = True
        order.save()
    print(request.user)
    if not request.user.is_authenticated:
        return HttpResponse("У вас недостаточно прав")
    elif request.user.is_admin:
        orders = Order.objects.filter(is_finished=False).values().order_by('-date')
        print(orders)
        ctx = {
                'orders': orders,
                }
        return render(request, 'pizzasite/makeorder.html', ctx)
    else:
        return HttpResponse("У вас недостаточно прав")










