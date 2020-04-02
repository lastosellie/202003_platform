"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오"""

try:
    x = int(input("정수를 입력하시오 : "))
    if x % 2 == 0:
        print("짝수")
    else:
        print("홀수")
except ValueError:
    print("No.. input is not a valid.")