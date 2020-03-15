""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

try:
    x = int(input("첫 번째 숫자를 입력하시오 : "))
    y = int(input("두 번째 숫자를 입력하시오 : "))
    operation = input("연산기호를 입력하시오 : ")
    if operation == "+": print(x + y)
    elif operation == "-": print(x - y)
    elif operation == "*": print(x * y)
    elif operation == "/": print(x / y)
    else:
        raise ValueError
except ValueError:
    print("No.. input is not a valid.")