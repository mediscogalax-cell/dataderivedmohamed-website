from django.shortcuts import render,HttpResponse

def about (request):
    return render(request,'index.html')
def contact (request):
    return render(request,'contacts.html')
def data(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')