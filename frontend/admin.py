from django.contrib import admin
from .models import Contact, Subscriber, Testimonial

# Register your models here.

admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Testimonial)
