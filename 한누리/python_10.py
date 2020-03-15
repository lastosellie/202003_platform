"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

def factorial(num):
    ret = 1
    for i in range(1, num + 1):
      ret *= i
    return ret

try:
    num = int(input("숫자를 입력하시오 : "))
    print(factorial(num))
except ValueError:
    print("No.. input is not a valid.")