from django.views import generic
from django.shortcuts import get_object_or_404, render
from services.models import Service
from main.forms import GetInTouch
# Create your views here.

class IndexView(generic.FormView):

    form_class = GetInTouch
    initial = {'key': 'value'}
    template_name = 'services/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_list'] = Service.objects.order_by('order')
        context['title'] = 'Services'
        

        return context

class DetailView(generic.DetailView):

    model = Service
    form_class = GetInTouch
    initial = {'key': 'value'}
    template_name = 'services/index.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['service'] = get_object_or_404(Service, pk=service_id)
        context['title'] = 'Services'
        
        return context

def index(request):
    services = Service.objects.order_by('order')
    context = {
        'services': services,
        'title': 'Services',
    }
    return render(request, 'services/index.html', context)

def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    context = {
        'service': service,
        'title': 'Service Details',
        'form': GetInTouch()
    }
    return render(request, 'services/detail.html', context)

