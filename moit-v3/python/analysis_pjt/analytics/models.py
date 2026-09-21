from django.db import models

class ReportStatistic(models.Model):
    date = models.DateField(unique=True, verbose_name="날짜")
    total = models.IntegerField(default=0, verbose_name="총 신고건수")
    pending = models.IntegerField(default=0, verbose_name="처리 대기")
    approved = models.IntegerField(default=0, verbose_name="승인")
    rejected = models.IntegerField(default=0, verbose_name="반려")

    def __str__(self):
        return f"[{self.date}] 신고 통계"