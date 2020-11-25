from django.contrib import admin
from .models import Test,Question,Answer

# Register your models here.
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)