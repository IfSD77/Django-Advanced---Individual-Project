"""
URL configuration for struct_portfolio_advanced project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from projects.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, \
    project_stats, project_by_year, project_by_type, projects_by_designer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<slug:slug>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<slug:slug>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('projects/stats/', project_stats, name='project_stats'),
    path('projects/type/<int:type_id>/', project_by_type, name='project_by_type'),
    path('projects/year/<int:year>/', project_by_year, name='project_by_year'),
    path('projects/designer/<int:designer_id>/', projects_by_designer, name='projects_by_designer'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
]

handler404 = 'django.views.defaults.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
