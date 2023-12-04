# ams_p1

23-2 소프트웨어공학 프로젝트#1,#2,3

### CUI 기반 계산기 만들기

**project#1: 2023-10-31 ~ 2023-11-17**

**project#2,3: 2023-11-29 ~ 2023-12-19**

## 구현할 기능 목록

<details>
<summary>project#1 </summary>

## project#1

1. 사용자가 입력하는 계산의 결과를 출력

   - 덧셈, 뺄셈, 곱셈만

2. 에러처리

   - 덧셈,뺄셈,곱셈이 아닌 연산자 일 때
   - 정수가 아닌 입력, 출력일 때
   - 연산자가 다를 때
   - 입력받은 값의 개수가 잘못되었을 때

3. 이스터에그

   - [7503,1111,2024,1225]가 입력되면 이스터에그 문구 출력

   </details>

## project #2,3

1.  유닛테스트 구현하기

    - 구현한 매서드 중 3개를 선택하여 유닛테스트 구현

2.  기능수정

    - 모든 동작은 숫자 입력 후 엔터키를 기준으로 실행 ⬅️ 프로젝트#1 에서는 '=' 기호로 실행

    - 에러 출력은 반드시 다음과 같은 형식으로 이루어져야 합니다. ➡️ [SYETEM] “메시지”

      ![캡처](https://github.com/xchxn/ams_p1/assets/62371559/4a6c6179-aca5-4c7c-9fb9-bc32da0bdc42)

    - 이스터에그 동작은 반드시 다음과 같은 형식

      ![그림2](https://github.com/xchxn/ams_p1/assets/62371559/419de61e-898e-4db4-ae54-25dd29669e41)

    - 이스터에그 추가

      ![3](https://github.com/xchxn/ams_p1/assets/62371559/cf4a3d01-08b9-4bf9-a8d5-77428dc3191d)

    - 팩토리얼 계산기능 추가

      ```
      0! = 1
      음수 팩토리얼은 [ERROR] Out Of Range
      두개 이상의 숫자가 입력되면 [ERROR] Input Error
      ```

      ![4](https://github.com/xchxn/ams_p1/assets/62371559/7964b5b8-16c4-4a4c-9e4a-9ba9da6a7fea)

❗ 팩토리얼 구현시 추가 요구사항

1. TDD로 개발하기
2. 중간 스크린샷 포함
3. 개발 과정은 팀원들이 공유

## 과제 요구사항

1. 인스펙션
   - 50-100 line 내외의 코드를 선정해서 inspection
   - 결과리포트 작성
2. Acceptance Testing

## 스택

### environment

Git, VSCode, pycharm

### dev

python 3.x

### comunication

Notion

---
