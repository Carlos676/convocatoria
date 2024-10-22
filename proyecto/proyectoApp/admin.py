from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        'departamento',
    )