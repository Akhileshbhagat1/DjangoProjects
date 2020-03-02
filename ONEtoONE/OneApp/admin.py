from django.contrib import admin
from .models import Student, Courss


class AdminStudent(admin.ModelAdmin):
    list_display = ['sno', 'sname', 'loc']


class AdminCourse(admin.ModelAdmin):
    list_display = ['cno', 'cname', 'cfee']


admin.site.register(Student, AdminStudent)
admin.site.register(Courss, AdminCourse)




