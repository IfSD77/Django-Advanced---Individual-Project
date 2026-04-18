from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'construction_type', 'location', 'postcode', 'built_in', 'contract_value', 'contract_value_confidential', 'description', 'image']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'postcode': forms.TextInput(attrs={'placeholder': 'e.g. RH1 1AA'}),
            'built_in': forms.NumberInput(attrs={'placeholder': 'e.g. 2023'}),
        }

    def clean_built_in(self) -> None:
        built_in = self.cleaned_data.get('built_in')
        if built_in and (built_in < 1900 or built_in > 2026):
            raise forms.ValidationError("Year must be between 1900 and 2026.")
        return built_in

    def clean_contract_value(self) -> None:
        value = self.cleaned_data.get('contract_value')
        if value and value < 0:
            raise forms.ValidationError("Contract value cannot be negative.")
        return value
