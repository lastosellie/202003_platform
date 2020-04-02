

def move(numDisks, fromPeg, toPeg):
    print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(fromPeg, numDisks, toPeg))

def hanoi(numDisks, fromPeg, toPeg):
    if numDisks <= 1:
        move(numDisks, fromPeg, toPeg)
    else:
        peg = 6 - (fromPeg + toPeg)
        hanoi(numDisks - 1, fromPeg, peg)
        move(numDisks, fromPeg, toPeg)
        hanoi(numDisks - 1, peg, toPeg)

hanoi(3, 1, 3)
