from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from .forms import LoginForm, SignUpForm
from .models import PasswordRecovery

from validators import is_invalid
from StoreBook.decorators import get_ip

import random, string
User = get_user_model()


# Create your views here.

def user_login(request):
	forms = LoginForm()
	msg = None

	if request.method == 'POST':
	    forms = LoginForm(request.POST or None)
	    
	    if forms.is_valid():
	        username = forms.cleaned_data['username']
	        password = forms.cleaned_data['password']
	        user = authenticate(username=username, password=password)

	        if user:
	        	login(request, user)
	        	return redirect('index')
	        else:
	        	msg = 'Invalid credentials'
	    else:
	    	msg = 'Error validating the form' 
	params = {'form': forms,  "msg" : msg}
	return render(request, "login.html", params)

def register(request):
	# if request.user.is_authenticated:
	#     return redirect('/index')
	msg     = None
	success = False

	if request.method == "POST":
		form = SignUpForm(request.POST)

		agree 	= request.POST.get("agree")
		phone 	= request.POST.get("phone")

		if agree is None:
		    msg = 'Please Acccept Privacy Policy'
		    return render(request, "register.html", {"form": form, "msg" : msg, "success" : success })
		
		if form.is_valid():
		    result = {'success': True}

		    if result['success']:
		        post = form.save(commit=False)
		        post.save()

		        username 		= form.cleaned_data.get("username")
		        email    		= form.cleaned_data.get("email")
		        raw_password 	= form.cleaned_data.get("password1")
		        user     = authenticate(username=username, password=raw_password)

		        msg      = 'User created.'
		        success  = True

		        register_user_mail(email, raw_password, username)
		        messages.success(request, 'Registration Completed Successfully. Kindly Login to Continue.')
		        return redirect("/login/")

		    else:
		        msg = 'Invalid reCAPTCHA. Please try again.'
		        form = SignUpForm()

		        return render(request, "register.html", {"form": form, "msg" : msg })

		else:
		    print(form.errors)  
	else:
	    form = SignUpForm()

	return render(request, "register.html", {"form": form, "msg" : msg, "success" : success })

def register_user_mail(email, password, username):

	subject  = 'Thank You For Signup'

	body     = '<h2>Your Account Information</h2>,<br><br>\
	    <b>Username:</b> '+username+'<br>\
	    <b>Password:</b> '+password+'<br><br>'

	msg = EmailMessage(subject, body, 'StoreBook', to=[email])
	msg.content_subtype = "html"
	msg.send()


def reset_password(request):
    if request.method == 'POST':
        email         = request.POST.get("email")

        if is_invalid(email):
            messages.error(request, 'Please Enter Correct Email Address')
            return redirect('/password/reset/')
        
        is_user = User.objects.filter(email=email)
        if not is_user.exists():
            messages.error(request, 'Email does not exist !')
            return render(request,'forget_password.html')
        else:
            user = is_user.last().username
            
            url  = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(100))

            reset_url = "http://127.0.0.1:8000/password/reset/" + url

            subject = 'Password Recovery'

            body    = "Hi " + is_user.last().username +",<br><br>\
                We're sending you this email because you requested a password reset. Click on this link to create a new password:<br><br>\
                Password Reset Link: <br><br>" + reset_url + "</a><br><br><br>\
                If you didn't request a password reset you can ignore this email. Your password will not be changed.<br><br>\
                Please feel free to contact us in case of any queries.<br><br>\
                Thanks & Regards,<br>\
                Team<br>"

            msg = EmailMessage(subject, body, 'StoreBook', to=[email])
            msg.content_subtype = "html"
            msg.send()

            PasswordRecovery(username=user, reset_link=url, ip_address=get_ip(request)).save()
            messages.success(request, 'Reset Link Sent to '+email)

            return render(request,'forget_password.html')

    return render(request, 'forget_password.html')

def recover_password(request, val):
    user = PasswordRecovery.objects.filter(reset_link=val)
    if not user.exists():
        messages.error(request, 'Invalid Reset Token')
        return render(request,'forget_password.html')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if is_invalid(password1) or is_invalid(password2):
            messages.error(request, 'Enter Correct Password')
            return render(request,'new_password.html') 

        if len(password1) < 8:
            messages.error(request, 'Password must contain 8 characters')
            return render(request,'new_password.html') 

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request,'new_password.html') 
        
        User.objects.filter(username=user.last().username).update(password=make_password(password1))
        user.delete()

        messages.success(request, 'Password Reset Successfully. Login To Continue')
        return redirect('/login')

    return render(request, 'new_password.html', {'user':user.last()})



def custom_logout(request):
    logout(request)
    return redirect("/login")