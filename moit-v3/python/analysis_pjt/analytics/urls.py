from django.urls import path
from . import views


urlpatterns = [

    # Pandas 신고 통계 분석
    path(
        'api/report-analysis/',
        views.analyze_report_statistics,
        name='report-analysis'
    ),

    # Spring Boot → Django 통계 데이터 수신
    path(
        'api/statistics/',
        views.api_receive_statistics,
        name='api_receive_statistics'
    ),

]