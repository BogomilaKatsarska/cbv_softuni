from django.contrib import admin

from cbv_softuni.web.models import Employee



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass