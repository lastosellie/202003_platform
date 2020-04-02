#quiz1
'''

5.N을 입력받은 뒤, 구구다 N단을 출력하는 프로그램을 작성하시오(format 활용)

'''

N = int(input("출력할 단을 입력해주세요 : "))
for i in range(1,10): # i의 값은 1~9까지 들어간다.
    print('{} * {} = {}' .format(N,i,N*i)) # format -> 괄호 안에 원하는 값을 순서대로 삽입해준다.

'''
6.
아래와 같이 별이 찍히게 출력하시오
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

'''
a=int(input('숫자를 입력하세요~'))
for i in range(1,a+1): # i의 값은 1부터 input 으로 받은 값까지
    print((a-i)*' ',i*'★') # #다이아몬드모양은 첫줄만 보면 뛰어쓰기가 입력값보다 하나씩 줄어들어지는걸 확인할수 있다.
for j in range(a-1,0,-1): # 새로운 for문으로 j값은 입력값 -1 부터 값이 1까지 줄어든다.
    print((a-j)*' ',j*'★') # 위 출력과 똑같은 방식으로 뛰어쓰기 계산 하면서 진행

'''
7.
1부터 100까지의 수의 합을 계산하던 중에 합이 1000 이상일 때,
최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


'''
total = 0 # 지속적으로 더한 값을 저장할 변수 지정
for i in range(1,101,1): # i 값은 1부터 100까지
    total = total +i # for 문이 실행될때마다 total 변수값은 1씩 증가되어 저장
    if total > 1000: # total 값이 1000이 넘어간다고 가정
        print(i) # 그때의 i값을 출력
        break #i값을 찾으면 for 문을 멈추는 명령어
'''
10.

팩토리얼을 구하는 함수를 작성하시오
ex ) 5! = 5x4x3x2x1  
  print(factoral(5)) -> 120 출력
  
'''
def factorial(n): #factorial 이라는 함수 생성
    ret = 1 # ret의 값은 1
    for i in range(n,0,-1): # i의 값은 입력값 n부터 1까지 역순으로 들어간다.
        ret *= i # ret = ret * i 라는 뜻  // 좀더 간단하게 ret*=i라 쓸수 있다.
    return ret

print(factorial(5))

'''
12.
리스트 메서드 중 하나를 이용하여 아래의 리스트를 ABCD
순으로 정렬하시오.

namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']

'''
namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
namelist.sort() #리스트 메서드 중에서 .sort()를 쓰면 오름차순으로 정렬이 된다.
print(namelist)

'''
13.
리스트 메서드 중 하나를 이용하여 아래의 리스트에 '화성'
이라는 요소를 삽입하시오.

planet =['태양','수성','금성','화성','목성','토성','천왕성','해왕성']

결과 : 
planet =['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

'''
planet =['태양','수성','금성','화성','목성','토성','천왕성','해왕성']
planet.insert(3,'지구') # 리스트 메서드 중에서 insert(a ,'띠용') 의 뜻은 리스트 인덱스 a번 자리에  띠용이 삽입 된다.
print(planet)

'''
14. 

대문자는 소문자로 소문자는 대문자로 출력하고 
영어가 아닌 문자가 입력되었을땐 '입력 형식이 잘못되었습니다'
라고 출력하는 프로그램을 작성하시오.

'''
a = input("입력 : ")
if(a.isupper() == True): # 입력값이 대문자인지 확인해주는 메소드( isupper() )
    print(a.lower()) # .lower() 소문자로 출력하기
elif(a.islower() == True): # 입력값이 소문자인지 확인해주는 메소드( islower() )
    print(a.upper()) # .upper() 대문자로 출력하기
else: # 두가지 경우가 아닐때
    print("입력 형식이 잘못되었습니다.") # text대로 출력

'''
15.
주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을
작성하시오. (리스트 split 과 슬라이싱 활용)
'''

num = input("주민등록번호 : ").split("-") # input 으로 주민등록번호를 받는데 -를 기준으로 끊는다.
                                         # 943310-1003254  를 입력하면 ['943310','1003254'] 로 적용
se = num[1] # 리스트중 2번쨰 리스트
if(se[:1] == "1" or se[:1] == "3"): #se 첫번쨰 값이 1이거나 3이면
    print("남자") #남자를 출력
elif(se[:1] == "2" or se[:1] == "4"): # #se 첫번째 값이 2이거나 4이면
    print("여자") # 여자 출력
#----------------------------------------------------- 밑에처럼 해도 상관없음.
if se[0] == "1" or se[0] == "3":
    print("남자")
elif se[0] == "2" or se[0] == "4":
    print("여자")


'''
18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.
file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']

'''
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
new_list=[] # append(append 메소드는 리스트에 새로운 값을 넣을때 쓴다.) 시킬 새로운 리스트 생성
for i in range(len(file)): # 리스트 길이만큼 for문을 돌린다. 여기선 길이가 4니까 0~3까지
    a = file[i].split(".") #split는 괄호안의 부호를 기준으로 자르는 메소드입니다.
                           # file[0]번째 값을 '.' 기준으로 잘라서 a = ['exit','py'] 이렇게 담아진다.
    new_list.append(a[0]) #a의 값중 첫번째 값을 new_list에 append 시킨다.

print(new_list)

'''
19.
다음 리스트에서 알파벳의 갯수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

'''
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
list = [] # 새로운 list 생성
for i in a: # 리스트값을 for문으로 돌려서 하나씩 확인할 수 있다.
    if len(i) == 7: # i값의 길이가 7이라고 하면
        list.append(i) # list에 append 시킨다.

print(list)

'''
20.
1부터 100까지 369 게임을 하는데 3,6,9가 들어가는 부분에는
'짝' 을 출력하고 5의 배수에는 '아자'  그외에는 수를 출력하는
프로그램을 만드시오.

'''
for i in range(1,101): # 1부터 100까지
    j=str(i) # i를 문자형으로 변경하여 j로 바꿈 -> '짝' 과  '아자' 로 변경하기 위해서
    if '3' in j:  # j 의 값이 '3' 이면 (문자에서 같은 값을 찾으려면 in을 쓰면 됩니다!
        print('짝',end=' ') #짝이 출력 end=' ' <- 이뜻은 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
    elif '6' in j:
        print('짝',end=' ')
    elif '9' in j:
        print('짝',end=' ')
    elif i%5==0: # 나머지 계산을 하기 위해서 j가 아닌 i를 이용 j는 문자형이기 때문에.
        print('아자',end='  ')
    else:
        print(j,end='  ')

#quiz2

########### 클래스 관련 용어들은 추가 사전교육 객체지향을 보시면 자세히 나와있습니다! 참고 부탁드립니다################
'''
3.
Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
print 기능(print) # 잔액이 ( ) 원 입니다.

테스트코드
card = Movie_card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()
잔액이 20000원 입니다.
마트에서 3000원 사용했습니다.
영화관에서 8000.0원 사용했습니다.
잔액이 부족합니다
잔액이 9000.0원 입니다.

'''
class Card: #클래스 생성
    def __init__(self): #객체가 만들어질때 바로 작동하는 함수(금액을 0으로 초기화)
       self.money=0
    def charge(self,num): #충전 함수 (입력값 만큼 값이 money에 충전)
        self.money += num
        print('잔액이 {}원 입니다.'.format(num)) # 충전후 잔액 표시
    def consume(self,num,loc): # 소비함수 생성
        if loc =='영화관': #입력한 장소가 영화관 일때
            if self.money >= num*0.8:  # 영화관이면서 지출한 금액이 남은 금액보다 적으면
                self.money -=num*0.8 # 남은금액에서 영화비 차감
                print('영화관에서 {}원 사용했습니다.'.format(int(num*0.8))) # 쓴 비용 출력
            else:
                print('잔액이 없습니다.') # 만일 남은금액이 지출할 금액보다 적으면 잔액이 없다고 출력
        else: # 영화관 말고 딴 지역에서 사용할때
            if self.money >= num:
               self.money -= num
               print('{}에서 {}원 사용했습니다.'.format(loc,num))
            else:
               print('잔액이 부족합니다')
    def print(self): # 잔액을 알려주는 함수
        print('잔액이 {}원 입니다.'.format(int(self.money)))

card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()

'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고 
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다

'''
class Card: #카드 클래스 생성 (부모)
    def __init__(self):  #객체가 만들어질때 바로 작동하는 함수(금액을 0으로 초기화)
        self.use=0
        print('카드가 발급 되었습니다.')
    def charge(self,num): #충전 함수
        self.use+=num
        print('{}이 충전되었습니다.'.format(self.use))
    def print(self): # 잔액을 알려주는 함수
        print('잔액이 {}원 입니다'.format(self.use))
    def consume(self,num,x): # 소비하는 함수
        if self.use >= num and x==x: # 남은금액보다 사용금액이 적고 장소를 나타내는 x변수를 비교 후 소비하는 함수
            self.use -= num
            print('{}에서 {}원을 사용했습니다.'.format(x,num))
        else:
            print('잔액이 부족합니다')

class Movie_card(Card): #영화카드 클래스 생성(자식)
    def consume(self,num,x):
        if x=='영화관':
            num = num*0.8
        super().consume(num,x) #super 키워드는 부모 클래스(Card)로부터 상속받은 필드나 메소드를 자식 클래스에서 참조하는 데 사용하는 참조 변수입

class Mart_card(Card): #마트카드 클래스 생성(자식)
    def consume(self,num,x):
        if x=='마트':
            num = num*0.9
        super().consume(num,x)

class Multi_card(Movie_card,Mart_card): #영화/마트 카드 기능 + 교통카드 클래스 생성(손자)
    def consume(self,num,x):
        if x=='교통':
            num= num*0.9
        super().consume(num,x)

#영화카드는 영화관에서 사용할 때만 할인이 이루워진다.
#마트카드는 마트에서 사용할 때만 할인이 이루워진다.
#멀티카드는 영화/마트/교통에서 할인이 이루워 진다.

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(1000,'마트')
multi_card.consume(1000,'영화관')
multi_card.consume(1000,'교통')
multi_card.print()

#알고리즘

'''
2.첫 번째 숫자를 두 번째 숫자부터 마지막 숫자까지 차례대로 비교하여
가장 작은 값을 찾아 첫 번째에 놓고,  두번째 숫자를 세 번째 숫자부터
마지막 숫자까지 차례대로 비교하여그 중 가장 작은 값을 찾아
두 번째 위치에 놓는 과정을 반복하며 정렬하는것을 선택정렬이라고 합니다.
주어진 리스트를 선택정렬함수(select_sort)를 생성하여 오름차순으로 정렬하시오

'''

list=[6,2,3,7,8,10,21,1]

def select_sort(a):
    n = len(a) # 리스트의 길이를 잰다.
    for i in range(0,n-1): # i 의 변수는 0부터 7까지
        min_idx = i  #min_idx = 0
        for j in range(i+1,n):  #j의 변수는 1 ~ 7
            if a[j] < a[min_idx]: # a[1] = 2 이고 a[0] = 6   2 < 6 이므로
                min_idx = j # min_idx 의 값이 0 에서 1로 변경
        a[i] , a[min_idx] = a[min_idx],a[i]  # 비교하다보면 min_idx는 7이되고 i는 0이니까 자리바꿈 - > 리스트가 [1,2,3,7,8,21,6] 이됨 다시 첫번째 for 문으로 돌아감.
    return a

print(select_sort(list))




'''

3.앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.

'''
list=[4,3,2,1,8,7,5,10,11,16,21,6]
def bubble_sort(a):
    for j in range(len(a)-1,0,-1): # j값은 리스트의 길이 12-1 인 11 부터 하나씩 줄어듬
        for i in range(j): #i=0 ~ 10
            if a[i] < a[i+1]: #a[0] = 4 이고 a[1] 은 3 이니 조건 반족 안해서  else로 넘어감
                continue
            else:
                a[i],a[i+1] = a[i+1],a[i] # 0번째와 1번째 자리바꿈.
    return a


print(bubble_sort(list))



'''

4.탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법입니다.
여러 경우 중 하나를 선택할 때 그것이 그상황에서 가장 좋다고 생각하는 것을
선택해 나가는 방식으로 진행하여 답을 구합니다.
하지만 탐욕알고리즘은 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는
방식이기 때문에 가장 좋은 결과를 얻는 것이 보장되는것은 아닙니다.
탐욕 알고리즘을 이용하여 동전을 지불하는 함수(greedy)를 짜는데 지불해야 하는
동전의 갯수가 최소가 되도록 함수를 구현하시오
(input 으로 액수와 동전의 종류를 입력하게 구현)

'''

def greedy():
    b =[]
    money = int(input('액수입력 : '))
    cash_type = [int(x) for x in input('동전의 종류 : ').split(' ')] #띄어쓰기로 끊어서 리스트로 저장
    cash_type.sort(reverse =True) #동전의 종류를 뒤죽박죽 입력할  수도 있으니 내림차순으로 정렬
    for i in range(len(cash_type)):
        b.append('%s원 동전 %s개' %(cash_type[i], money // cash_type[i]))  #b라는 리스트에 append 시키는데 금액을 첫번째 캐쉬타입으로 나누었을때의 몫을 삽입
        money =money - ((money // cash_type[i]) * cash_type[i]) # money의 변수를 변경 -> 560원을 입력하고 cash_type의 첫번째 값이 100이라하면
                                                                # 560 - ( (560 //100) *100) = 60 으로 변경
    x=', '
    answer=x.join(b) # b라는 리스트값을 , 로 구분하여 출력
    return answer

print(greedy())