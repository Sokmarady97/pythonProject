import json, re

def load_data ():
    f = open('02_customer/data.json', 'r')
    return json.load(f)

def save_data(custlist):
    f = open('02_customer/data.json', 'w')
    json.dump(custlist, f, indent=2)
    f.close()

def insert_data(custlist):
    customer = {'name':'', 'gender':'', 'email':'','birthday':''}
    customer['name'] = input('이름을 입력하세요>>>')
    while True:
        customer['gender'] = input('성별을 입력하세요(M,F)>>>').upper()
        if customer['gender'] in ('M', 'F'):
            break
    while True:
        ##^[a-z][a-z0-9] it mean ^ not in [a-z][a-z0-9]
        ##{} 무한대 {최소, 최대}
        ##tang@gmail.com  ^[a-z][a-z0-9]{4,20}@[a-z]{2,10}[.][a-z]{2,10}
        regex = re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}[.][a-z]{2,10}')
        while True:
            customer['email'] = input('이메일을 입력하세요>>>')
            check = regex.search(customer['email'])
            if check:
                break
            else:
                print('@를 포함한 정확한 이메일을 입력하세요')
        id_check = 0
        for i in custlist:
            if i['email'] ==  customer['email']:
                id_check = 1
                break
        if id_check == 0:
            break
        print('중복되는 이메일이 있습니다.')
    while True:
        customer['birthday'] = input('출생년도 4자리 입력해 주세요>>>')
        if len(customer['birthday']) == 4 and customer['birthday'].isdigit():
            break
    print(customer)
    custlist.append(customer)
    print(custlist)
    page = len(custlist)-1
    print(page)
    return page

def current_data(custlist,page):
    if page >= 0:
       print(f'현재 페이지는 {page+1}쪽입니다.')
       print(custlist[page])
    else:
        print('입력된 정보가 없습니다.')

def before_data(custlist,page):
    if  page <= 0:
      print(f'첫번째 페이지 입니다.')
      print(page)
    else:
      page -= 1
      print(f'현재 페이지는 {page+1}쪽입니다.')
      print(custlist[page])
      return page

def next_data(custlist,page):
    if page >= len(custlist)-1:
      print('마지막 페이지입니다.')
      print(page)
    else:
      page += 1
      print(f'현재 페이지는 {page+1}쪽입니다.')
      print(custlist[page])
    return page