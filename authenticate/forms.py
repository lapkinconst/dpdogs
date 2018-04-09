from django.forms import ModelForm
from authenticate.models import CommentUser


class EditForm(ModelForm):
    class Meta:
        model = CommentUser
        fields = ('age', 'avatar',)
