"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""

for i in range(1, 101):
    ret = ""
    s = str(i)
    if s.find("3") != -1 or s.find("6") != -1 or s.find("9") != -1:
        ret += "짝"
    if i % 5 == 0:
        ret += "아자"
    if ret == "":
        print(i, end=" ")
    else:
        print(ret, end=" ")