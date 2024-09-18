from django.contrib import admin

from urlsAndViews.uavApp.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
