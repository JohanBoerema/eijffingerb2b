from django.contrib import admin
from django.urls import path

from orders.views import get_orderlines

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_orderlines)
]
