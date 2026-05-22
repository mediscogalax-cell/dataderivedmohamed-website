def datar(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = intouch(name=name, phone=phone, email=email, message=message)
        data.save()

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return redirect('contact')
