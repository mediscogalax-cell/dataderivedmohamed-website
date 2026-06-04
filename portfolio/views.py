from django.shortcuts import render,HttpResponse,redirect
from .models import intouch
from django.contrib import messages 
from .forms import registerform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
@login_required(login_url="signup")
def home (request):
    return render(request,'index.html')
def about (request):
    return render(request,'about.html')
def contact (request):
    return render(request,'contacts.html')
def datar(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = intouch(name=name, phone=phone, email=email, message=message)
        data.save()

        # messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return redirect('contact')
def signup(request):
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('about/')
    else:
        form=registerform()
    return render(request,'regsteration/signup.html',{'form':form})
    redirect('home')




