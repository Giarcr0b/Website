from django.shortcuts import get_object_or_404, render
from projects.models import Project

# Create your views here.
#def home(request):
 #   return render(request, 'home.html', {})
    

def index(request):
    projects = Project.objects.order_by('technology')[:5]
    
    context = {
        'projects': projects,
        'title': 'Projects',
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project,
        'title': 'Project Details',
    }
    return render(request, 'projects/detail.html', context)

    