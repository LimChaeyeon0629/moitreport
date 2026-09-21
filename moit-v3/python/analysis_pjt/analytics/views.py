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
        return JsonResponse({
            'status': 'fail',
            'message': 'POST 요청만 지원합니다.'
        }, status=405)

    try:
        # DB 데이터 가져오기
        qs = ReportStatistic.objects.all().values(
            'date',
            'total',
            'pending',
            'approved',
            'rejected'
        )

        if qs.exists():

            # DB QuerySet → Pandas DataFrame
            df = pd.DataFrame(list(qs))

            # ----------------------------------------------------
            # 📊 Pandas 데이터 분석 수행
            # ----------------------------------------------------

            # 날짜순 정렬
            df = df.sort_values('date')

            # 가장 최근 신고 통계
            latest = df.iloc[-1]

            total = int(latest['total'])
            pending = int(latest['pending'])
            approved = int(latest['approved'])
            rejected = int(latest['rejected'])

            # 평균 신고 건수
            avg_total = round(
                df['total'].mean(),
                1
            )

            # 최대 신고 건수
            max_total = int(
                df['total'].max()
            )

            # 최소 신고 건수
            min_total = int(
                df['total'].min()
            )

            # 누적 통계 데이터 합계
            total_sum = int(
                df['total'].sum()
            )

            # 처리 완료 건수
            processed = approved + rejected

            # 승인율
            if processed > 0:
                approval_rate = round(
                    approved / processed * 100,
                    1
                )
            else:
                approval_rate = 0

            # 날짜별 추이
            trend_dates = (
                df['date']
                .astype(str)
                .tolist()
            )

            trend_totals = (
                df['total']
                .tolist()
            )

        else:
            total = 0
            pending = 0
            approved = 0
            rejected = 0

            avg_total = 0
            max_total = 0
            min_total = 0
            total_sum = 0

            approval_rate = 0

            trend_dates = []
            trend_totals = []

        # ----------------------------------------------------
        # 🎯 Spring Boot로 분석 결과 반환
        # ----------------------------------------------------
        return JsonResponse({
            'total': total,
            'pending': pending,
            'approved': approved,
            'rejected': rejected,

            'avgTotal': avg_total,
            'maxTotal': max_total,
            'minTotal': min_total,
            'totalSum': total_sum,

            'approvalRate': approval_rate,

            'trendDates': trend_dates,
            'trendTotals': trend_totals
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


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