from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class"       : "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class"       : "form-control"
            }
        ))

    phone = forms.IntegerField(error_messages={
        'required'            : 'Please Enter Mobile Number'
    },
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Mobile Number",                
                "class"       : "form-control",
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Enter Password",                
                "class"       : "form-control",
                "autocomplete":"on"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Re Enter Password",                
                "class"       : "form-control",
                "autocomplete":"on"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_phone(self, *args, **kwargs):
        phone = self.cleaned_data.get("phone")
        if phone < 0:
            raise forms.ValidationError("Phone Number must Contain Numbers")

        if len(str(phone)) > 10:
            raise forms.ValidationError("Phone Number Should Not Be More Than 10 Characters (It has "+str(len(str(phone)))+")")
        return phone