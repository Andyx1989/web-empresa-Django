from django.contrib import admin
from django.db import models
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')
# Register your models here.
admin.site.register(Page, PageAdmin)

# Register your models here.
