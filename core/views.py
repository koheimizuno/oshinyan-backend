# admin_views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from subprocess import run

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

@staff_member_required
def backup_database(request):
    run(['sudo', '-i', '-u', 'postgres'], shell=True)
    run(['pg_dump', 'oshinyandb', '-U', 'postgres' '>', '/home/oshinyan.love/backend/DB_backup/oshinyandb.sql'], shell=True)
    return HttpResponse("The Database was backed up successfully!")

@staff_member_required
def restore_database(request):
    run(['sudo', '-i', '-u', 'postgres'], shell=True)
    run(['psql', 'oshinyandb', '<', '/home/oshinyan.love/backend/DB_backup/oshinyandb.sql'], shell=True)
    return HttpResponse("The Database was restored successfully!")