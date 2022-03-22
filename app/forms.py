from django import forms

from .models import Season, Drop, Product, Order, Delivery

class SupplierForm(forms.Form):
    name = forms.CharField(error_messages={
        'required'              : 'Please Enter Name',
    },
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
        'placeholder': "Enter Name"
    }))
    address = forms.CharField(error_messages={
        'required'              : 'Please Enter Address',
        },
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
        'placeholder': "Enter Address"
    }))
    email = forms.CharField(error_messages={
        'required'              : 'Please Enter Email',
        },
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
        'placeholder': "Enter Email"
    }))
    username = forms.CharField(error_messages={
        'required'              : 'Please Enter UserName',
        },
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
        'placeholder': "Enter UserName"
    }))
    password = forms.CharField(error_messages={
        'required'              : 'Please Enter Password',
        },
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
        'placeholder': "Enter Password"
    }))
    retype_password = forms.CharField(error_messages={
        'required'              : 'Please Enter Re-Password',
        },
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
        'placeholder': "Enter Re-Password"
    }))


class BuyerForm(forms.Form):
    name = forms.CharField(error_messages={
        'required'              : 'Please Enter Name',
    },
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
        'placeholder': "Enter Name"
    }))
    address = forms.CharField(error_messages={
        'required'              : 'Please Enter Address',
        },
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
        'placeholder': "Enter Address"
    }))
    email = forms.CharField(error_messages={
        'required'              : 'Please Enter Email',
        },
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
        'placeholder': "Enter Email"
    }))
    username = forms.CharField(error_messages={
        'required'              : 'Please Enter UserName',
        },
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
        'placeholder': "Enter Username"
    }))
    password = forms.CharField(error_messages={
        'required'              : 'Please Enter Password',
        },
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
        'placeholder': "Enter Password"
    }))
    retype_password = forms.CharField(error_messages={
        'required'              : 'Please Enter Re-Password',
        },
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
        'placeholder': "Enter Re-Password"
    }))

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name', 'placeholder': "Enter Name"
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description', 'placeholder': "Enter Description"
            })
        }

class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name', 'placeholder': "Enter Name"
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name', 'placeholder': "Enter Name"
            }),
            'sortno': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sortno', 'placeholder': "Enter Sortno"
            })
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop'
        ]

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'design': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'design', 'placeholder': "Enter Design"
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'color', 'placeholder': "Enter Color"
            }),
            'buyer': forms.Select(attrs={
                'class': 'form-control', 'id': 'buyer'
            }),
            'season': forms.Select(attrs={
                'class': 'form-control', 'id': 'season'
            }),
            'drop': forms.Select(attrs={
                'class': 'form-control', 'id': 'drop'
            }),
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['order', 'courier_name']

        widgets = {
            'order': forms.Select(attrs={
                'class': 'form-control', 'id': 'order'
            }),
            'courier_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'courier_name'
            }),
        }