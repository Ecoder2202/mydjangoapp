from datetime import date
from django.contrib import admin

# Register your models here.

from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display=('title', 'message', 'price','upload',)
    list_filter=('title','price', 'date')


admin.site.register(Card, CardAdmin)
