from django.contrib import admin
from .models import Branch,Code,Year,Student,Teacher,User


class BranchAdmin(admin.ModelAdmin):
    list_display=['branch']

class StudentAdmin(admin.ModelAdmin):
    list_display=['user']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['user']
        

admin.site.register(Branch,BranchAdmin)
admin.site.register(Code)
admin.site.register(Year)

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(User)

# Register your models here.
