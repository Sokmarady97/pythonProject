import re
custlist=[]
page=-1

def add_customer():
    name = input("input coustomer name: ")
    movies = input("input type of movies: ").split(",")
    tickets = int(input("input ticket: "))
    custlist.append({"name": "", "moveis": "", "tickets": ""})
    print("customer has been added.")

def current_customer():
    


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료            
    ''')

    if choice=="I":        
        add_customer()
    elif choice=="C":
        print("현재 고객 정보 조회")
    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
