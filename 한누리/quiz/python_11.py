"""11. 최대공약수를 구하는 함수를 구현하시오"""

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        n = x % y
        x = y
        y = n
    return x

try:
    x = int(input("첫 번째 숫자를 입력하시오 : "))
    y = int(input("두 번째 숫자를 입력하시오 : "))
    print(gcd(x, y))
except ValueError:
    print("No.. input is not a valid.")