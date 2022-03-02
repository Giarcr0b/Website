from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.mail import send_mail
from main.models import Testimonial, Author, Contact
from services.models import Service
# from projects.models import Project
from django.urls import reverse_lazy
from main.forms import GetInTouch, ContactForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Create your views here.


# Home page view (not listing stuff so use template view)
class indexView(generic.FormView):

    form_class = GetInTouch
    initial = {'key': 'value'}
    template_name = 'main/index.html'
    success_url = '/get_in_touch_confirm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_list'] = Service.objects.order_by('order')[0:3]
        # context['project_list'] = Project.objects.order_by('pk')[0:3]
        context['testimonial_list'] = Testimonial.objects.order_by('pk')[0:3]
        context['title'] = 'Home'

        return context


# About page view uses detail view

class AboutView(generic.FormView):

    form_class = GetInTouch
    initial = {'key': 'value'}
    model = Author
    template_name = 'main/about.html'
    success_url = '/get_in_touch_confirm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context

# Testimonials view lists testimonials so use List view


class TestimonialView(generic.FormView):

    form_class = GetInTouch
    initial = {'key': 'value'}
    template_name = 'main/testimonials.html'
    success_url = '/get_in_touch_confirm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonial_list'] = Testimonial.objects.all()
        context['title'] = 'Testimonials'
        return context


# contact page view (look at changing this to a contactview see docs)

""" class ContactView(generic.CreateView):
    form_class = ContactForm
    template_name = 'main/contact_form.html'
    success_url = '/contact_form'

    def form_valid(self,form):

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context
     """


class ContactView(generic.FormView):

    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'main/contact_form.html'
    success_url = '/get_in_touch_confirm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context

    """ def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        title = 'Contact'
        return render(request, self.template_name, {'form': form, 'title': title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        title = 'Contact'
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return HttpResponseRedirect('main:contact')

        return render(request, self.template_name, {'form': form, 'title': title}) """


""" def contact_form(request):

    title = 'Contact'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('main:contact')

    else:
        form = ContactForm()

    return render(request, 'main/contact_form.html', {'form': form, 'title': title}) """
# Get in touch form view

""" class GetInTouchView(generic.FormView):

    template_name = 'main/get_in_touch.html'
    form_class = GetInTouch
    # form = GetInTouch()
    success_url = '/thanks/'

    def form_valid(self,form):
        form.send_email()
        return super().form_valid(form) """


def get_in_touch(request):
    if request.method == 'POST':

        form = GetInTouch(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['robertson_craig@btopenworld.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(
                "It works!!",
                "This will get sent through Mailgun",
                "Anymail Sender <craig@muirfieldsoftwareservices.co.uk>",
                ["robertson_craig@btopenworld.com"]
            )
            # return redirect('home')
    else:
        form = GetInTouch()

    return render(request, 'main/get_in_touch.html', {'form': form})


def get_in_touch_confirm(request):

    context = {
        'title': 'Confirmation',

    }
    return render(request, 'main/get_in_touch_confirm.html', context)
