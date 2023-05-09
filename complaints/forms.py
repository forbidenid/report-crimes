from . models import Complaint
from django import forms


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['title', 'category', 'description', 'location']