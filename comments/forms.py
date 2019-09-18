from django import forms

from .models import Comment, Upvote

class UpdvateForm(forms.ModelForm):

    class Meta:
        model = Upvote
        fields = ('creator', 'comment')
