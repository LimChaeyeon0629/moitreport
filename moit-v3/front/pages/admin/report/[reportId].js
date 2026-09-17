return (
    <div className="report-detail-page">

        <div className="admin-report-detail-grid">

            {/* ======================================
                A. 관리자 신고 상세보기
            ====================================== */}
            <Card className="admin-report-detail-main">
                <Title level={2} className="admin-report-detail-title">
                    관리자 신고 상세보기
                </Title>

                <Descriptions
                    bordered
                    column={1}
                    className="report-detail-descriptions"
                >
                    <Descriptions.Item label="신고자">
                        {currentReport.memberNickname ?? '-'}{' / '}
                        {currentReport?.trustScore}점{' '}
                        <ReportStatusCodeTag
                            statusCode={currentReport.statusCode}
                        />
                    </Descriptions.Item>

                    <Descriptions.Item label="신고 대상">
                        {currentReport.targetMemberNickname ?? '-'}{' / '}
                        {currentReport?.targetTrustScore}점{' '}
                        <ReportStatusCodeTag
                            statusCode={currentReport.targetStatusCode}
                        />
                    </Descriptions.Item>

                    <Descriptions.Item label="접수 번호">
                        {formatReceiptNumber(
                            currentReport.createdAt,
                            currentReport.reportId
                        )}
                    </Descriptions.Item>

                    <Descriptions.Item label="신고 게시글">
                        {getTargetTypeText(currentReport.targetType)}
                        {' · '}
                        {currentReport.targetTitle || '삭제된 게시글'}
                    </Descriptions.Item>

                    <Descriptions.Item label="신고 사유">
                        {getReasonCodeText(currentReport.reasonCode)}
                        ({currentReport.reasonCode})
                    </Descriptions.Item>

                    <Descriptions.Item label="상세 내용">
                        <div className="report-detail-description-text">
                            {currentReport.reasonDetail
                                ? currentReport.reasonDetail
                                : '작성된 상세 내용이 없습니다.'}
                        </div>
                    </Descriptions.Item>

                    <Descriptions.Item label="처리 상태">
                        <ReportStatusTag status={currentReport.status} />
                    </Descriptions.Item>

                    <Descriptions.Item label="신고일">
                        {currentReport.createdAt
                            ?.replace('T', ' ')
                            .slice(0, 19)}
                    </Descriptions.Item>

                    {currentReport.userUpdatedAt && (
                        <Descriptions.Item label="수정일자">
                            {currentReport.userUpdatedAt
                                ?.replace('T', ' ')
                                .slice(0, 19)}
                        </Descriptions.Item>
                    )}
                </Descriptions>
            </Card>


            {/* ======================================
                오른쪽 B + C
            ====================================== */}
            <div className="admin-report-detail-side">

                {/* B. AI 판단 보조 */}
                <Card className="admin-report-ai-card">
                    <Title level={4} className="admin-report-section-title">
                        AI 판단 보조
                    </Title>

                    <Space
                        direction="vertical"
                        size="middle"
                        style={{ width: '100%' }}
                    >
                        <p className="admin-report-ai-description">
                            신고 내용과 신고 대상 원문,
                            운영 기준 및 과거 유사 사례를 기반으로 분석합니다.
                        </p>

                        <span className="admin-report-ai-notice">
                            ※ AI 결과는 참고용이며 최종 승인 및 반려 결정은
                            관리자가 수행합니다.
                        </span>

                        <Button
                            type="primary"
                            onClick={handleAiAnalysis}
                            loading={aiAnalysisLoading}
                            disabled={!reportId}
                        >
                            {aiAnalysisLoading
                                ? '분석 중... ⏳'
                                : 'AI 판단 보조 요청'}
                        </Button>

                        {aiAnalysisError && (
                            <Alert
                                type="error"
                                showIcon
                                message="AI 분석 실패"
                                description={aiAnalysisError}
                            />
                        )}

                        {currentAiAnalysis && (
                            <Card
                                size="small"
                                title="AI 분석 결과"
                                className="admin-report-ai-result"
                            >
                                <div className="admin-report-ai-result-text">
                                    {currentAiAnalysis}
                                </div>
                            </Card>
                        )}
                    </Space>
                </Card>


                {/* C. 처리 사유 + 버튼 */}
                <Card className="admin-report-process-card">
                    <Title level={4} className="admin-report-section-title">
                        신고 처리
                    </Title>

                    {currentReport.status === 'PENDING' && (
                        <div className="admin-report-process-reason">
                            <Title
                                level={5}
                                className="admin-report-process-title"
                            >
                                처리 사유
                            </Title>

                            <Input.TextArea
                                rows={4}
                                placeholder="승인, 반려 또는 삭제 사유를 입력하세요."
                                value={processReason}
                                onChange={(e) => {
                                    setProcessReason(e.target.value);
                                }}
                            />
                        </div>
                    )}

                    <div className="admin-report-actions">

                        <div className="admin-report-actions-left">
                            <Button
                                onClick={() => router.push('/admin/report')}
                            >
                                목록
                            </Button>

                            <Button onClick={handleTargetView}>
                                해당 글 보기
                            </Button>
                        </div>

                        {currentReport.status === 'PENDING' && (
                            <div className="admin-report-actions-right">
                                <Button
                                    type="primary"
                                    onClick={handleApproved}
                                    loading={adminUpdate.loading}
                                >
                                    승인
                                </Button>

                                <Button
                                    danger
                                    onClick={handleRejected}
                                    loading={adminUpdate.loading}
                                >
                                    반려
                                </Button>

                                <Button
                                    danger
                                    onClick={handleDelete}
                                    loading={adminDelete.loading}
                                >
                                    삭제
                                </Button>
                            </div>
                        )}
                    </div>
                </Card>
            </div>
        </div>


        {/* ======================================
            D. 관리자 처리 이력
        ====================================== */}
        <Card className="admin-report-history-card">
            <Title level={4} className="admin-report-section-title">
                관리자 처리 이력
            </Title>

            {auditLogFetch.loading ? (
                <Spin />
            ) : auditLogs && auditLogs.length > 0 ? (

                auditLogs.map((log) => (
                    <Descriptions
                        key={log.auditLogId}
                        bordered
                        column={1}
                        size="small"
                        className="admin-report-history-item"
                    >
                        <Descriptions.Item label="처리 일시">
                            {log.processedAt
                                ? log.processedAt
                                    .replace('T', ' ')
                                    .slice(0, 19)
                                : '-'}
                        </Descriptions.Item>

                        <Descriptions.Item label="처리 관리자">
                            {log.adminNickname || '-'}
                        </Descriptions.Item>

                        <Descriptions.Item label="처리 상태">
                            <Space>
                                <ReportStatusTag
                                    status={log.previousStatus}
                                />
                                <span>→</span>
                                <ReportStatusTag
                                    status={log.changedStatus}
                                />
                            </Space>
                        </Descriptions.Item>

                        <Descriptions.Item label="관리자 처리 사유">
                            {log.processReason || '-'}
                        </Descriptions.Item>

                        <Descriptions.Item label="매너 점수 변동">
                            {log.trustScoreChange != null
                                ? `${log.trustScoreChange > 0 ? '+' : ''}${log.trustScoreChange}점`
                                : '-'}
                        </Descriptions.Item>
                    </Descriptions>
                ))

            ) : currentReport?.status === 'APPROVED'
                || currentReport.status === 'REJECTED' ? (

                <div>
                    처리 이력이 삭제되었습니다. (유효기간 3년 만료)
                </div>

            ) : (
                <div>
                    처리 이력이 없습니다.
                </div>
            )}
        </Card>

    </div>
);