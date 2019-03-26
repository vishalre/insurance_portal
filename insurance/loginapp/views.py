from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.


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
    # print("hello from password")

    if request.method == 'GET':
        return render(request, 'loginapp/change_password.html')
    # else:
    #     return HttpResponse("<h1>POST OR GET METHOD ERROR OR SOMEOTHER ERROR</h1>")

    if request.method == 'POST':
        currentpassword = request.user.password #user's current password
        old_pass = request.POST.get("oldpassword")
        change_fpass = request.POST.get("firstpassword")
        change_spass = request.POST.get("secondpassword")
        # print(old_pass)
        matchcheck= check_password(old_pass, currentpassword)
        # print(matchcheck)
        if( matchcheck and (change_fpass == change_spass)):
            user1 = User.objects.get(username = request.user)
            user1.set_password(change_fpass)
            user1.save()
            update_session_auth_hash(request, user1)  # Important!
            return redirect('login_view')
        else:
             return redirect('changepass')
    else:
        return HttpResponse("<h1>METHOD ERROR</h1>")

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))

def login_view(request):
    if request.method == 'POST':
        insr_user = request.POST.get("username") # request['username']
        insr_pass = request.POST.get("pass");
        # test = User.objects.get(email = 'vishal@gmail.com')
        # print(test)

        user = authenticate(username=insr_user, password=insr_pass)

        if user is not None:
            user_last = User.objects.get(username = user)
            last_login = user_last.last_login
            print(last_login,"from login_view")
            if last_login is None:
                login(request, user)
                return redirect('changepass')
            else:
                login(request, user)
                return test(request)
        else:
            return HttpResponse("<h1>Invalid Credentials</h1>")


    return render(request, 'loginapp/index.html')
