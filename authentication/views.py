from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser

# Create your views here.
# def home(request):
#     return HttpResponse("hi")

def homeU(request):
    logout(request)
    if request.method=='POST':
        search_domain=request.POST['domain']
        if search_domain=='':
            return render(request,"authentication/homeU.html")
        matching_users = CustomUser.objects.filter(domain_name=search_domain)
        # matching_users[0]
        print(matching_users)
        if matching_users:
            return redirect(matching_users[0].domain_url)
        else:
            messages.success(request, "Domain not yet registered")
            return render(request,"authentication/homeU.html")
    
    return render(request,"authentication/homeU.html")

@login_required
def homeL(request):
    if request.method=='POST':
        search_domain=request.POST['domain']
        if search_domain=='':
            return render(request,"authentication/homeU.html")
        matching_users = CustomUser.objects.filter(domain_name=search_domain)
        # matching_users[0]
        print(matching_users)
        if matching_users:
            return redirect(matching_users[0].domain_url)
        else:
            messages.success(request, "Domain not yet registered")
            return render(request,"authentication/homeL.html")
        
    return render(request,"authentication/homeL.html")

@login_required
def editM(request):
    return render(request,"authentication/editM.html")


@login_required
def editU(request):
    if request.method == 'POST':
        user = request.user
        if user is not None and user.is_authenticated:
            password = request.POST['password']
            url = request.POST['newurl']
            reenter_newurl = request.POST['reenter_newurl']

            # Use authenticate to check user credentials
            auth_user = authenticate(username=user.username, password=password)

            if auth_user is not None:
                if url == reenter_newurl:
                    # Use set_password to update the password
                    auth_user.set_password(password)
                    auth_user.domain_url = url
                    auth_user.save()
                    messages.success(request, "Profile updated successfully!")
                else:
                    messages.error(request, "URLs do not match!")
            else:
                messages.error(request, "Wrong password!")

            return render(request, 'authentication/editM.html')

        else:
            return render(request, 'authentication/homeU.html')

    return render(request, "authentication/editU.html")


@login_required
def editP(request):
    if request.method == 'POST':
        user = request.user
        if user is not None and user.is_authenticated:
            password = request.POST['oldpassword']
            newpassword = request.POST['newpassword']
            reenter_newpassword = request.POST['reenter_newpassword']

            # Use authenticate to check user credentials
            auth_user = authenticate(username=user.username, password=password)

            if auth_user is not None:
                if newpassword == reenter_newpassword:
                    # Use set_password to update the password
                    auth_user.set_password(newpassword)
                    auth_user.save()
                    messages.success(request, "Profile updated successfully!")
                else:
                    messages.error(request, "passwords do not match!")
            else:
                messages.error(request, "Wrong password!")

            return render(request, 'authentication/editM.html')

        else:
            return render(request, 'authentication/homeU.html')

    return render(request, "authentication/editP.html")



@login_required
def editD(request):
    if request.method == 'POST':
        user = request.user
        if user is not None and user.is_authenticated:
            password = request.POST['password']
            newDomain = request.POST['newDomain']
            reenter_newDomain = request.POST['reenter_newDomain']

            auth_user = authenticate(username=user.username, password=password)

            if auth_user is not None:
                if newDomain == reenter_newDomain:
                    auth_user.set_password(password)
                    auth_user.domain_name = newDomain
                    auth_user.save()
                    messages.success(request, "Profile updated successfully!")
                else:
                    messages.error(request, "domains do not match!")
            else:
                messages.error(request, "Wrong password!")

            return render(request, 'authentication/editM.html')

        else:
            return render(request, 'authentication/homeU.html')

    return render(request, "authentication/editD.html")



def signup(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['password']
        reenter_password=request.POST['reenter_password']
        domain_name=request.POST['domain_name']
        url=request.POST['url']

        myuser=CustomUser.objects.create_user(username,password)
        myuser.domain_url=url
        myuser.reenter_password=reenter_password
        myuser.domain_name=domain_name
        myuser.save()

        messages.success(request,"account created successfully!!!")

        return redirect('login.html')

    return render(request,"authentication/signup.html")


def loginn(request):

    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']
        
        user=authenticate(request,username=user_name,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect('homeL.html')
        else:
            messages.error(request,"incorrect cred!")
            return render(request,'authentication/homeU.html')
    return render(request,"authentication/login.html")

@login_required
def signout(request):
    messages.sucess(request,"logged out sucessfully")
    return redirect('homeU.html')