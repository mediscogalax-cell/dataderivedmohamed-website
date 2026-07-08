from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import intouch
from .forms import registerform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# HOME PAGE
def home(request):
    return render(request, "index.html")



# ABOUT PAGE
def about(request):
    return render(request, "about.html")



# CONTACT PAGE
def contact(request):
    return render(request, "contacts.html")



# CONTACT FORM SAVE
def datar(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")


        intouch.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )


        messages.success(
            request,
            "Your message has been sent successfully!"
        )


    return redirect("contact")




# =========================
# AUTHENTICATION
# =========================



# SINGLE AUTH PAGE
def auth_page(request):
    is_head = request.user.groups.filter(name="Head").exists()

    return render(request, "auth.html", {
        "is_head": is_head
    })





# LOGIN
def signin(request):

    if request.method == "POST":


        username = request.POST.get("username")

        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request,user)

            messages.success(
                request,
                "Login successful!"
            )

            return redirect("home")


        else:

            messages.error(
                request,
                "Invalid username or password."
            )


    return redirect("auth_page")






# =========================
# REGISTER / SIGNUP
# =========================



def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")


        # CHECK PASSWORD MATCH
        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("auth_page")



        # CHECK USERNAME EXISTS
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("auth_page")



        # CHECK EMAIL EXISTS
        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already registered."
            )

            return redirect("auth_page")



        # CREATE USER
        user = User.objects.create_user(

            username=username,

            email=email,

            password=password1

        )



        # LOGIN AFTER REGISTER
        login(
            request,
            user
        )



        messages.success(
            request,
            "Account created successfully!"
        )



    return redirect("auth_page")






# LOGOUT
def signout(request):

    logout(request)


    messages.success(
        request,
        "You have logged out successfully."
    )


    return redirect("home")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import intouch


@login_required(login_url='home')
def dashboard(request):

    query = request.GET.get("search")


    contacts = intouch.objects.all().order_by("-id")


    if query:

        contacts = contacts.filter(

            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(message__icontains=query)

        )


    total_messages = intouch.objects.count()


    context = {

        "contacts": contacts,

        "total_messages": total_messages,

        "query": query

    }


    return render(
        request,
        "dashboard.html",
        context
    )





def delete_message(request,id):

    contact = get_object_or_404(
        intouch,
        id=id
    )


    contact.delete()


    messages.success(
        request,
        "Message deleted successfully!"
    )


    return redirect("dashboard")