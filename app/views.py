from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from StoreBook.decorators import get_ip

from .models import (
    Supplier,
    Buyer,
    # Season,
    # Drop,
    # Product,
    # Order,
    # Delivery
)
from .forms import (
    SupplierForm,
    BuyerForm,
    # SeasonForm,
    # DropForm,
    # ProductForm,
    # OrderForm,
    # DeliveryForm
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
                user = User.objects.get(pk=obj.user.pk)
                user.email      = email
                user.username   = username
                user.save()


                obj.name            = name
                obj.address         = address
                obj.save()
                messages.success(request, 'Supplier Updated Successfully!')
                return redirect('/supplier-list')
    
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
        obj = get_object_or_404(Supplier, id = id)
        forms = BuyerForm(request.POST or None)
    else:
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

    params = {'form': forms}
    return render(request, 'store/buyer.html', params)

@login_required(login_url='login')
def all_buyers(request):
    buyers = Buyer.objects.filter(session_user=request.user)

    params = {'buyers': buyers}
    return render(request, 'store/all_buyers.html', params)