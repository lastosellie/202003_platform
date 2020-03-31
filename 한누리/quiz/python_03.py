"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

try:
    num = int(input("참여 인원 수를 입력하시오 : "))
    print("----------" * 2)
    max_number = 0
    numbers = []
    winner = []
    for n in range(1, num + 1):
        enter = input("%d번째 선수 Enter Key를 눌러 주사위를 던져주세요." % n)
        if enter == "":
            number = random.randint(1, 6)
            numbers.append(number)
            if number > max_number:
                winner = [n]
                max_number = number
            elif number == max_number:
                winner.append(n)
        else:
            raise ValueError
    print("----------" * 2)
    print("주사위의 눈 :")
    print(numbers)
    print("----------" * 2)
    print("승자 :")
    for w in winner:
        print("%d번째 선수" % w)
except ValueError:
    print("No.. input is not a valid.")