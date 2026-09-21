import json
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import ReportStatistic


# ============================================================
# 신고 통계 Pandas 분석
# Spring Boot에서 이 API를 호출하고
# 분석 결과를 pages/admin/index.js 에 전달
# ============================================================
@csrf_exempt
def analyze_report_statistics(request):

    if request.method != 'POST':
        return JsonResponse(
            {
                'status': 'fail',
                'message': 'POST 요청만 지원합니다.'
            },
            status=405
        )

    try:
        data = json.loads(request.body)
        reports = data.get('reports', [])

        # Spring에서 받은 신고 원본 상태값을 DataFrame으로 변환
        df = pd.DataFrame(reports)

        if df.empty:
            return JsonResponse({
                'total': 0,
                'pending': 0,
                'approved': 0,
                'rejected': 0
            })

        # ★ Pandas가 직접 상태별 신고 건수 분석
        status_counts = df['status'].value_counts()
        pending = int(status_counts.get('PENDING', 0))
        approved = int(status_counts.get('APPROVED', 0))
        rejected = int(status_counts.get('REJECTED', 0))
        total = int(len(df))

        return JsonResponse({
            'total': total,
            'pending': pending,
            'approved': approved,
            'rejected': rejected
        })

    except Exception as e:
        return JsonResponse(
            {
                'status': 'error',
                'message': str(e)
            },
            status=400
        )


# ============================================================
# Spring Boot → Django 신고 통계 데이터 수신
# ============================================================
@csrf_exempt
def api_receive_statistics(request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            report_date = data.get('date')

            total = data.get('total', 0)
            pending = data.get('pending', 0)
            approved = data.get('approved', 0)
            rejected = data.get('rejected', 0)

            # 같은 날짜의 데이터가 있으면 UPDATE
            # 없으면 CREATE
            ReportStatistic.objects.update_or_create(
                date=report_date,

                defaults={
                    'total': total,
                    'pending': pending,
                    'approved': approved,
                    'rejected': rejected
                }
            )

            return JsonResponse({
                'status': 'success',
                'message': '신고 통계 데이터 갱신 완료!'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

    return JsonResponse({
        'status': 'fail',
        'message': 'POST 요청만 지원합니다.'
    }, status=405)


# ============================================================
# 기존 방문자/매출 분석 코드
# 신고 통계 기능으로 변경되어 사용하지 않음
# ============================================================

# import pandas as pd
# from django.shortcuts import render
# from .models import ServiceLog
#
# def dashboard_view(request):
#     ...