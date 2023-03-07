from django.db.models import Q
from rest_framework import generics, permissions

from .models import Directory, Machine, Maintenance, Complaint
from .serializers import DirectorySerializer, MachineNotAuthSerializer, MachineAuthSerializer, MaintenanceSerializer, \
    ComplaintSerializer
from .permissions import MachinePermission, MaintenancePermission, ComplaintPermission


class DirectoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class MachineListAPIView(generics.ListCreateAPIView):
    queryset = Machine.objects.all().select_related('client', 'service_company')
    serializer_class = MachineAuthSerializer
    permission_classes = [MachinePermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.has_perms(['moi_silant.view_machine', 'moi_silant.change_machine']):
            return qs
        return qs.filter(Q(client=user) | Q(service_company=user)).distinct()


class MachineRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all().select_related('client', 'service_company', 'machine_model', 'engine_model',
                                                    'transmission_model', 'steering_axle_model', 'driving_axle_model')
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        return MachineAuthSerializer if self.request.user.is_authenticated else MachineNotAuthSerializer


class MaintenanceMixin:
    queryset = Maintenance.objects.all().select_related('machine', 'machine__client', 'machine__service_company',
                                                        'maintenance_type')
    serializer_class = MaintenanceSerializer
    permission_classes = [MaintenancePermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.has_perms(['moi_silant.view_maintenance', 'moi_silant.change_maintenance']):
            return qs
        return qs.filter(Q(machine__client=user) | Q(machine__service_company=user)).distinct()


class MaintenanceListAPIView(MaintenanceMixin, generics.ListCreateAPIView):
    pass


class MaintenanceUpdateAPIView(MaintenanceMixin, generics.UpdateAPIView):
    pass


class ComplaintMixin:
    queryset = Complaint.objects.all().select_related('machine', 'machine__client', 'machine__service_company',
                                                      'failure_node', 'recovery_method')
    serializer_class = ComplaintSerializer
    permission_classes = [ComplaintPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.has_perms(['moi_silant.view_complaint', 'moi_silant.change_complaint']):
            return qs
        return qs.filter(Q(machine__client=user) | Q(machine__service_company=user)).distinct()


class ComplaintListAPIView(ComplaintMixin, generics.ListCreateAPIView):
    pass


class ComplaintUpdateAPIView(ComplaintMixin, generics.UpdateAPIView):
    pass
