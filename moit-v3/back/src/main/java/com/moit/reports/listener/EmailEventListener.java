package com.moit.reports.listener;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.springframework.transaction.event.TransactionPhase;
import org.springframework.transaction.event.TransactionalEventListener;

import com.moit.reports.dto.EmailRequestDto;
import com.moit.reports.service.SendEmailService;

import lombok.RequiredArgsConstructor;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.List;
import java.util.Map;

import org.springframework.context.ApplicationEventPublisher;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.moit.meetup.entity.Meetup;
import com.moit.meetup.repository.MeetupRepository;
import com.moit.member.entity.Member;
import com.moit.member.entity.MemberInfo;
import com.moit.member.repository.MemberInfoRepository;
import com.moit.member.repository.MemberRepository;
import com.moit.reports.api.ApiEmail;
import com.moit.reports.dto.EmailRequestDto;
import com.moit.reports.dto.ReportAuditLogDto;
import com.moit.reports.dto.ReportSearchDto;
import com.moit.reports.dto.ReportsDto.ReportListResponseDto;
import com.moit.reports.dto.ReportsDto.ReportProcessDto;
import com.moit.reports.dto.ReportsDto.ReportRequestDto;
import com.moit.reports.dto.ReportsDto.ReportResponseDto;
import com.moit.reports.entity.MemberReportStatus;
import com.moit.reports.entity.Report;
import com.moit.reports.entity.ReportAuditLog;
import com.moit.reports.enums.ReportStatus;
import com.moit.reports.enums.TargetType;
import com.moit.reports.repository.MemberReportStatusRepository;
import com.moit.reports.repository.ReportAuditLogRepository;
import com.moit.reports.repository.ReportRepository;
import com.moit.review.entity.Review;
import com.moit.review.repository.ReviewRepository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Component
@RequiredArgsConstructor
public class EmailEventListener {

    private final SendEmailService sendEmailService;

    @Async
    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    public void handleEmail(EmailRequestDto emailDto) {
    	
    	log.info("========================================");
        log.info("[EMAIL] AFTER_COMMIT 이벤트 수신");
        log.info("[EMAIL] 실행 Thread = {}", Thread.currentThread().getName());
        log.info("[EMAIL] 비동기 이메일 발송 시작");

        try {
            sendEmailService.sendEmail(emailDto);
            log.info("[EMAIL] 이메일 발송 완료");
            
        } catch (Exception e) {
            log.error("[EMAIL] 이메일 발송 실패", e);
        }

        log.info("========================================");
    }
}