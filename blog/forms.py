from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': '85', 'rows': '3'}))
    class Meta:
        model = Comment
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'comment'


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)
