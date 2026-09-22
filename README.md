# 🚀 MOIT Report Portfolio

<img width="1983" height="793" alt="KakaoTalk_20260918_141127112" src="https://github.com/user-attachments/assets/c6ee182c-54f7-421f-9e72-9970e5dd6310" />

MOIT 팀 프로젝트에서 담당한 **사용자 신고 및 관리자 신고 처리 기능**을 중심으로,

v1 → v2 → v3까지 기능을 확장하고 실제 AWS 환경에 배포한 개인 포트폴리오 저장소입니다.

## 📈 Report Feature Evolution

| Version | Tech Stack | 신고 기능 고도화 |
| --- | --- | --- |
| **v1** | Spring Framework, JSP, MyBatis, MySQL | 사용자 신고 CRUD, 관리자 신고 목록/상세/처리 |
| **v2** | Spring Boot, Thymeleaf, MyBatis, Oracle, OpenAI API | 중복 신고 방지, 본인 신고 방지, OpenAI API 신고 사유 생성, 이메일 발송 |
| **v3** | Spring Boot, React, Next.js, JWT, Redis, JPA, MyBatis, Oracle | Redis Lock, 신뢰도 연계, Audit Log, 비동기 이메일, RAG 기반 관리자 판단 보조 |

## 🎥 신고 기능 시연 영상

🔗 [MOIT v1 REPORT] https://www.youtube.com/watch?v=QSb3lZ5VrFA
https://github.com/LimChaeyeon0629/moitreport/tree/main/moit-v1

🔗 [MOIT v2 REPORT] https://www.youtube.com/watch?v=BbsZr3dRHZ0

🔗 [MOIT v3 REPORT] https://www.youtube.com/watch?v=QX637JXQ8XY

## 🧪 신고 기능 테스트 가이드

- **Service URL**: https://moitreport.duckdns.org/
  
배포된 서비스에서 사용자 신고 등록부터 관리자 처리까지 전체 흐름을 테스트할 수 있습니다.

### 🔑 테스트 계정

별도의 회원가입 없이 아래 데모 계정으로 신고 기능을 테스트할 수 있습니다.

| 구분 | 아이디 | 비밀번호 | 용도 |
| --- | --- | --- | --- |
| 👤 일반회원 1 | `user01` | `user123` | 신고 등록 및 신고 내역 확인 |
| 👤 일반회원 2 | `user02` | `user123` | 다른 사용자 계정 / 신고 기능 테스트 |
| 🛡 관리자 | `admin` | `admin123` | 접수된 신고 조회 및 승인·반려 처리 |

> 일반회원 계정을 2개 제공하여 다른 사용자가 작성한 콘텐츠를 대상으로 신고 기능을 테스트할 수 있습니다.

---

### 1. 사용자 신고 등록

1. [MOIT](https://moitreport.duckdns.org/)에 접속합니다.
2. 일반회원 계정 `user01`로 로그인합니다.
3. `모임 찾기`에서 신고할 모임글 또는 후기글을 선택합니다.
4. 상세 화면에서 `신고` 버튼을 누릅니다.
5. 신고 사유와 상세 내용을 입력한 뒤 신고를 등록합니다.

---

### 2. 사용자 신고 내역 확인

1. `user01` 계정으로 로그인합니다.
2. 우측 상단의 `마이페이지`를 선택합니다.
3. 사이드바의 `내 신고 내역`으로 이동합니다.
4. 등록한 신고 내용과 현재 처리 상태를 확인합니다.

---

### 3. 관리자 신고 처리

1. 로그인 화면에서 `관리자 로그인` 탭을 선택합니다.
2. 관리자 데모 계정으로 로그인합니다.

   - 아이디: `admin`
   - 비밀번호: `admin123`

3. 우측 상단의 `마이페이지`를 선택합니다.
4. 관리자 신고 관리 페이지에서 접수된 신고 목록을 확인합니다.
5. 신고 상세 화면에서 신고 내용과 관련 정보를 확인합니다.
6. 신고를 `승인` 또는 `반려` 처리합니다.

---

### 4. 처리 결과 확인

관리자가 신고를 처리한 뒤 `user01` 계정으로 다시 로그인합니다.

`마이페이지 → 내 신고 내역`

에서 변경된 신고 처리 상태를 확인할 수 있습니다.

---

### 5. 예외 처리 테스트

#### 🚫 중복 신고 방지
`user01` 계정으로 이미 신고한 동일한 게시글을 다시 신고하면 중복 신고가 차단됩니다.

#### 🚫 본인 작성 글 신고 방지
자신이 작성한 모집글 또는 후기글에 신고를 시도하면 신고가 제한됩니다.

일반회원 계정 `user01`, `user02`를 번갈아 사용하면
작성자와 신고자를 분리하여 테스트할 수 있습니다.
