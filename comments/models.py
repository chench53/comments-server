from django.db import models
from django.utils import timezone

# Create your models here.

class Creator(models.Model):
    fullname = models.CharField(max_length=30)
    profile_picture_url = models.URLField()

    def __str__(self):
        return self.fullname


class Customer(models.Model):
    pass


class File(models.Model):
    file_url = models.URLField()
    file_mime_type = models.CharField(max_length=20)


class Comment(models.Model):
    creator = models.ForeignKey(Creator, models.SET_NULL, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    # created_by_admin = models.BooleanField()
    # created_by_current_user = models.BooleanField()
    # upvote_count = models.IntegerField(default=0)
    # user_has_upvoted = models.BooleanField()
    # is_new = models.BooleanField()

    def pulish(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.content
