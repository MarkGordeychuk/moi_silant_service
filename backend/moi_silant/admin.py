from django.contrib import admin
from django.forms import ModelForm, ModelChoiceField

from .models import Directory, Machine, Maintenance, Complaint


class MachineForm(ModelForm):
    machine_model = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.MACHINE_MODEL))
    engine_model = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.ENGINE_MODEL))
    transmission_model = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.TRANSMISSION_MODEL))
    driving_axle_model = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.DRIVING_AXLE_MODEL))
    steering_axle_model = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.STEERING_AXLE_MODEL))


class MachineAdmin(admin.ModelAdmin):
    form = MachineForm


class MaintenanceForm(ModelForm):
    maintenance_type = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.MAINTENANCE_TYPE))


class MaintenanceAdmin(admin.ModelAdmin):
    form = MaintenanceForm


class ComplaintForm(ModelForm):
    failure_node = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.FAILURE_NODE))
    recovery_method = ModelChoiceField(queryset=Directory.objects.filter(directory_name=Directory.FAILURE_NODE))


class ComplaintAdmin(admin.ModelAdmin):
    form = MaintenanceForm


admin.site.register(Directory)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Complaint, ComplaintAdmin)
