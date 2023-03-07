from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Directory, Machine, Maintenance, Complaint

UserModel = get_user_model()


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = '__all__'


class ShortDirectoryRelatedField(serializers.PrimaryKeyRelatedField):
    def __init__(self, directory_name, **kwargs):
        super().__init__(queryset=Directory.objects.filter(directory_name=directory_name), **kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return {'id': value.pk, 'name': value.name}


class MachineNotAuthSerializer(serializers.ModelSerializer):
    machine_model = ShortDirectoryRelatedField(Directory.MACHINE_MODEL)
    engine_model = ShortDirectoryRelatedField(Directory.ENGINE_MODEL)
    transmission_model = ShortDirectoryRelatedField(Directory.TRANSMISSION_MODEL)
    driving_axle_model = ShortDirectoryRelatedField(Directory.DRIVING_AXLE_MODEL)
    steering_axle_model = ShortDirectoryRelatedField(Directory.STEERING_AXLE_MODEL)

    class Meta:
        model = Machine
        exclude = ['supply_contract', 'shipment_date', 'consignee', 'delivery_address', 'complete_set', 'client',
                   'service_company']


class MachineAuthSerializer(MachineNotAuthSerializer):
    client = serializers.SlugRelatedField(slug_field='name', queryset=UserModel.objects.all())
    service_company = serializers.SlugRelatedField(slug_field='name', queryset=UserModel.objects.all())

    class Meta:
        model = Machine
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    maintenance_type = ShortDirectoryRelatedField(Directory.MAINTENANCE_TYPE)
    client = serializers.SlugRelatedField(slug_field='name', read_only=True)
    service_company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Maintenance
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    failure_node = ShortDirectoryRelatedField(Directory.FAILURE_NODE)
    recovery_method = ShortDirectoryRelatedField(Directory.RECOVERY_METHOD)
    service_company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Complaint
        fields = '__all__'
