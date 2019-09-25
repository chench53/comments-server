from django.contrib import admin

from .models import Creator, Comment, Upvote

# Register your models here.

admin.site.register(Creator)
admin.site.register(Comment)
admin.site.register(Upvote)
