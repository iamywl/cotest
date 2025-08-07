# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVESla4ucDFAU4&categoryId=AWcVESla4ucDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

phone_book = {
    "홍길동": "010-1111-1111",
    "이순신": "010-1111-2222",
    "강감찬": "010-1111-3333"
}

print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for name in phone_book.keys():
    print(name)

print("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")
name_to_search = input()

if name_to_search in phone_book:
    phone_number = phone_book[name_to_search]
    print(f"{name_to_search}의 전화번호는 {phone_number}입니다.")