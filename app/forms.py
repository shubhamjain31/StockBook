from django import forms

from .models import Season, Drop

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