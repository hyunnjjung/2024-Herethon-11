#  2024-Herethon-11: WorkLady
> **2024 여기톤(HERETHON) 11조 프로젝트**  : 사용자의 질문과 경험을 연결하는 여성 커리어 Q&A 플랫폼


##  서비스 소개
여성들이 커리어와 일상에 대한 고민을 자유롭게 나누고, 질문과 답변을 통해 경험을 공유할 수 있는 **Q&A 기반 커리어 네트워킹 플랫폼**입니다.  

모든 사용자의 프로필을 공개하여 다양한 멘토를 탐색하고, 1:1 질문 및 답변을 통해 실질적인 도움을 받을 수 있도록 설계되었습니다.

<br/>

<p align="center">
  <img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/695bfd57-a59a-4c4d-8536-e742a68a02e6" width="100%">
</p>

---

##  Service Preview

###  Q&A / 멘토링 / 채팅 기능
<p align="center">
  <img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/57d3c6df-9351-4467-bb57-49215b67a424" width="80%">
</p>

* 질문 작성 및 조회
* 멘토 기반 Q&A
* 채팅 형태의 1:1 상담 기능


###  마이페이지 및 사용자 관리
<p align="center">
  <img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/9eb5bdad-b5ab-45d8-bd13-0f1904815d46" width="80%">
</p>

* 사용자 프로필 관리
* 질문/답변 기록 조회
* 코인 시스템

---

##  기술 스택

### **Design**
![Figma](https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)

### **Front End**
![HTML5](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### **Back End**
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### **Environment & Communication**
![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![VSCode](https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white) ![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white) ![Notion](https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white)

---

##  담당 역할 (여현정)

본 프로젝트는 **Django Template 기반의 풀스택 서비스**로 구현되었으며, 저는 **백엔드 로직 설계 및 구현**을 주도하였습니다.

* **핵심 기능: 1:1 질문 및 멘토링 시스템 구현**
  * 멘토와 멘티 간의 전용 질문/답변 데이터 모델 설계
  * 채팅 UI 기반의 상담 인터페이스를 위한 비즈니스 로직 처리
* **Django 기반 백엔드 아키텍처 설계**

---

##  주요 기능

###  회원 관리
* 회원가입 / 로그인 / 로그아웃
* 세션 기반 인증 처리

###  질문 & 답변 시스템
* 질문 등록 / 조회 / 삭제
* 답변 작성 및 관리

###  멘토링 기능
* 1:1 질문 및 답변
* 채팅 형태 인터페이스

###  프로필 관리
* 사용자 프로필 생성 및 수정
* 멘토 리스트 탐색

###  코인 시스템
* 활동 기반 코인 적립
* 코인 사용 및 내역 관리

###  마이페이지
* 사용자 활동 기록 조회
* 질문/답변 히스토리 관리

---

## 개발 환경에서 실행 방법
```
django-admin startproject worklady
cd worklady
python manage.py runserver
```
## 팀원 소개
<table border="" cellspacing="0" cellpadding="0" width="100%">
<tr width="100%">
<td align="center">김보미</td>
<td align="center">김민지</td>
<td align="center">남선우</td>
<td align="center">박시현</td>
<td align="center">송예림</td>
<td align="center">여현정</td>
</tr>
<tr width="100%">
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/0fcd9a86-a106-43de-9ebc-4e43e8f4c38c" alt="sticker" width="90px"></td>
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/8f19d05d-c1eb-4f03-af95-93813ff9e639" alt="sticker" width="90px"></td>
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/f34f194d-47b9-4bd2-a74b-a24933bed287" alt="sticker" width="90px"></td>
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/3083080a-f82d-4941-bef9-7fcb278a24c2" alt="sticker" width="90px"></td>
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/7f74d31e-e34b-4eaa-8e9f-57d3b1ae112d" alt="sticker" width="90px"></td>
<td align="center"><img src="https://github.com/2024-HERETHON/2024-Herethon-11/assets/128691874/40db4470-4719-464b-ab90-4ecd316c969a" alt="sticker" width="90px"></td>
</tr>
<tr width="100%">
<td align="center">기획·디자인</td>
<td align="center">프론트엔드</td>
<td align="center">프론트엔드</td>
<td align="center">백엔드</td>
<td align="center">백엔드</td>
<td align="center">백엔드</td>
</tr>
</table>
