# admin_views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from subprocess import run, CalledProcessError
from django.http import HttpResponse, HttpResponseServerError

@staff_member_required
def backup_database(request):
    try:
        run(['sudo', '-i', '-u', 'postgres'], check=True)
        run(['pg_dump', 'oshinyandb', '-U', 'postgres', '>', '/home/oshinyan.love/backend/DB_backup/oshinyandb.sql'], shell=True, check=True)
        return HttpResponse("The Database was backed up successfully!")
    except CalledProcessError as e:
        error_message = f"An error occurred: {e}"
        return HttpResponseServerError(error_message)

@staff_member_required
def restore_database(request):
    try:
        run(['sudo', '-i', '-u', 'postgres'], shell=True)
        run(['psql', 'oshinyandb', '<', '/home/oshinyan.love/backend/DB_backup/oshinyandb.sql'], shell=True)
        return HttpResponse("The Database was restored successfully!")
    except CalledProcessError as e:
        error_message = f"An error occurred: {e}"
        return HttpResponseServerError(error_message)