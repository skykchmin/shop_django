from django.contrib import admin
from .models import Stuser
# Register your models here.

class StuserAdmin(admin.ModelAdmin):
    list_display = ('email',) #뒤에 ,을 찍는 이유: ,가 없으면 문자열로 인식 >> 튜플로 인식하게 하기 위해

admin.site.register(Stuser, StuserAdmin)