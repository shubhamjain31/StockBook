import email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from StoreBook.decorators import get_ip
from validators import is_invalid

from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)

User = get_user_model()

# Create your views here.

@login_required(login_url='login')
def index(request):
	return render(request, "index.html")

@login_required(login_url='login')
def supplier(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Supplier, id = id)
        forms = SupplierForm(initial={'name': obj.name, 'address': obj.address, 'email':obj.user.email, 'username':obj.user.username})
    else:
        obj = ''
        forms = SupplierForm()

    if request.method == 'POST':
        forms = SupplierForm(request.POST)

        if forms.is_valid():
            name 			= forms.cleaned_data['name']
            address 		= forms.cleaned_data['address']
            email 			= forms.cleaned_data['email']
            username 		= forms.cleaned_data['username']
            password 		= forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']

            if not obj:
                if password == retype_password:
                    user = User.objects.create_user(
                        username=username, password=password,
                        email=email, is_supplier=True
                    )
                    Supplier.objects.create(user=user, name=name, address=address, ip_address=get_ip(request), session_user=request.user)

                    messages.success(request, 'Supplier Added Successfully!')
                    return redirect('/supplier-list')
                else:
                    messages.error(request, 'Password Do Not Match!')
            else:
                if password == retype_password:
                    user = User.objects.get(pk=obj.user.pk)
                    user.email      = email
                    user.username   = username
                    user.save()


                    obj.name            = name
                    obj.address         = address
                    obj.save()
                    messages.success(request, 'Supplier Updated Successfully!')
                    return redirect('/supplier-list')
                else:
                    messages.error(request, 'Please Enter Valid Password Before Updating Your Data!')
                    return redirect(last)
        else:
            print(forms.errors)
    
    params = {'form': forms, 'obj':obj}
    return render(request, 'store/supplier.html', params)

@login_required(login_url='login')
def all_suppliers(request):
    suppliers = Supplier.objects.filter(session_user=request.user)

    params = {'suppliers': suppliers}
    return render(request, 'store/all_suppliers.html', params)

@login_required(login_url='login')
def delete_supplier(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Supplier.objects.get(pk=id)
        user_obj = User.objects.get(pk=obj.user.pk)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    user_obj.delete()
    obj.delete()

    messages.success(request, 'Supplier Deleted Successfully')
    return redirect('/supplier-list/')

@login_required(login_url='login')
def buyer(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Buyer, id = id)
        forms = BuyerForm(initial={'name': obj.name, 'address': obj.address, 'email':obj.user.email, 'username':obj.user.username})
    else:
        obj = ''
        forms = BuyerForm()

    if request.method == 'POST':
        forms = BuyerForm(request.POST)

        if forms.is_valid():
            name            = forms.cleaned_data['name']
            address         = forms.cleaned_data['address']
            email           = forms.cleaned_data['email']
            username        = forms.cleaned_data['username']
            password        = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']

            if not obj:
                if password == retype_password:
                    user = User.objects.create_user(
                        username=username, password=password,
                        email=email, is_buyer=True
                    )
                    Buyer.objects.create(user=user, name=name, address=address, ip_address=get_ip(request), session_user=request.user)

                    messages.success(request, 'Buyer Added Successfully!')
                    return redirect('/buyer-list')
                else:
                    messages.error(request, 'Password Do Not Match!')
            else:
                if password == retype_password:
                    user = User.objects.get(pk=obj.user.pk)
                    user.email      = email
                    user.username   = username
                    user.save()


                    obj.name            = name
                    obj.address         = address
                    obj.save()
                    messages.success(request, 'Buyer Updated Successfully!')
                    return redirect('/buyer-list')
                else:
                    messages.error(request, 'Please Enter Valid Password Before Updating Your Data!')
                    return redirect(last)
        else:
            print(forms.errors)

    params = {'form': forms, 'obj':obj}
    return render(request, 'store/buyer.html', params)

@login_required(login_url='login')
def all_buyers(request):
    buyers = Buyer.objects.filter(session_user=request.user)

    params = {'buyers': buyers}
    return render(request, 'store/all_buyers.html', params)

@login_required(login_url='login')
def delete_buyer(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Buyer.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()

    messages.success(request, 'Buyer Deleted Successfully')
    return redirect('/buyer-list/')

@login_required(login_url='login')
def season(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Season, id = id)
        forms = SeasonForm(request.POST or None, instance = obj)
    else:
        obj = ''
        forms = SeasonForm()

    if request.method == 'POST':
        if not id:
            forms = SeasonForm(request.POST)

        if forms.is_valid():
            name            = forms.cleaned_data['name']
            description     = forms.cleaned_data['description']

            if not obj:
                Season.objects.create(name=name, description=description, ip_address=get_ip(request), session_user=request.user)

                messages.success(request, 'Season Added Successfully!')
                return redirect('/season-list')
            else:
                obj.name                = name
                obj.description         = description
                obj.save()
                messages.success(request, 'Season Updated Successfully!')
                return redirect('/season-list')
        else:
            print(forms.errors)

    params = {'form': forms, 'obj':obj}
    return render(request, 'store/season.html', params)

@login_required(login_url='login')
def all_seasons(request):
    seasons = Season.objects.filter(session_user=request.user)

    params = {'seasons': seasons}
    return render(request, 'store/all_seasons.html', params)

@login_required(login_url='login')
def delete_season(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Season.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()

    messages.success(request, 'Season Deleted Successfully')
    return redirect('/season-list/')

@login_required(login_url='login')
def drop(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Drop, id = id)
        forms = DropForm(request.POST or None, instance = obj)
    else:
        obj = ''
        forms = DropForm()

    if request.method == 'POST':
        if not id:
            forms = DropForm(request.POST)

        if forms.is_valid():
            name            = forms.cleaned_data['name']

            if not obj:
                Drop.objects.create(name=name, ip_address=get_ip(request), session_user=request.user)

                messages.success(request, 'Drop Added Successfully!')
                return redirect('/drop-list')
            else:
                obj.name                = name
                obj.save()
                messages.success(request, 'Drop Updated Successfully!')
                return redirect('/drop-list')
        else:
            print(forms.errors)

    params = {'form': forms, 'obj':obj}
    return render(request, 'store/drop.html', params)

@login_required(login_url='login')
def all_drops(request):
    drops = Drop.objects.filter(session_user=request.user)

    params = {'drops': drops}
    return render(request, 'store/all_drops.html', params)

@login_required(login_url='login')
def delete_drop(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Drop.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()

    messages.success(request, 'Season Deleted Successfully')
    return redirect('/drop-list/')

@login_required(login_url='login')
def product(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Product, id = id)
        forms = ProductForm(request.POST or None, instance = obj)
    else:
        obj = ''
        forms = ProductForm()

    if request.method == 'POST':
        if not id:
            forms = ProductForm(request.POST)

        if forms.is_valid():
            name            = forms.cleaned_data['name']
            sortno          = forms.cleaned_data['sortno']

            if not obj:
                Product.objects.create(name=name, sortno=sortno, ip_address=get_ip(request), session_user=request.user)

                messages.success(request, 'Product Added Successfully!')
                return redirect('/product-list')
            else:
                obj.name                = name
                obj.sortno              = sortno
                obj.save()
                messages.success(request, 'Product Updated Successfully!')
                return redirect('/product-list')
    
    params = {'form': forms, 'obj':obj}
    return render(request, 'store/product.html', params)

@login_required(login_url='login')
def all_products(request):
    products = Product.objects.filter(session_user=request.user)

    params = {'products': products}
    return render(request, 'store/all_products.html', params)

@login_required(login_url='login')
def delete_product(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Product.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()

    messages.success(request, 'Product Deleted Successfully')
    return redirect('/product-list/')

@login_required(login_url='login')
def order(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Order, id = id)
        forms = OrderForm(request.POST or None, instance = obj)
    else:
        obj = ''
        forms = OrderForm()

    if request.method == 'POST':
        if not id:
            forms = OrderForm(request.POST)

        if forms.is_valid():
            supplier    = forms.cleaned_data['supplier']
            product     = forms.cleaned_data['product']
            design      = forms.cleaned_data['design']
            color       = forms.cleaned_data['color']
            buyer       = forms.cleaned_data['buyer']
            season      = forms.cleaned_data['season']
            drop        = forms.cleaned_data['drop']

            if not obj:
                Order.objects.create(
                    supplier    = supplier,
                    product     = product,
                    design      = design,
                    color       = color,
                    buyer       = buyer,
                    season      = season,
                    drop        = drop,
                    status      = 'pending',
                    ip_address  = get_ip(request), 
                    session_user = request.user
                )

                messages.success(request, 'Order Added Successfully!')
                return redirect('/order-list')
            else:
                obj.supplier            = supplier
                obj.product             = product
                obj.design              = design
                obj.color               = color
                obj.buyer               = buyer
                obj.season              = season
                obj.drop                = drop
                obj.save()
                messages.success(request, 'Order Updated Successfully!')
                return redirect('/order-list')
    
    params = {'form': forms, 'obj':obj}
    return render(request, 'store/order.html', params)

@login_required(login_url='login')
def all_orders(request):
    orders = Order.objects.filter(session_user=request.user)

    params = {'orders': orders}
    return render(request, 'store/all_orders.html', params)

@login_required(login_url='login')
def delete_order(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Order.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()

    messages.success(request, 'Order Deleted Successfully')
    return redirect('/order-list/')

@login_required(login_url='login')
def all_deliveries(request):
    deliveries = Delivery.objects.filter(session_user=request.user)

    params = {'deliveries': deliveries}
    return render(request, 'store/all_deliveries.html', params)

@login_required(login_url='login')
def delivery(request, id=None):
    last = request.META.get('HTTP_REFERER', None)

    if id:
        obj = get_object_or_404(Delivery, id = id)
        forms = DeliveryForm(request.POST or None, instance = obj)
    else:
        obj = ''
        forms = DeliveryForm()

    if request.method == 'POST':
        if not id:
            forms = DeliveryForm(request.POST)

        if forms.is_valid():
            order            = forms.cleaned_data['order']
            courier_name     = forms.cleaned_data['courier_name']

            if not obj:
                Delivery.objects.create(
                    order            = order,
                    courier_name     = courier_name,
                    ip_address       = get_ip(request), 
                    session_user     = request.user
                )

                messages.success(request, 'Delivery Added Successfully!')
                return redirect('/delivery-list')
            else:
                obj.order.pk         = order.pk,
                obj.courier_name     = courier_name
                obj.save()
                messages.success(request, 'Delivery Updated Successfully!')
                return redirect('/delivery-list')
        else:
            messages.error(request, 'Something Went Wrong!')
    
    params = {'form': forms, 'obj':obj}
    return render(request, 'store/delivery.html', params)

@login_required(login_url='login')
def delete_delivery(request, id):
    last = request.META.get('HTTP_REFERER', None)
    
    try:
        obj      = Delivery.objects.get(pk=id)
    except:
        messages.error(request, 'Something Went Wrong!')
        return redirect(last)

    obj.delete()
    messages.success(request, 'Delivery Deleted Successfully')
    return redirect('/delivery-list/')

def user_settings(request):
    last = request.META.get('HTTP_REFERER', None)

    obj = User.objects.get(username=request.user)

    if request.method == 'POST':
        fullname    = request.POST.get('full_name')
        firstname   = request.POST.get('first_name')
        lastname    = request.POST.get('last_name')
        mobile      = request.POST.get('mobile')

        if fullname is None:
            messages.error(request, "Enter Valid Full Name")
            return redirect(last)

        if is_invalid(fullname):
            messages.error(request, "Enter Valid Full Name")
            return redirect(last)

        if firstname is None:
            messages.error(request, "Enter Valid First Name")
            return redirect(last)

        if is_invalid(firstname):
            messages.error(request, "Enter Valid First Name")
            return redirect(last)

        if lastname is None:
            messages.error(request, "Enter Valid Last Name")
            return redirect(last)

        if is_invalid(lastname):
            messages.error(request, "Enter Valid Last Name")
            return redirect(last)

        if mobile is None:
            messages.error(request, "Enter Valid Mobile")
            return redirect(last)

        if is_invalid(mobile):
            messages.error(request, "Enter Valid Mobile")
            return redirect(last)

        obj.fullname    = fullname
        obj.first_name  = firstname
        obj.last_name   = lastname
        obj.mobile      = mobile
        obj.save()
        messages.success(request, 'Settings Updated!')

    params = {'user_obj': obj}
    return render(request, 'settings.html', params)

@login_required(login_url='login')
def upgrade(request):
    return render(request, 'store/upgrade.html')