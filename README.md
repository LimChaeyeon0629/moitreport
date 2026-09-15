# 🚀 MOIT Report Portfolio

MOIT 팀 프로젝트에서 담당한 **사용자 신고 및 관리자 신고 처리 기능**을 중심으로,

v1 → v2 → v3까지 기능을 확장하고 실제 AWS 환경에 배포한 개인 포트폴리오 저장소입니다.

## 📈 Report Feature Evolution

| Version | Tech Stack | 신고 기능 고도화 |
| --- | --- | --- |
| **v1** | Spring Framework, JSP, MyBatis, MySQL | 사용자 신고 CRUD, 관리자 신고 목록/상세/처리 |
| **v2** | Spring Boot, Thymeleaf, MyBatis, Oracle, OpenAI API | 중복 신고 방지, 본인 신고 방지, OpenAI API 신고 사유 생성, 이메일 발송 |
| **v3** | Spring Boot, React, Next.js, JWT, Redis, JPA, MyBatis, Oracle | Redis Lock, 신뢰도 연계, Audit Log, 비동기 이메일, RAG 기반 관리자 판단 보조 |

## 🌐 Deployment

- **Service URL**: https://moitreport.duckdns.org/
- **Repository**: https://github.com/LimChaeyeon0629/moitreport
- **Deployment**: AWS EC2 / Nginx / PM2 / Docker
- **Backend**: Spring Boot
- **Frontend**: Next.js
- **Database**: Oracle
- **Cache / Lock**: Redis

## 🧪 신고 기능 테스트 가이드

배포된 서비스에서 사용자 신고 등록부터 관리자 처리까지 전체 흐름을 테스트할 수 있습니다.

### 1. 사용자 신고 등록

1. [MOIT 배포 사이트](https://moitreport.duckdns.org/)에 접속합니다.
2. 회원가입으로 생성한 일반회원 아이디로 로그인합니다.
3. `모임 찾기`에서 신고할 모임글 또는 후기글을 선택합니다.
4. 상세 화면에서 `신고`를 누릅니다.
5. 신고 사유를 작성하고 신고를 등록합니다.

### 2. 사용자 신고 내역 확인

1. 일반회원으로 로그인합니다.
2. 우측 상단에 `마이페이지`를 누릅니다.
3. 사이드바에 `내 신고 내역`으로 이동합니다.

### 3. 관리자 신고 처리

관리자 테스트 계정은 다음과 같습니다.

| 구분 | 계정 |
| --- | --- |
| 아이디 | `admin` |
| 비밀번호 | `admin123` |

1. 로그인 화면에서 `관리자 로그인` 탭을 선택합니다.
2. 위 관리자 테스트 계정으로 로그인합니다.
3. 우측 상단에 `마이페이지`를 누릅니다.
4. 관리자 신고 관리 페이지에서 접수된 신고 목록을 확인합니다.
5. 상세 화면에서 신고 내용을 확인한 후 승인 또는 반려할 수 있습니다.

### 4. 처리 결과 확인

관리자가 신고를 처리한 뒤 일반회원 계정으로 다시 로그인하여  
`마이페이지 → 신고 목록`에서 변경된 처리 상태를 확인합니다.

