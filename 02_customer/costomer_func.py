import func 

custlist = func.load_data()
page = len(custlist) - 1

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
    >>>''').upper()
    
    if choice=="I":        
        print("고객 정보 입력")
        page = func.insert_data(custlist)

    elif choice=="C":
        print("현재 고객 정보 조회")
        func.current_data(custlist,page)

    elif choice == 'P':
        print("이전 고객 정보 조회")
        page = func.before_data(custlist,page)

    elif choice == 'N':
        print("다음 고객 정보 조회")
        page = func.next_data(custlist,page)

    elif choice=='D':
        print("고객 정보 삭제")
        choice1 = input('삭제하러는 이메일을 입력하세요>>>')
        delok = 0
        # for i in range(0, len(custlist)):
        #     print(custlist[i])
        for i, item in enumerate(custlist):
            if item['email'] == choice1:
                name = custlist.pop(i)['name']
                print(f'{name} 고객님의 정보가 삭제되었습니다.')
                delok = 1
                break
        if delok == 0:
            print('등록되지 않는 이메일입니다.')
            print(custlist)

    elif choice=="U":
        print("고객 정보 수정")
        while True:
            choice1 = input('수정하러는 이메일을 입력하세요>>>')
            idx = -1
            for i in range(0, len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx = i
                    break
            if idx == -1:
                print('등록되지 않은 이메일 입니다.')
                break
            choice2 = input('''
다음 중 수정할 항목을 입력하세요
(name, gender, birthyear)
수정항 정보가 없으면 "exit"
>>>''')
            if choice2 in ('name', 'gender', 'birthyear'):
                custlist[idx][choice2]= input(f'수정할 {choice2}를 입력하세요>>> ')
                break
            elif choice2 == 'exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    elif choice=="Q":
        print("프로그램 종료")
        func.save_data(custlist)
        break
