"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""

for i in range(1990, 2060, 4):
    print("%d년" % i, end=" ")

def find_worldcup_year():
    worldcup_years = []
    for i in range(1988, 2061):
        if i % 4 == 2:  # 월드컵 개최 연도는 4의 배수 + 2의 값이기 때문. ex) 2002, 2006, 2010
            worldcup_years.append(i)
    return worldcup_years


if __name__ == '__main__':
    print('1988년 ~ 2060년까지 중 월드컵이 개최되는 연도 : \n{}'.format(find_worldcup_year()))