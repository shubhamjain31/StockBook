from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from StoreBook.decorators import get_ip

from .models import (
    Supplier,
    # Buyer,
    # Season,
    # Drop,
    # Product,
    # Order,
    # Delivery
)
from .forms import (
    SupplierForm,
    # BuyerForm,
    # SeasonForm,
    # DropForm,
    # ProductForm,
    # OrderForm,
    # DeliveryForm
)

# Create your views here.


def index(request):
	return render(request, "index.html")

@login_required(login_url='login')
def suppliers(request):
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

            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_supplier=True
                )
                Supplier.objects.create(user=user, name=name, address=address, ip_address=get_ip(request))
                # return redirect('supplier-list')
    
    params = {'form': forms}
    return render(request, 'store/supplier.html', params)