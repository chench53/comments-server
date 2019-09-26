from django import forms

from .models import Comment, Upvote

# I am so confused about this ...

class UpvoteForm(forms.ModelForm):

    class Meta:
        model = Upvote
        fields = ('creator', 'comment')

class DownvoteForm(forms.Form):
    creator = forms.IntegerField()
    comment = forms.IntegerField()
