from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from loginapp.forms import *
from loginapp.models import detailsmodel,UserProfile
from newsapi import NewsApiClient



# Create your views here.
@login_required
def activity_view(request):
    return render(request,'loginapp/activity.html')

@login_required
def status_view(request):
    return render(request,'loginapp/status.html')

@login_required
def claims_view(request):
    if request.method == 'POST':
        # vv=request.POST
        # print(vv,request.FILES.get('car'))
        validate = UserProfile.objects.get(user = request.user)
        lic_post = request.POST.get('lic')
        # print(type(validate.license))
        if( (validate.license) == int(lic_post) ):  #validate.license returns int so
            ob1=detailsmodel(userid=request.user,
            licnum=request.POST.get('lic'),
            carImg=request.FILES.get('car'),
            speed=request.POST.get('speed'),
            vechilemodel=request.POST.get('vechilemodel'),
            ageofvechile=request.POST.get('age'))
            ob1.save()
            print(ob1)
            return redirect('claims_page')
        else:
            return HttpResponse('invalid license number')
    else:
        return render(request, 'loginapp/claims.html')
    return render(request,'loginapp/claims.html')

@login_required
def user_view(request):
    data = UserProfile.objects.get(user = request.user)
    return render(request,'loginapp/user.html',{'data' : data })

@login_required
def dashboard_view(request):
    import requests
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=e894820c96e44c209a7be606a4ffdcf6')
    response = requests.get(url).json()
    article = response['articles']

    results = []
    for ar in article:
        results.append(ar['title'])

    # for i in range(len(results)):
    #     print(i + 1, results[i])
    results = results[:10]

    return render(request,'loginapp/dashboard.html',{'results' : results})

# @login_required
# def detailsview(request):
#     print('dd')
#     if request.method == 'POST':
#         vv=request.POST
#         print(vv,request.FILES.get('car'))
#         ob1=detailsmodel(licnum=request.POST.get('lic'),
#         carImg=request.FILES.get('car'),
#         speed=request.POST.get('speed'),
#         vechilemodel=request.POST.get('vechilemodel'))
#         ob1.save()
#         print(ob1)
#         return redirect('logout')
#     else:
#         return render(request, 'loginapp/details.html')


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
    return render(request, 'loginapp/logout.html')

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
                return redirect('dashboard_page')
        else:
            return HttpResponse("<h1>Invalid Credentials</h1>")


    return render(request, 'loginapp/index.html')
