from django.contrib import admin
from .models import ConstructionType, Project
from participations.models import Participation


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
    raw_id_fields = ['designer']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ParticipationInline]
    list_display = ['name', 'built_in', 'location', 'postcode', 'get_contract_value_short']
    search_fields = ['name', 'location', 'postcode']
    list_filter = ['built_in', 'contract_value_confidential']


@admin.register(ConstructionType)
class ConstructionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
