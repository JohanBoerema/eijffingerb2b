from django.contrib import admin

from .models import Order, Items, User


admin.site.register([User, Order, Items])
