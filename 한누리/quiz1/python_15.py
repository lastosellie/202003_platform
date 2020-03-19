"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """

try:
    numbers = input("주민등록번호를 입력하세요 : ")
    l_numbers = numbers.split('-')
    first_number = int(l_numbers[1][:1])
    if first_number % 2 == 0:
        print("여자")
    else:
        print("남자")
except ValueError:
    print("No.. input is not valid.")