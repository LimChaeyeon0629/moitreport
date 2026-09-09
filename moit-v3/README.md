# 🚀 MOIT (모잇)

팀 프로젝트 – v3
MOIT v3 (소모임 플랫폼) - Spring Boot + React/Next.js

프로젝트 목표:
- 커뮤니티 서비스 구축 (모임 생성·참여 및 사용자 간 소통 기능 구현)
- 신고 관리 체계 고도화 (신고 접수·관리자 처리·신뢰도 반영을 연계한 운영 프로세스 구축)
- AI 판단 보조 기능 (OpenAI API와 RAG를 활용한 정책·유사 사례 기반 관리자 판단 보조)
기간 / 인원:	2026.08.12 ~ 2026.08.28 (6명)
개발 언어:	Java 17, Spring Boot 3.3.5, Spring Security, JWT Redis, JPA, MyBatis, Oracle, React, Next.js

주요기능:
- 사용자 신고 CRUD와 관리자 신고 검색·페이징·상세 조회 및 승인·반려 기능 구현
- 신고 처리 결과가 회원 신뢰도와 관리자 감사 이력에 연결되도록 서비스 로직 구성
- 운영 정책 및 신고 사례를 RAG로 검색하여 OpenAI API기반 분석 결과 제공
- 신고 처리 결과 이메일 발송 및 장기 누적 Audit Log 자동 정리
 	 
[신고 처리 동시성 제어]
- 동일 신고에 대한 중복 승인 및 신뢰도 중복 차감을 방지하기 위해 Redis Lock 적용
- Lock 획득 후 DB의 신고 상태를 재확인하여 이미 처리된 신고의 재처리 방지
→ 성과: 동시 요청 상황에서도 신고 상태와 신뢰도 데이터의 정합성을 유지할 수 있도록 보완
 	 
[비동기 이메일 처리]
- 신고 처리 완료 후 이메일이 발송되도록 트랜잭션 AFTER_COMMIT 적용
- @Async를 이용해 이메일 발송을 핵심 처리 로직과 분리하고 실패 건 재처리 구조 구성
→ 성과: 외부 이메일 서비스 지연·실패가 신고 처리 트랜잭션에 미치는 영향 최소화

[OpenAI API + RAG]
- 운영정책 및 신고 사례 문서를 청크 단위로 구성하고 관련 문맥을 검색하여 AI에 전달
- AI 분석 결과를 구조화하여 관리자 신고 상세 화면과 연계
→ 성과: 관리자가 운영 정책 및 과거 사례를 함께 참고할 수 있는 신고 판단 보조 기능 구현
 
[데이터 및 운영 이력 관리]
- 신고 삭제 방식을 물리 삭제에서 논리 삭제로 변경
- 관리자 처리 전·후 상태, 처리 사유, 신뢰도 변화 등을 Audit Log로 저장
- 처리일 기준 3년이 지난 Audit Log를 스케줄러로 자동 정리하여 장기 누적 데이터 관리
→ 성과: 추적성 확보 및 불필요한 장기 데이터 누적을 방지하여 운영 데이터 관리 효율성 향상

트러블슈팅 
1.	[동시성] Redis Lock을 통한 중복 신고 처리 방지
- 문제: 여러 관리자가 동일 신고를 동시에 승인할 경우 신뢰도 중복 차감 후 Audit Log 중복 저장 가능성
- 해결: 신고 ID 기준 Redis Lock을 적용, Lock 획득, DB에서 신고 상태가 PENDING인지 재확인
- 성과: 동시 요청 상황에서 중복 승인·반려를 방지하고 데이터의 정합성을 유지하도록 개선

2.	[외부 연동] 이메일 발송과 핵심 트랜잭션 분리
- 문제: 신고 처리 과정에서 이메일 서비스 지연·실패가 발생할 경우 핵심 처리 로직 영향 가능성
- 해결: @TransactionalEventListener(phase = AFTER_COMMIT)과 @Async를 적용하여 신고 처리 트랜잭션이 정상 커밋된 이후 이메일을 비동기 발송하도록 분리
- 성과: 코드 결합도를 낮추고, 이메일 서비스의 지연·실패가 트랜잭션에 미치는 영향 최소화

3.	[AI/RAG] LLM 판단의 근거 부족 문제 개선
- 문제: 신고 내용을 LLM에 직접 전달하는 방식만으로는 신고 정책이나 기존 처리 사례가 충분히 반영되지 않아 판단 근거가 일관되지 않을 수 있음
- 해결: 신고 내용을 Embedding으로 변환하고, 정책·기존 사례를 Chunk단위로 쪼개어 보내서 Cosine Similarity를 계산하여 관련도가 높은 Top-K 문서를 검색한 뒤 LLM Context에 함께 전달하는 RAG 구조
- 성과: 단순 GPT API 호출에서 벗어나 서비스 내부 정책과 유사 사례를 근거로 관리자 판단 보조

프로젝트 소감
- 기능 구현뿐 아니라 동시성, 데이터 정합성, 외부 서비스 장애 등 실제 운영 상황을 고려한 백엔드 설계 경험을 쌓음
- 담당 기능과 연계된 팀 기능까지 통합 테스트하여 약 11건의 오류·사용성 개선점을 발견하며 서비스 전체 흐름 검증의 중요성을 경험







## 📌 프로젝트 소개

**MOIT(모잇)**는 스터디, 프로젝트, 운동, 취미 활동 등 **공통의 관심사와 목표를 가진 사람들이 모임을 만들고 참여할 수 있는 목적형 커뮤니티 플랫폼**입니다.

1차 프로젝트에서는 기본적인 소모임 플랫폼을 구축하였으며, 2차 프로젝트에서는 **Spring Boot 기반으로 리팩토링하고 다양한 Open API와 AI 기능을 도입하여 서비스 품질과 사용자 경험을 고도화**하였습니다.

---

# 🎯 프로젝트 목표

* 목적 기반 소모임 커뮤니티 서비스 구축
* 안전하고 신뢰할 수 있는 모임 환경 제공
* AI 및 Open API를 활용한 사용자 편의성 향상
* 유지보수성과 확장성을 고려한 Spring Boot 기반 리팩토링 및 기능 고도화

---

# 📅 프로젝트 개요

| 항목    | 내용                        |
| ----- | ------------------------- |
| 프로젝트명 | MOIT (모잇)                 |
| 1차 개발 | 2026.06.16 ~ 2026.06.22   |
| 2차 개발 | 2026.07.02 ~ 2026.07.14 |
| 개발 형태 | 팀 프로젝트                    |

---

# 🔄 리팩토링 및 기술 변경

### Framework

* Spring Framework → **Spring Boot**

### Database

* MySQL → **Oracle**

### View

* JSP → **Thymeleaf**

### Security

* Spring Security 적용
* OAuth2 기반 소셜 로그인 추가
* BCrypt 비밀번호 암호화 적용

---

# ✨ 주요 기능

## 👤 회원

### 1차

* 회원가입
* 로그인

### 2차 고도화

* OAuth2 기반 소셜 로그인
* 관심사 태그 등록
* BCrypt 비밀번호 암호화
* HIBP(Have I Been Pwned) API를 활용한 비밀번호 유출 여부 검사

---

## 🤝 모임

### 1차

* 모임 등록
* 모임 조회
* 수정 / 삭제
* 모임 신청

### 2차 고도화

* OpenAI GPT API를 활용한

  * 모임 제목 자동 추천
  * 카테고리 자동 추천
  * 소개글 자동 작성
* 참가자 신뢰도 AI 평가
* 기상청 단기예보 API를 활용한 모임 날씨 알림
* VWorld 주소 검색 API 기반 주소 검색
* 네이버 MAP API를 활용한 지도 시각화

---

## 📝 후기

### 1차

* 후기 작성
* 조회
* 수정
* 삭제
* 좋아요

### 2차 고도화

* OpenAI GPT API 기반 욕설 및 비방 필터링
* OpenAI GPT API 기반 개설자 후기 분석 서비스

---

## 📨 문의

### 1차 신규 기능
* 문의 작성, 답변
* 조회
* 수정
* 삭제

### 2차 신규 기능

* OpenAI GPT API 기반 문의 비속어 필터링
* 답변 등록 시 비동기 이벤트 기반 알림 발송

---

## 🚨 신고

### 1차

* 모집글 신고
* 후기 신고
* 관리자 신고 처리

### 2차 고도화

* OpenAI GPT API 기반 신고 사유 문장 생성
* 중복 신고 방지
* SMTP 기반 신고 처리 결과 메일 자동 발송

---

## 📢 광고

### 1차

* 광고 등록
* 수정
* 삭제
* 상태 관리

### 2차 고도화

* OpenAI GPT API 기반 광고 제목 및 내용 자동 생성
* 광고 게시 상태 자동 관리 Scheduler
* SMTP 기반 광고 종료 예약 메일 발송

---

# 💡 프로젝트 특징

* Spring Boot 기반 리팩토링을 통한 유지보수성 향상
* Oracle 및 Thymeleaf 기반 서버 사이드 렌더링 적용
* OAuth2 및 Spring Security를 활용한 보안 강화
* OpenAI GPT API를 활용한 AI 추천 및 콘텐츠 생성
* 기상청, VWorld, 네이버 MAP 등 다양한 Open API 연동
* SMTP 및 비동기 이벤트를 활용한 사용자 알림 자동화
* Scheduler를 통한 광고 상태 자동 관리
* AI 기반 콘텐츠 필터링으로 안전한 커뮤니티 환경 제공

---

# 🛠 기술 스택

### Front-End

* HTML5
* CSS3
* JavaScript
* Thymeleaf

### Back-End

* Java
* Spring Boot
* Spring Security
* OAuth2
* MyBatis

### Database

* Oracle

### AI & Open API

* OpenAI GPT API
* Have I Been Pwned API
* 기상청 단기예보 API
* VWorld 주소 검색 API
* 네이버 MAP API
* SMTP Mail

### DevOps & Collaboration

* Git
* GitHub
* Notion

---

# 👥 Team

* GitHub Flow 기반 협업
* Notion을 활용한 일정 및 업무 관리
* 코드 리뷰를 통한 협업 진행

---

# 🎥 프로젝트 시연

* 회원가입 및 로그인

  * https://www.youtube.com/watch?v=jCiTv0grZYE

* 모임 등록 및 신청

  * https://www.youtube.com/watch?v=WLSxFhWPIRs

* 문의

  * https://www.youtube.com/watch?v=eWmBrzBqTeU

* 후기

  * https://www.youtube.com/watch?v=vFFOV-ELUPY

* 신고

  * https://www.youtube.com/watch?v=BbsZr3dRHZ0

* 광고

  * https://www.youtube.com/watch?v=iv0MOgaqSUI

---

## 📢 MOIT

**Meet + It = MOIT**

같은 관심사와 목표를 가진 사람들이 연결되어 함께 성장할 수 있도록 지원하는 목적형 커뮤니티 플랫폼입니다.

1차 프로젝트에서 기본 기능을 구현한 후, 2차 프로젝트에서는 **Spring Boot 리팩토링과 AI(OpenAI GPT API), OAuth2, 기상청 API, VWorld API, 네이버 MAP API 등 다양한 Open API를 적용하여 서비스의 완성도와 사용자 경험을 크게 향상**시켰습니다.
