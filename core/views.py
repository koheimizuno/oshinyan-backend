# admin_views.py
from django.contrib.admin.views.decorators import staff_member_required
from subprocess import run, CalledProcessError
from django.http import HttpResponse, HttpResponseServerError
import os

@staff_member_required
def backup_database(request):
    try:
        with open('/home/oshinyan.love/backend/DB_backup/oshinyandb.sql', 'w') as output_file:
            run(['sudo', '-i', '-u', 'postgres', 'pg_dump', 'oshinyandb'], stdout=output_file, check=True)
        # os.environ['PGPASSWORD'] = 'postgres'
        # with open('F:/Work/Oshinyan/oshinyan.love/backend/DB_backup/oshinyandb.sql', 'w') as output_file:
        #     run(['C:/Program Files/PostgreSQL/16/bin/pg_dump', '-U', 'postgres', '-d', 'oshinyandb'], stdout=output_file, check=True)
        return HttpResponse("The Database was backed up successfully! 📁✨")
    except CalledProcessError as e:
        error_message = f"An error occurred: {e}"
        return HttpResponseServerError(error_message)

@staff_member_required
def restore_database(request):
    try:
        with open('/home/oshinyan.love/backend/DB_backup/oshinyandb.sql', 'r') as input_file:
            run(['sudo', '-i', '-u', 'postgres', 'psql', 'oshinyandb'], stdin=input_file, check=True)
        return HttpResponse("The Database was restored successfully! 🔄🔙")
    except CalledProcessError as e:
        error_message = f"An error occurred: {e}"
        return HttpResponseServerError(error_message)