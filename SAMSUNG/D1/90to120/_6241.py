# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVA-k64qMDFAU4&categoryId=AWcVA-k64qMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4&&&&&&&&&&
inputs = input()
temp = inputs.split("://")
http = temp[0]
host = temp[1].split("/")

print(f"protocol: {http}")
print(f"host: {host[0]}")
print(f"others: {host[1]}")
# print(f"http : ","".join(http[1]))
# print(f"host : ", "".join(host[0]))
# print(f"other")

######
# 입력으로 전체 URL 주소를 받습니다.
url = input()

# "://"를 기준으로 문자열을 한 번 나누어 프로토콜 부분과 나머지 부분으로 분리합니다.
protocol_parts = url.split("://")
protocol = protocol_parts[0]
rest_of_url = protocol_parts[1]

# 나머지 부분에서 첫 번째 "/"를 기준으로 문자열을 한 번 나누어 호스트와 경로/쿼리 부분으로 분리합니다.
# split('/', 1)은 첫 번째 나오는 '/'를 기준으로 최대 한 번만 분리하라는 의미입니다.
host_parts = rest_of_url.split("/", 1)
host = host_parts[0]
others = host_parts[1]

# f-string을 사용하여 지정된 형식에 맞게 결과를 출력합니다.
print(f"protocol: {protocol}")
print(f"host: {host}")
print(f"others: {others}")