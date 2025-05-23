# 
# # 아키 코값 출력하기
# print(ord("A"))
# # 아키값으로 문자 출력하기
# print(chr(65))
# 
# 
# str = "apple"
# print("str의 첫 번째 문자는", str[0], "네 번째 문자는", str[3])
# 
# a = "Hello goorm!"
# b = a[-1] + a[-2] + a[-3]
# c = a[-0]
# print(b)
# print(c)
# 
# a = "Hello goorm!"
# 
# b = a[:5]
# c = a[5:]
# d = a[6:-11]
# print(b)
# print("c:", c)
# print("d:", d)
# 
# a = "Hello goorm!"
# 
# b = a[0:-5]
# c = a[6:-11]
# 
# #[start 보다 end가 작으면 빈칸이 리턴된다.]
# print("b:",b)
# print("c:",c)

city = "seoul"
today = 12
day = "화요일"
Myfriend = "Hello My Friend"
print(Myfriend[6:8])
temperature = 26

#정수형 temperature은 문자열과 덧셈 불가 -> str(문자열)로 형변환	
announcement = city + "의 " + str(today) + "일 " +day + " 기온은 " + str(temperature) + "도 입니다."

#1번 방법
print("1번 방법 :",city,"의",today,"일",day,"기온은",temperature,"도 입니다.")
#2번 방법
print("2번 방법 :",announcement)