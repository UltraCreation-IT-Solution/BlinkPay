from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
@admin.register(Payment_details)
class ViewAdmin(ImportExportModelAdmin):
    pass
