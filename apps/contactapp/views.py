from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import textwrap


def contact(request):
    if request.method == "POST":
        print("DEBUG: Contact POST request received")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        courses = request.POST.get('courses')
        message = request.POST.get('message')
        print(f"DEBUG: Data - Name: {name}, Email: {email}")

        try:
            # Save to Database
            instance = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                courses=courses,
                message=message
            )
            print(f"DEBUG: Database record created with ID: {instance.id}")

            # Send Email
            subject = f"New Contact Form Submission from {name}"
            email_message = textwrap.dedent(f"""
                New inquiry details:
                ------------------
                Name: {name}
                Email: {email}
                Phone: {phone}
                Course: {courses}
                
                Message:
                {message}
                ------------------
            """).strip()

            print("DEBUG: Attempting to send email...")
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,  # From
                ['jaygautam3006@gmail.com'],   # To (your Gmail)
                fail_silently=False,
            )
            print("DEBUG: Email sent successfully")
            
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
            
        except Exception as e:
            print(f"DEBUG: ERROR in contact view: {str(e)}")
            messages.error(request, f"Error sending message: {str(e)}")
            return redirect('contact')

    return render(request, "pages/contact_us.html")

