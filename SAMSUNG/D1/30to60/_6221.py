# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU9bOK4lMDFAU4&categoryId=AWcU9bOK4lMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1

inputs1 = input()
inputs2 = input()

# Result : Man1 Win!
if inputs1 == "가위" and inputs2 == "보":
    print("Result : Man1 Win!")
if inputs1 == "바위" and inputs2 == "가위":
    print("Result : Man1 Win!")
if inputs1 == "보" and inputs2 == "바위":
    print("Result : Man1 Win!")

# Result : Man2 Win!
if inputs1 == "가위" and inputs2 == "바위":
    print("Result : Man2 Win!")
if inputs1 == "바위" and inputs2 == "보":
    print("Result : Man2 Win!")
if inputs1 == "보" and inputs2 == "가위":
    print("Result : Man2 Win!")

if inputs2 == inputs1 :
    print("Result : Draw")