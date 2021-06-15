from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.widgets import Widget
from main.models import Contact
from captcha.fields import CaptchaField, CaptchaTextInput

ANSWER_CHOICE = [('1', 'Yes'), ('2', 'No')]


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'main/custom_field.html'


class GetInTouch(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2}), required=True)
    cc_myself = forms.BooleanField(
        widget=forms.Select(
            attrs={'style': 'position: relative; width: 80px; right: 0px;'},
            choices=ANSWER_CHOICE),
        required=False)
    captcha = CaptchaField(widget=CustomCaptchaTextInput)


class ContactForm(forms.ModelForm):

    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Details of your project idea.'}
        ),
        max_length=4000, help_text='The max length of the text is 4000')

    captcha = CaptchaField(widget=CustomCaptchaTextInput)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'type_of_service', 'details')
