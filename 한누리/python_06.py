"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""
try:
    num = int(input("숫자를 입력하세요 : "))
    for x in range(1, num + 1):
        print(" " * (num - x) + "★ " * x)
    for x in range(1, num):
        print(" " * x + "★ " * (num - x))
except ValueError:
    print("No.. input is not a number.")