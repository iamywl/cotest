# src = https://www.acmicpc.net/problem/1271
# var, var1 = map(int, input().split())
# 리스트(배열)가 두 개 생기지 않는다.
# ["1000", "100"] 리스트는 한 번만 만들어집니다.
# 그 안의 값 두 개를 꺼내서 var, var1 변수에 각각 넣고 끝입니다.
# 값 개수 맞아야 한다.
# 입력이 1000 하나뿐이면 부족해서 오류.
# 1000 100 50처럼 세 개면 초과라서 오류.

# int var, var1;
# scanf("%d %d", &var, &var1);


var, var1 = map(int, input().split())
print(var//var1)
print(var%var1)

