from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from projects.views import (
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView, project_stats, projects_by_type
)
from accounts.views import RegisterView, CustomLoginView, CustomLogoutView, ProfileUpdateView
from core.views import designers_view, about_extra, contact_view, designer_detail, custom_404

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    # Home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Projects
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/stats/', project_stats, name='project_stats'),
    path('projects/by-type/', projects_by_type, name='projects_by_type'),
    path('projects/<slug:slug>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<slug:slug>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/', ProjectListView.as_view(), name='project_list'),

    # Designers
    path('designers/', designers_view, name='designers'),
    path('designers/<slug:slug>/', designer_detail, name='designer_detail'),

    # Core pages
    path('about-extra/', about_extra, name='about_extra'),
    path('contact/', contact_view, name='contact'),

    # About
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]

# Custom error handlers
handler404 = 'core.views.custom_404'
handler500 = 'django.views.defaults.server_error'

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
