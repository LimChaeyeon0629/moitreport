import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:dio/dio.dart';

class ReportState {
  final List<dynamic> reports;
  final bool loading;
  final String? error;

  const ReportState({
    this.reports = const [],
    this.loading = false,
    this.error,
  });
}

class ReportNotifier extends Notifier<ReportState> {
  late final Dio _dio;

  @override
  ReportState build() {
    _dio = Dio(BaseOptions(baseUrl: 'https://moitreport.duckdns.org'));

    return const ReportState();
  }

  Future<void> fetchReports() async {
    state = ReportState(reports: state.reports, loading: true, error: null);

    try {
      final response = await _dio.get('/api/reports/my');

      final data = response.data;

      state = ReportState(
        reports: data['reports'] ?? [],
        loading: false,
        error: null,
      );
    } catch (e) {
      state = ReportState(
        reports: state.reports,
        loading: false,
        error: e.toString(),
      );
    }
  }
}

final reportProvider = NotifierProvider<ReportNotifier, ReportState>(
  ReportNotifier.new,
);
