from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# Projects views
from projects.views import (
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView, project_stats,
    project_by_year, project_by_type, projects_by_designer
)

# Accounts views
from accounts.views import RegisterView, CustomLoginView, CustomLogoutView, ProfileUpdateView, ProfileAPI

# API views
from projects.api_views import ProjectListAPI, ProjectDetailAPI, ProjectCreateAPI, DesignerListAPI

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    # Home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Projects web views
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

    # ================== API Endpoints ==================
    path('api/projects/', ProjectListAPI.as_view(), name='api_project_list'),
    path('api/projects/<slug:slug>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('api/projects/create/', ProjectCreateAPI.as_view(), name='api_project_create'),
    path('api/designers/', DesignerListAPI.as_view(), name='api_designer_list'),
    path('api/profile/', ProfileAPI.as_view(), name='api_profile'),
]

handler404 = 'django.views.defaults.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)