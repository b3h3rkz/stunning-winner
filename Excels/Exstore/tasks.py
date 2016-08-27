from celery import task
import django_excel
from .models import UserData

@task
def import_data(file):
    return file.save_to_database(name_columns_by_row=2,
								 model=UserData,
								 mapdict=['first_name', 'last_name', 'age', 'gender', 'address'])

