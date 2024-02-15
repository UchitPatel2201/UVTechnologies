from django.contrib import admin
from .models import Quotation, ContactInfo

# Register your models here.
admin.site.register(Quotation)
admin.site.register(ContactInfo)
    
