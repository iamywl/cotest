inputs = input()
number_list_str = inputs.split(',')
odd_list = [int(num.strip()) for num in number_list_str if num.strip() and int(num.strip()) % 2 != 0]
'''
odd_list = []
for num in number_list_str:

    # 3. [안전 장치] 우선 문자열의 공백을 제거해보고, 그 결과가 비어있지 않은지 확인합니다.
    #    - num이 ' 2' -> num.strip()은 '2' -> 비어있지 않으므로 `True`
    #    - num이 ''   -> num.strip()은 ''   -> 비어있으므로 `False`
    if num.strip():
    
        # 4. [본격적인 홀수 검사] 안전 장치를 통과한 값만 숫자로 바꿔 홀수인지 확인합니다.
        #    - num.strip()이 비어있지 않은 경우에만 이 코드가 실행됩니다.
        if int(num.strip()) % 2 != 0:
        
            # 5. 모든 조건을 통과했다면, 최종 리스트에 숫자로 변환한 값을 추가합니다.
            odd_list.append(int(num.strip()))
'''
print(', '.join(map(str, odd_list)))