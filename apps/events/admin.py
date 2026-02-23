from django.contrib import admin
from .models import Event
from hkm.models import Contact

admin.site.register(Contact)
admin.site.register(Event)
