from rest_framework import serializers
from .models import Project, ConstructionType

class ConstructionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionType
        fields = ['id', 'name', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    construction_type = ConstructionTypeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'slug',
            'construction_type',
            'location',
            'postcode',
            'built_in',
            'contract_value',
            'contract_value_confidential',
            'description',
            'image'
        ]