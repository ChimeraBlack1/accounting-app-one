from django import forms
from django.forms.widgets import Input
from .models import Account

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model= Account
        fields = [
            "account_number",
            "account_name",
            "account_type",
            "account_balance",
        ]

# class mySubclass(Input):
#     input_type = 'text'
#     template_name ="forms/datalist.html"


class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    # comment = forms.CharField(widget=mySubclass)


