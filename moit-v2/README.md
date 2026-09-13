# 🚀 MOIT (모잇)

### 📢 MOIT = **Meet + It = MOIT**

같은 관심사와 목표를 가진 사람들이 모여 함께 성장하는 목적형 커뮤니티 플랫폼

**MOIT(모잇)** 는 스터디, 프로젝트, 운동, 취미 활동 등 **공통의 관심사와 목표를 가진 사람들이 모임을 만들고 참여할 수 있는 목적형 커뮤니티 플랫폼**입니다.

1차 프로젝트에서 기본적인 소모임 플랫폼을 구축한 후, 2차 프로젝트에서는 **Spring Boot 기반으로 리팩토링하고 AI 및 다양한 Open API를 적용하여 서비스 편의성과 기능 확장성을 높였습니다.**

---

## 📌 프로젝트 개요

| 항목    | 내용                                             |
| ----- | ---------------------------------------------- |
| 프로젝트명 | MOIT (모잇)                                      |
| 개발 버전 | MOIT v2                                        |
| 개발 기간 | 2026.07.02 ~ 2026.07.14                        |
| 개발 인원 | 6명                                             |
| 개발 형태 | 팀 프로젝트                                         |
| 담당 기능 | 사용자 및 관리자 신고 관리                                |
| 개발 목표 | Spring Boot 기반 리팩토링 및 AI·Open API를 활용한 서비스 고도화 |

---

## 🙋 담당 기능

### 🚨 신고 관리 기능

* 중복 신고 방지
* 본인 작성 글 신고 방지
* OpenAI GPT API 기반 신고 사유 문장 생성
* 관리자 신고 승인 / 반려 / 삭제 상태 변경
* SMTP 기반 신고 처리 결과 메일 자동 발송
* 신고 처리 3일 후 만족도 메일 자동 발송

---

## 🛠 기술 스택

| 구분            | 기술                                                              |
| ------------- | --------------------------------------------------------------- |
| Front-End     | HTML5, CSS3, JavaScript, Thymeleaf                              |
| Back-End      | Java 17, Spring Boot, Spring Security, OAuth2, MyBatis          |
| Database      | Oracle                                                          |
| AI & Open API | OpenAI GPT API |
| Mail          | SMTP                                                            |
| Collaboration | Git, GitHub, Notion                                             |

### 🤝 협업 방식

* GitHub Flow 기반 협업
* Git을 활용한 기능별 브랜치 관리
* Notion을 활용한 일정 및 업무 관리
* 코드 리뷰를 통한 협업 진행

---

## 🔄 리팩토링 및 기술 변경

1차 프로젝트의 구조를 기반으로 2차 프로젝트에서는 주요 기술 스택과 서비스 구조를 변경하고 기능을 고도화했습니다.

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

## 🔥 주요 기능

2차 프로젝트에서는 기존 기능을 Spring Boot 기반으로 리팩토링하고, **OpenAI GPT API와 다양한 외부 API를 활용한 사용자 지원 기능을 추가**했습니다.

### 🚨 신고

#### 1차 기능

* 모집글 신고 / 후기 신고
* 사용자 신고 작성 / 조회 / 수정 / 삭제
* 사용자 신고 목록 및 상세 조회
* 관리자 신고 목록 및 상세 조회
* 관리자 신고 승인 / 삭제 처리

#### 2차 고도화

* 중복 신고 방지
<img width="468" height="238" alt="image" src="https://github.com/user-attachments/assets/90045ded-1937-4b4d-858e-5153eb467b1b" />

  
* 본인 작성 글 신고 방지
  <img width="446" height="236" alt="image" src="https://github.com/user-attachments/assets/20fc4e76-96e4-456b-b956-a293d7ead320" />

  
* OpenAI GPT API 기반 신고 사유 문장 생성
<img width="468" height="269" alt="image" src="https://github.com/user-attachments/assets/c2e61e9e-348c-46f6-8421-76fe8a05626b" />

  
* 관리자 신고 승인 / 반려 / 삭제 상태 변경
<img width="446" height="268" alt="image" src="https://github.com/user-attachments/assets/a6252cdf-31d2-4fe8-854b-f941b7894430" />

  
* SMTP 기반 신고 처리 결과 메일 자동 발송
<img width="504" height="272" alt="image" src="https://github.com/user-attachments/assets/c006981e-421c-4f77-aeb3-4d73f3a3a373" />

  
* 신고 처리 3일 후 만족도 메일 자동 발송
<img width="481" height="282" alt="image" src="https://github.com/user-attachments/assets/e3c0411c-93e4-44c6-b201-5a6090f8e2a8" />

---

## ✨ 프로젝트 특징

* Spring Boot 기반 리팩토링을 통한 유지보수성 향상
* Oracle 및 Thymeleaf 기반 서버 사이드 렌더링 적용
* OAuth2 및 Spring Security를 활용한 보안 강화
* OpenAI GPT API를 활용한 AI 추천 및 콘텐츠 생성
* 기상청, VWorld, 네이버 MAP 등 다양한 Open API 연동
* SMTP 및 비동기 이벤트를 활용한 사용자 알림 자동화
* Scheduler를 통한 광고 상태 자동 관리
* AI 기반 콘텐츠 필터링을 통한 안전한 커뮤니티 환경 제공

---

## 💡 트러블슈팅

### 1. [검색 / 페이징] 관리자 신고 검색 기능 오류

**문제**
* 검색 조건과 상태별 버튼 필터를 함께 사용할 경우 조회 조건 충돌 문제가 발생했습니다.

**해결**
* 검색 조건과 상태 조건의 처리 흐름을 분리하고 MyBatis 쿼리와 요청 파라미터 전달 과정을 변경했습니다.

**성과**
* 관리자 신고 목록의 검색 및 페이징 기능을 안정화 했고, 복합 조회 조건 처리 방식에 대한 이해가 향상 되었습니다.
  
---

### 2. [정책 설계] 하루 신고 횟수 제한 방식 재검토

**문제**
* 신고 남용 방지를 위해 하루 최대 5회 제한을 적용했으나 과도한 제한이 될 수 있다고 판단했습니다.

**해결**
* 단순 횟수 제한 방식은 삭제하고 동일 신고 누적 패턴을 분석하거나 IP 기반 남용 탐지처럼 실제 악용 행위를 판별하는 방식으로 개선 방향성 구상했습니다.

**성과**
* 기능 제한만 추가하는 것보다 실제 사용자 행동과 운영 정책을 함께 고려해야 함을 경험했습니다.

---

## 🎥 시연 영상

### 신고 등록

🔗 [https://www.youtube.com/watch?v=QSb3lZ5VrFA&feature=youtu.be](https://www.youtube.com/watch?v=BbsZr3dRHZ0)

---

## 📝 회고

검색 조건 충돌과 배치 쿼리 개선점을 직접 확인하면서, 기능이 동작하는 것뿐 아니라 데이터 정합성과 운영 정책까지 함께 검토해야 한다는 점을 배웠습니다.
동시 처리, 실시간 점수 반영, 신고 남용 탐지 등의 한계를 V3에서 Redis Lock, 즉시 반영 방식, RAG 등으로 확장하는 계기로 뻗어 나갔습니다.
