from django.contrib import admin
from .models import Designer

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'short_bio')
    search_fields = ('full_name', 'profession')
    list_filter = ('profession',)
