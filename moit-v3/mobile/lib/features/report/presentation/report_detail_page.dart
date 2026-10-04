import 'package:flutter/material.dart';

class ReportDetailPage extends StatelessWidget {
  final Map<String, dynamic> report;

  const ReportDetailPage({super.key, required this.report});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('신고 상세')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: ListView(
          children: [
            Text('신고 번호: ${report['reportId'] ?? '-'}'),
            const SizedBox(height: 12),

            Text('대상: ${report['targetTitle'] ?? '-'}'),
            const SizedBox(height: 12),

            Text('사유: ${report['reasonCode'] ?? '-'}'),
            const SizedBox(height: 12),

            Text('상세 내용: ${report['reasonDetail'] ?? '-'}'),
            const SizedBox(height: 12),

            Text('상태: ${report['status'] ?? '-'}'),
          ],
        ),
      ),
    );
  }
}
