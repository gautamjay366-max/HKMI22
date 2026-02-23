import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hkm.settings')
django.setup()

from hkm.models import Contact
from django.core.mail import send_mail

print("Testing Database...")
try:
    count = Contact.objects.count()
    print(f"Database OK. Contact count: {count}")
except Exception as e:
    print(f"Database Error: {e}")

print("\nTesting Email (fail_silently=False)...")
try:
    send_mail(
        "Test Subject",
        "Test Message",
        settings.EMAIL_HOST_USER,
        ['jaygautam3006@gmail.com'],
        fail_silently=False,
    )
    print("Email Sent OK")
except Exception as e:
    print(f"Email Error: {e}")
