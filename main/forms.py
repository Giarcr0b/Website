from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from main.models import Contact

ANSWER_CHOICE = [('1','Yes'), ('2','No')]

class GetInTouch(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=True)
    cc_myself = forms.BooleanField(
        widget=forms.Select(
        attrs={'style': 'position: relative; width: 80px; right: 0px;'},
        choices=ANSWER_CHOICE), 
        required=False)

class ContactForm(forms.ModelForm):

    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
         max_length=4000, help_text='The max length of the text is 4000')

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'type_of_service', 'details')

        