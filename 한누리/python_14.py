"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""


import re

uppercase_check = re.compile(r'[A-Z]')
lowercase_check = re.compile(r'[a-z]')

try:
    s = input()
    if uppercase_check.match(s):
        s = s.lower()
    elif lowercase_check.match(s):
        s = s.upper()
    else:
        raise ValueError
    print(s)

except ValueError:
    print("입력 형식이 잘못되었습니다")