from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse

# Create your views here.

# signup logic
def signUp(request):
    User = get_user_model()
    
    # # logged-in user does not need to register again
    # if request.user.is_authenticated:
    #     return render(request=request, template_name="dashboard.html")
    
    # form submission logic
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # return HttpResponse("Success")


        # # redirect user to the dashboard
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/login")
        
    return render(request=request, template_name="signup.html", context={})

# signin logic
def signIn(request):
    if request.method == "POST":
        username= request.POST.get("username_login")
        password= request.POST.get("password_login")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard")

        else:
            return HttpResponse("Username or Password incorrect. Please try again")
        
    return render(request=request, template_name="login.html", context={})

def index(request):
    return render(request=request, template_name="index.html")


def signOut(request):
    return render(request=request, template_name="index.html")


def dashboard(request):
    if request.user.is_authenticated:
        return render(request=request, template_name="dashboard.html")
    else:
        return redirect(index) 