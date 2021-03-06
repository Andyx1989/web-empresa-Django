from django.contrib import admin
from django.db import models
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')
# Register your models here.
admin.site.register(Link, LinkAdmin)
