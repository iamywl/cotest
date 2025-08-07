# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWI1J65cUDFAU4&categoryId=AWcWI1J65cUDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

inputs = [1, 2, 3, 4, 3, 2, 1]

def make_uni(arg):
    uni_list = []
    uni_list.append(arg[0])
    for i in arg:
        for j in arg:
            if uni_list[i] != arg[j]:
                uni_list.append(arg[j])
    print(uni_list)
make_uni(inputs)