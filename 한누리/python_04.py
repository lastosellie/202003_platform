"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""

def get_triangle_area(x, y):
    return x * y / 2

try:
    x = int(input("삼각형의 가로를 입력하시오 : "))
    y = int(input("삼각형의 높이를 입력하시오 : "))
    area = get_triangle_area(x, y)
    print("삼각형의 넓이 : %d" % area)
except ValueError:
    print("No.. input is not a valid.")