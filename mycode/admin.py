from django.contrib import admin
from mycode.models.customer.customer import Customer,Materials,Designer
# Register your models here.
admin.site.register(Customer)
admin.site.register(Materials)
admin.site.register(Designer)
