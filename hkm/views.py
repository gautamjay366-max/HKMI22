from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    return render(request,'pages/index.html')

def about_us(request):
    return render(request, 'pages/aboutus.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # SEND EMAIL
        subject = f"New Contact Form Message from {name}"
        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['jaygautam3006@gmail.com'],  # where you want to receive mail
            fail_silently=False,
        )


    return render(request, "pages/contact_us.html")
