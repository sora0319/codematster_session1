### 자리수 처리하기
1. 숫자 거꾸로 출력
    - 슬라이싱으로 문자열을 거꾸로 만든 다음 '0,1,2,3' 같은 예를 없애기 위해 'int' 형으로 변형
2. 각자리 숫자 합 출력
    - 숫자를 str형으로 다시 변환 후 for문으로 받아 총합
------------
### 부정
1. 0은 거짓으로 나머지는 참으로 출력
--------
### 세로행렬
1. N x N 의 행렬을 세로로 출력
2. 2중 for문 사용
------
### 비밀번호 찾기
1. 문자열을 하나씩 출력함
    - 단, 'c'가 포함되어있으면 멈춤
------
### 등차수열
1. 입력받아서 split으로 시작 수(start), 각 값의 차(gap), 알고 싶은 항(final) 구별하기
2. start + gap * (final - 1) <== str이므로 int로 바꾸어서 계산
------
### 8진수와 16진수
1. 8진수로 나타내기 (octal_n)
    - while 문
        - 입력값 N % 8 = 나머지
        - 나머지를 octal_n에 앞에 붙이기
        - 몫이 0이면 break
2. 16진수로 나타내기 (hexadecimal)
    - while 문
        - 입력값 N % 16  = 나머지
        - 10 <= 나머지 <= 15 이면 
            - chr(나머지 + 55)을 hexadecimal에 앞에 붙이기
        - 그외 
            - hexadecimal에 앞에 붙이기
        -  몫이 0이면 break
-------
### 아스키코드
1. 입력값을 받아서 chr()로 변형해 출력한다
------
### 나머지
1. 입력값을 받아 5, 7로 나머지를 구한 후 비교해서 큰 것을 출력한다
---------
### 1등급한우
1. if 문을 사용
    - 200이상 A
    - 180이상 B
    - 150이상 C
    - 나머지 D
---------------
### 자녀의 키는
1. 두값을 받아 평균을 출력한다