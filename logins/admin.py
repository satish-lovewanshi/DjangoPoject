from django.contrib import admin
from .models import StudentReg,TeacherReg,Branch,Code,Year


class BranchAdmin(admin.ModelAdmin):
    list_display=['branch']        

admin.site.register(Branch,BranchAdmin)
admin.site.register(Code)
admin.site.register(Year)
admin.site.register(StudentReg)
admin.site.register(TeacherReg)

# Register your models here.
