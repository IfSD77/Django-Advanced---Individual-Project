from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined', 'get_groups')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'company')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()]) if obj.groups.exists() else "-"
    get_groups.short_description = 'Groups'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_short', 'linkedin_url')
    search_fields = ('user__username', 'user__email', 'user__first_name')
    list_filter = ('user__groups',)
    readonly_fields = ('user',)

    def bio_short(self, obj):
        return (obj.bio[:60] + '...') if obj.bio and len(obj.bio) > 60 else obj.bio
    bio_short.short_description = 'Bio'
