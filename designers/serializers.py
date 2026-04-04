from rest_framework import serializers
from .models import Designer

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = ['id', 'full_name', 'profession', 'initials', 'short_bio']