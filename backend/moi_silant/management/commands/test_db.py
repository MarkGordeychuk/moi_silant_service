from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from openpyxl import load_workbook

from accounts.models import User as UserModel
from moi_silant.models import Directory, Machine, Maintenance, Complaint

# UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Создаёт тестовую бд из файла test_db.xlsx'
    requires_migrations_checks = True

    @staticmethod
    def create_machines(sheet):
        client_group = Group.objects.get(name="client")
        sc_group = Group.objects.get(name="service_company")

        for machine_info in sheet['A4':'Q13']:
            machine_model = machine_info[1].value
            engine_model = machine_info[3].value
            transmission_model = machine_info[5].value
            driving_axle_model = machine_info[7].value
            steering_axle_model = machine_info[9].value
            machine = Directory.objects.update_or_create(name=machine_model,
                                                         defaults={'directory_name': Directory.MACHINE_MODEL})[0]
            engine = Directory.objects.update_or_create(name=engine_model,
                                                        defaults={'directory_name': Directory.ENGINE_MODEL})[0]
            transmission = Directory.objects.update_or_create(name=transmission_model,
                                                              defaults={'directory_name': Directory.TRANSMISSION_MODEL})[0]
            driving_axle = Directory.objects.update_or_create(name=driving_axle_model,
                                                              defaults={'directory_name': Directory.DRIVING_AXLE_MODEL})[0]
            steering_axle = Directory.objects.update_or_create(name=steering_axle_model,
                                                               defaults={'directory_name': Directory.STEERING_AXLE_MODEL})[0]

            client_name = machine_info[12].value
            try:
                client = UserModel.objects.get(name=client_name)
            except UserModel.DoesNotExist:
                client = UserModel.objects.create_user(username=client_name, name=client_name, email='',
                                                       password='qwerty')
            finally:
                client.groups.add(client_group)

            service_company_name = machine_info[16].value
            try:
                service_company = UserModel.objects.get(name=service_company_name)
            except UserModel.DoesNotExist:
                service_company = UserModel.objects.create_user(username=service_company_name,
                                                                name=service_company_name, email='', password='qwerty')
            finally:
                service_company.groups.add(sc_group)

            Machine.objects.get_or_create(
                machine_model=machine,
                machine_number=machine_info[2].value,
                engine_model=engine,
                engine_number=machine_info[4].value,
                transmission_model=transmission,
                transmission_number=machine_info[6].value,
                driving_axle_model=driving_axle,
                driving_axle_number=machine_info[8].value,
                steering_axle_model=steering_axle,
                steering_axle_number=machine_info[10].value,
                shipment_date=machine_info[11].value,
                client=client,
                consignee=machine_info[13].value,
                delivery_address=machine_info[14].value,
                complete_set=machine_info[15].value,
                service_company=service_company
            )

    @staticmethod
    def create_maintenances(sheet):
        for maintenance_info in sheet['A2':'G37']:
            maintenance_type_name = maintenance_info[1].value

            maintenance_type = Directory.objects.update_or_create(name=maintenance_type_name,
                                                                  defaults={'directory_name': Directory.MAINTENANCE_TYPE})[0]

            Maintenance.objects.get_or_create(
                machine_id=maintenance_info[0].value,
                maintenance_type=maintenance_type,
                date=maintenance_info[2].value,
                operating_time=maintenance_info[3].value,
                work_order_number=maintenance_info[4].value,
                work_order_date=maintenance_info[5].value,
                organization=maintenance_info[6].value
            )

    @staticmethod
    def create_complaints(sheet):
        for complaint_info in sheet['A3':'I14']:
            failure_node = Directory.objects.update_or_create(name=complaint_info[3].value,
                                                              defaults={'directory_name': Directory.FAILURE_NODE})[0]
            recovery_method = Directory.objects.update_or_create(name=complaint_info[5].value,
                                                                 defaults={'directory_name': Directory.RECOVERY_METHOD})[0]

            Complaint.objects.get_or_create(
                machine_id=complaint_info[0].value,
                failure_date=complaint_info[1].value,
                operating_time=complaint_info[2].value,
                failure_node=failure_node,
                failure_description=complaint_info[4].value,
                recovery_method=recovery_method,
                spare_parts=complaint_info[6].value or '',
                recovery_date=complaint_info[7].value,
                downtime=complaint_info[8].value
            )

    def handle(self, *args, **options):
        wb = load_workbook('./test_db/test_db.xlsx')
        sheet_machines = wb['машины']
        sheet_maintenance = wb['ТО output']
        sheet_complaint = wb['рекламация output']
        self.create_machines(sheet_machines)
        self.create_maintenances(sheet_maintenance)
        self.create_complaints(sheet_complaint)

