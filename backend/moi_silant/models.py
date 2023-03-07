from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class Directory(models.Model):
    MACHINE_MODEL = 'MM'
    ENGINE_MODEL = 'EM'
    TRANSMISSION_MODEL = 'TM'
    DRIVING_AXLE_MODEL = 'DAM'
    STEERING_AXLE_MODEL = 'SAM'
    MAINTENANCE_TYPE = 'MT'
    FAILURE_NODE = 'FN'
    RECOVERY_METHOD = 'RM'
    DIRECTORY_NAME_CHOICES = [
        (MACHINE_MODEL, _('Machine model')),
        (ENGINE_MODEL, _('Engine model')),
        (TRANSMISSION_MODEL, _('Transmission model')),
        (DRIVING_AXLE_MODEL, _('Driving axle model')),
        (STEERING_AXLE_MODEL, _('Steering axle model')),
        (MAINTENANCE_TYPE, _('Maintenance type')),
        (FAILURE_NODE, _('Failure node')),
        (RECOVERY_METHOD, _('Recovery method')),
    ]
    directory_name = models.CharField(max_length=3, choices=DIRECTORY_NAME_CHOICES)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"<{self.get_directory_name_display()}: {self.name}>"


class Machine(models.Model):
    machine_number = models.CharField(max_length=128, primary_key=True)
    machine_model = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    engine_model = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    engine_number = models.CharField(max_length=128)
    transmission_model = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    transmission_number = models.CharField(max_length=128)
    driving_axle_model = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    driving_axle_number = models.CharField(max_length=128)
    steering_axle_model = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    steering_axle_number = models.CharField(max_length=128)
    supply_contract = models.CharField(max_length=128)
    shipment_date = models.DateField()
    consignee = models.CharField(max_length=128)
    delivery_address = models.CharField(max_length=256)
    complete_set = models.CharField(max_length=256)
    client = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    service_company = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='+')


class Maintenance(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    date = models.DateField()
    operating_time = models.FloatField()
    work_order_number = models.CharField(max_length=128)
    work_order_date = models.DateField()
    organization = models.CharField(max_length=128)

    @property
    def client(self):
        return self.machine.client

    @property
    def service_company(self):
        return self.machine.service_company


class Complaint(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    failure_date = models.DateField()
    operating_time = models.FloatField()
    failure_node = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    failure_description = models.TextField()
    recovery_method = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='+')
    spare_parts = models.TextField(blank=True)
    recovery_date = models.DateField(null=True)
    downtime = models.FloatField()

    @property
    def service_company(self):
        return self.machine.service_company
    