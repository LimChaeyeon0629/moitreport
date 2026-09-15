# 🚀 MOIT Report Portfolio

MOIT 팀 프로젝트에서 담당한 **사용자 신고 및 관리자 신고 처리 기능**을 중심으로,

v1 → v2 → v3까지 기능을 확장하고 실제 AWS 환경에 배포한 개인 포트폴리오 저장소입니다.

## 🌐 Deployment

- **Service URL**: https://moitreport.duckdns.org/
- **Repository**: https://github.com/LimChaeyeon0629/moitreport
- **Deployment**: AWS EC2 / Nginx / PM2 / Docker
- **Backend**: Spring Boot
- **Frontend**: Next.js
- **Database**: Oracle
- **Cache / Lock**: Redis

## 🙋 My Contribution

제가 담당한 영역은 **사용자 신고 및 관리자 신고 처리 기능**입니다.

## 📈 Report Feature Evolution

| Version | Tech Stack | 신고 기능 고도화 |
| --- | --- | --- |
| **v1** | Spring Framework, JSP, MyBatis, MySQL | 사용자 신고 CRUD, 관리자 신고 목록/상세/처리 |
| **v2** | Spring Boot, Thymeleaf, MyBatis, Oracle, OpenAI API | 중복 신고 방지, 본인 신고 방지, OpenAI API 신고 사유 생성, 이메일 발송 |
| **v3** | Spring Boot, React, Next.js, JWT, Redis, JPA, MyBatis, Oracle | Redis Lock, 신뢰도 연계, Audit Log, 비동기 이메일, RAG 기반 관리자 판단 보조 |

## 📂 Version Details

### MOIT v1

* **Tech Stack:** Spring Framework, JSP, MyBatis, MySQL, Ajax
* **Features:** 회원가입/로그인, 모임 등록 및 신청, 문의, 후기, 신고, 광고
* 📁 README: [moit-v1/README.md](https://github.com/LimChaeyeon0629/moitreport/tree/main/moit-v1)
* 📖 Notion: https://app.notion.com/p/MoA-37195798f73380cebe19e12b11b69dad?source=copy_link

### MOIT v2

* **Tech Stack:** Spring Boot, Thymeleaf, MyBatis, Oracle, Ajax, Open API
* **Features:** Spring Boot로 마이그레이션, 프로젝트 구조 개선 및 기능 고도화
* 📁 README: [moit-v2/README.md](https://github.com/LimChaeyeon0629/moitreport/tree/main/moit-v2)
* 📖 Notion: https://app.notion.com/p/MoA-37195798f73380cebe19e12b11b69dad?source=copy_link

### MOIT v3

* **Tech Stack:** Spring Boot, Gradle, JPA, MyBatis, Oracle, JWT, Redis, React, Next.js, Ant Design
* **Features:**
  * Spring Boot + Gradle 기반 백엔드 환경 구축
  * JPA 도입 및 Entity 중심 데이터 관리
  * MyBatis와 JPA를 함께 사용하는 Hybrid Persistence 구조 적용
  * JWT 기반 인증/인가 구현
  * Redis 기반 인증 및 데이터 관리
  * React + Next.js 기반 프론트엔드 전환
  * Ant Design UI 컴포넌트 적용
  * 기존 MOIT 서비스 기능 고도화 및 신규 기능 추가

* 📁 README: [moit-v3/README.md](https://github.com/LimChaeyeon0629/moitreport/tree/main/moit-v3)
* 📖 Notion: https://app.notion.com/p/MoA-37195798f73380cebe19e12b11b69dad?source=copy_link
