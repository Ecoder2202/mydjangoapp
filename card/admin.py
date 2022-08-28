from django.contrib import admin

# Register your models here.

from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display=('title',  'description', 'message', 'price','upload')
    list_filter=('title','description','message','price',)


admin.site.register(Card, CardAdmin)
