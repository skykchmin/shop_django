from django.contrib import admin
from .models import Stuser
# Register your models here.

class StuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Stuser, StuserAdmin)