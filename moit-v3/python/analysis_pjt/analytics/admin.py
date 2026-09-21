from django.contrib import admin
from .models import ReportStatistic

# ServiceLogAdmin 클래스 정의 및 등록
# @admin.register(ServiceLog)   admin 사이트에 노출
@admin.register(ReportStatistic)
class ServiceLogAdmin(admin.ModelAdmin): 
    list_display = ('date', 'total', 'pending', 'approved', 'rejected')