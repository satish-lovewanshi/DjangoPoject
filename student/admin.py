from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=('student_id','total_questions','attempt','right','wrong','marks','score','test_id','branch')





# Register your models here.
