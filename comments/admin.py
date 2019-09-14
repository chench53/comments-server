from django.contrib import admin

from .models import Creator, Comment

# Register your models here.

admin.site.register(Creator)
admin.site.register(Comment)
