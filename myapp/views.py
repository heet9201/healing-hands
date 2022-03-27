from io import StringIO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from .models import Person

# Create your views here.
def index(request):
    # name = 'John'
    # messages.info(request, "This is a index")
    return render(request, 'index.html')

def signup(request):
    # messages.info(request, "This is a signup page")
    return render(request, 'loginpage.html')

def loginpage(request):
    if request.method == 'POST':
        # messages.info(request, "ummmmmmmmmmmm, okay")
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']


        # if User.objects.filter(username = username).exists():
        #     messages.info(request, "Username is already exists")
        #     return redirect('loginpage')

        # elif User.objects.filter(username__exact='').count():
        #     # messages.info(request, "It's working!!!")
        #     messages.info(request, "What are you doing?, do it right you stupid!!!!")
        #     return redirect('login')


        if User.objects.filter(username = username).exists():
                return redirect('loginpage')
        elif User.objects.filter(email = email).exists():
            return redirect('loginpage')
        else:
            # if (User.objects.create_user(username = None, password = None, email = None)):
            new_user = User.objects.create_user(username = username, password = password, email = email)
            # new_user = User.objects.create_user(username, password)
            new_user.is_active = True
            # new_user.first_name = first_name
            # new_user.last_name = last_name
            # new_user.is
            new_user.save()
            # new_user.save();
            return redirect('login')
        # else:
        #     messages.info(request, "First name is equal to the last name")
        #     return redirect('loginpage')

    else:
        # messages.info(request, "DONE!!!")
        # return redirect('login')
        return render(request, 'loginpage.html')

# @csrf_excenpt........
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        # messages.info(request, "What are you doing!!!")
        return render(request, 'loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def page_01(request):
    return render(request, 'pages/page_01.html')

def page_02(request):
    return render(request, 'pages/page_02.html')

def page_03(request):
    return render(request, 'pages/page_03.html')

def page_04(request):
    return render(request, 'pages/page_04.html')