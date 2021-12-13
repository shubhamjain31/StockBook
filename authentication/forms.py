from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

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

    mobile = forms.IntegerField(error_messages={
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
        fields = ('username', 'mobile', 'email', 'password1', 'password2')

    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")
        if mobile < 0:
            raise forms.ValidationError("Mobile Number must Contain Numbers")

        if len(str(mobile)) > 10:
            raise forms.ValidationError("Mobile Number Should Not Be More Than 10 Characters (It has "+str(len(str(mobile)))+")")
        return mobile