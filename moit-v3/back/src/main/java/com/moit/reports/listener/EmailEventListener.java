package com.moit.reports.listener;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.springframework.transaction.event.TransactionPhase;
import org.springframework.transaction.event.TransactionalEventListener;

import com.moit.reports.dto.EmailRequestDto;
import com.moit.reports.service.SendEmailService;

import lombok.RequiredArgsConstructor;

@Component
@RequiredArgsConstructor
public class EmailEventListener {

    private final SendEmailService sendEmailService;

    @Async
    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    public void handleEmail(EmailRequestDto emailDto) {
        sendEmailService.sendEmail(emailDto);
    }
}