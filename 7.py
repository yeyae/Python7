#문자열 포매팅 
#1. 숫자 바로 대입
"I eat %d apples." %3
#2. 문자열 바로 대입
"I eat %s apples." % "five"
#3. 숫자값을 나타내는 변수로 대입
number=3
"I eat %d apples." %number
#4. 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
#문자열 포맷 코드
#%s : 문자열(String)
#%c : 문자 1개(Character)
#%d : 정수(Integer)
#%f : 부동소수(Floating-point)
#%o : 8진수
#%x : 16진수
