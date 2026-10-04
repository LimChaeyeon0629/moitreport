import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../data/report_provider.dart';
import 'report_detail_page.dart';

class ReportListPage extends ConsumerStatefulWidget {
  const ReportListPage({super.key});

  @override
  ConsumerState<ReportListPage> createState() => _ReportListPageState();
}

class _ReportListPageState extends ConsumerState<ReportListPage> {
  @override
  void initState() {
    super.initState();

    Future.microtask(() {
      ref.read(reportProvider.notifier).fetchReports();
    });
  }

  @override
  Widget build(BuildContext context) {
    final state = ref.watch(reportProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('내 신고 내역')),
      body: state.loading
          ? const Center(child: CircularProgressIndicator())
          : state.error != null
          ? Center(
              child: Text('조회 실패\n${state.error}', textAlign: TextAlign.center),
            )
          : state.reports.isEmpty
          ? const Center(child: Text('신고 내역이 없습니다.'))
          : ListView.builder(
              itemCount: state.reports.length,
              itemBuilder: (context, index) {
                final report = Map<String, dynamic>.from(state.reports[index]);

                return Card(
                  margin: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 6,
                  ),
                  child: ListTile(
                    title: Text(report['targetTitle'] ?? '신고 내역'),
                    subtitle: Text('상태: ${report['status'] ?? '-'}'),
                    trailing: const Icon(Icons.chevron_right),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (_) => ReportDetailPage(report: report),
                        ),
                      );
                    },
                  ),
                );
              },
            ),
    );
  }
}
