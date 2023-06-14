from django.contrib import admin
from dashboard.models import employee, Book

# Register your models here.

# (option:1) untuk memunculkan table sederhana
# admin.site.register(employee)

# (option:2) untuk memunculkan custom table

admin.site.register(Book)


@admin.register(employee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'gender', 'employeeType')
