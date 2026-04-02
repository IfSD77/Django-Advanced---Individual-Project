from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, Profile


class CustomAdminSite(admin.AdminSite):
    site_header = "Structural Portfolio UK - Administration"
    site_title = "Admin Panel"
    index_title = "Dashboard"

    def has_permission(self, request):
        if not request.user.is_active:
            return False
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Administrators').exists()


admin.site = CustomAdminSite()

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)

admin.site.register(Group, GroupAdmin)
admin.site.register(Permission)

from projects.models import Project, ConstructionType
admin.site.register(Project)
admin.site.register(ConstructionType)

from designers.models import Designer
admin.site.register(Designer)

from participations.models import Participation
admin.site.register(Participation)