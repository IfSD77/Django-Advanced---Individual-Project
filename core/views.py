from django.shortcuts import render
from django.utils import timezone
from django.db import models
from projects.models import Project
from designers.models import Designer

def designers_view(request):
    designers = Designer.objects.all().order_by('full_name')
    
    designer_stats = []
    for designer in designers:
        project_count = designer.participations.count()
        designer_stats.append({
            'designer': designer,
            'project_count': project_count
        })
    
    return render(request, 'core/designers.html', {
        'designer_stats': designer_stats,
    })

def designer_detail(request, slug):
    designer = Designer.objects.get(slug=slug)
    participations = designer.participations.all().select_related('project')
    
    return render(request, 'core/designer_detail.html', {
        'designer': designer,
        'participations': participations,
    })

def about_extra(request):
    return render(request, 'core/about_extra.html', {
        'current_time': timezone.now(),
    })

def contact_view(request):
    return render(request, 'core/contact.html', {
        'contact_email': 'demo@structuralportfolio.uk',
    })

# Custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
