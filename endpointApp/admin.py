from django.contrib import admin
from .models import *

from django.apps import apps


# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except:
#         pass


class StudentProfileListAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in StudentProfile._meta.fields if True]


admin.site.register(StudentProfile, StudentProfileListAdmin)


class TeacherProfileListAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in TeacherProfile._meta.fields if True]


admin.site.register(TeacherProfile, TeacherProfileListAdmin)
