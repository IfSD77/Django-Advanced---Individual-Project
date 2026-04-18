from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Avg
from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['-built_in', 'name']


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'slug': self.object.slug})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


def project_stats(request):
    projects = Project.objects.all()
    
    total_projects = projects.count()
    total_value = projects.aggregate(Sum('contract_value'))['contract_value__sum'] or 0
    avg_value = projects.aggregate(Avg('contract_value'))['contract_value__avg'] or 0
    
    context = {
        'total_projects': total_projects,
        'total_value': f"£{total_value:,.0f}" if total_value else "£0",
        'avg_value': f"£{avg_value:,.0f}" if avg_value else "£0",
    }
    
    return render(request, 'projects/project_stats.html', context)


def projects_by_type(request):
    from django.db.models import Count
    projects_by_type = {}
    for ct in Project.objects.values('construction_type__name').annotate(count=Count('id')).order_by('construction_type__name'):
        name = ct['construction_type__name']
        projects_by_type[name] = Project.objects.filter(construction_type__name=name)
    
    return render(request, 'projects/projects_by_type.html', {'projects_by_type': projects_by_type})
