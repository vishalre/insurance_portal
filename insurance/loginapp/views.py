from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.

def login_view(request):
    # form = forms.User_form()

    if request.method == 'POST':
        insr_user = request.POST.get("username") # request['username']
        insr_pass = request.POST.get("pass");
        # test = User.objects.get(email = 'vishal@gmail.com')
        # print(test)

        user = authenticate(username=insr_user, password=insr_pass)
        print(user,"from login_view")
        # user_login = User.objects.get(username = insr_user)
        # user_login = user_login.last_login
        # print(user_login)
        # if user is not None:
        #     if user_login is None:
        #         login(request, user)
        #         return change_password(request)
        #     else:
        #         login(request, user)
        #         return test(request)
        if user is not None:
            login(request, user)
            return change_password(request)
        else:
            return redirect(reverse('login_view'))


    return render(request, 'loginapp/index.html')

@login_required
def test(request):
    return render(request, 'loginapp/comingsoon.html')

#
# def test_1(request):
#     return HttpResponse("<h1>CHANGE PASSWORD</h1>")

#work in progress
#not working properly
@login_required
def change_password(request):
    if request.method == 'POST':
        # print(request.user,request.POST)

        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            print("from change")
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login_view')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'loginapp/change_password.html', {
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))
