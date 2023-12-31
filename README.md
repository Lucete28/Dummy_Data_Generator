﻿# Dummy_Data_Generator
# Streamlit 데이터 생성 및 합체 웹 애플리케이션

이 프로젝트는 Streamlit을 활용하여 데이터를 생성하고 합체하며, 생성된 데이터를 다운로드하는 기능을 가진 웹 애플리케이션입니다.

[바로가기](https://dummydatagenerator-avdlyvxyctskn2nfnkbcra.streamlit.app/)

![Alt text](image.png)

## TECH 
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

## 기능 설명

### 데이터 생성

1. **사용자 지정 설정**:
   - 컬럼명, 데이터 타입, 데이터 생성 옵션을 선택합니다.
   - 정수(INT), 문자열(STRING), 실수(FLOAT), 이름(NAME), 날짜(DATE), 시간(TIME), 옵션(OPTION) 등 다양한 데이터 타입을 지원합니다.
   - 데이터 타입 별 설정을 조절하여 원하는 데이터를 생성합니다.

2. **랜덤 데이터 생성**:
   - 선택한 데이터 타입과 설정에 따라 원하는 개수의 데이터를 랜덤하게 생성합니다.
   - 누락된 값도 지정한 개수만큼 생성할 수 있습니다.

### 데이터 합체

1. **두 열 합체**:
   - 생성된 데이터 중 두 열을 선택하여 새로운 열을 만듭니다.
   - 구분자를 설정하여 합체된 값을 생성합니다.

### 데이터 다운로드

1. **CSV 파일 다운로드**:
   - 생성한 데이터를 CSV 파일로 다운로드할 수 있습니다.
   - 파일 이름을 설정하여 다운로드합니다.
