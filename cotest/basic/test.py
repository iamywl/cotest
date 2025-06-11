import os

def generate_progress_markdown():
    # 백준 "기초 코드 작성 요령 II" 문제 목록 및 완료 여부
    # 이 '완료' 상태는 이전에 대화에서 확인된 파일 목록을 기반으로 작성되었습니다.
    # 만약 실제 파일 시스템을 스캔하여 동적으로 업데이트하고 싶다면 이 부분을 수정해야 합니다.
    problems = [
        {"분류": "연습 문제", "번호": 10871, "제목": "X보다 작은 수", "완료": True},
        {"분류": "기본 문제", "번호": 1000, "제목": "A+B", "완료": False},
        {"분류": "기본 문제", "번호": 2557, "제목": "Hello World", "완료": False},
        {"분류": "기본 문제", "번호": 10171, "제목": "고양이", "완료": False},
        {"분류": "기본 문제", "번호": 10869, "제목": "사칙연산", "완료": False},
        {"분류": "기본 문제", "번호": 9498, "제목": "시험 성적", "완료": False},
        {"분류": "기본 문제", "번호": 2752, "제목": "세수정렬", "완료": True},
        {"분류": "기본 문제", "번호": 2753, "제목": "윤년", "완료": True},
        {"분류": "기본 문제", "번호": 2480, "제목": "주사위 세개", "완료": True},
        {"분류": "기본 문제", "번호": 2490, "제목": "윷놀이", "완료": True},
        {"분류": "기본 문제", "번호": 2576, "제목": "홀수", "완료": True},
        {"분류": "기본 문제", "번호": 2587, "제목": "대표값2", "완료": True},
        {"분류": "기본 문제", "번호": 2309, "제목": "일곱 난쟁이", "완료": True},
        {"분류": "기본 문제", "번호": 10093, "제목": "숫자", "완료": False},
        {"분류": "기본 문제", "번호": 1267, "제목": "핸드폰 요금", "완료": False},
        {"분류": "기본 문제", "번호": 10804, "제목": "카드 역배치", "완료": False},
        {"분류": "기본 문제", "번호": 15552, "제목": "빠른 A+B", "완료": False},
        {"분류": "기본 문제", "번호": 2438, "제목": "별 찍기 - 1", "완료": False},
        {"분류": "기본 문제", "번호": 2439, "제목": "별 찍기 - 2", "완료": True},
        {"분류": "기본 문제", "번호": 2440, "제목": "별 찍기 - 3", "완료": False},
        {"분류": "기본 문제", "번호": 2441, "제목": "별 찍기 - 4", "완료": False},
        {"분류": "기본 문제", "번호": 2442, "제목": "별 찍기 - 5", "완료": False},
        {"분류": "기본 문제", "번호": 2443, "제목": "별 찍기 - 6", "완료": False},
        {"분류": "기본 문제", "번호": 2444, "제목": "별 찍기 - 7", "완료": False},
        {"분류": "기본 문제", "번호": 2445, "제목": "별 찍기 - 8", "완료": False},
        {"분류": "기본 문제", "번호": 2446, "제목": "별 찍기 - 9", "완료": False},
        {"분류": "기본 문제", "번호": 2562, "제목": "최댓값", "완료": True},
    ]

    total_problems = len(problems)
    completed_problems = sum(1 for p in problems if p["완료"])

    # 진행률 계산 (소수점 첫째 자리까지)
    progress_percentage = (completed_problems / total_problems) * 100 if total_problems > 0 else 0
    # progress-bar.xyz는 100까지의 정수값을 받으므로 반올림
    progress_for_bar = round(progress_percentage) 

    markdown_content = []

    # 1. 시각적 진척도 바와 텍스트 진행률 헤더 추가
    # progress-bar.xyz URL 구성
    # {value}는 현재 완료된 퍼센트 (정수), {scale}은 전체 100% 기준, {title}은 바 위에 표시될 텍스트
    # {suffix}는 바 끝에 붙을 텍스트
    progress_bar_url = (
        f"https://progress-bar.xyz/{progress_for_bar}/"
        f"?scale=100" # 전체 스케일 (100% 기준)
        f"&title=progress" # 바 위에 표시될 제목
        f"&width=500" # 바의 너비
        f"&color=4CAF50" # 바의 색상 (예: 녹색)
        f"&suffix=/{total_problems}" # 완료된 개수 뒤에 전체 개수 표시
    )

    markdown_content.append(f"![{progress_percentage:.0f}%]({progress_bar_url})")
    markdown_content.append("") # 공백 줄
    markdown_content.append(f"## **진행 상황: {completed_problems}/{total_problems} 문제 완료 (약 {progress_percentage:.0f}%)**")
    markdown_content.append("---")
    markdown_content.append("")

    # 2. 문제집 제목 추가
    markdown_content.append("## 백준 문제집: 기초 코드 작성 요령 II (진행 상황)")
    markdown_content.append("")
    markdown_content.append("이 표는 백준 온라인 저지의 \"기초 코드 작성 요령 II\" 문제집에 포함된 문제들의 진행 상황을 정리한 것입니다.")
    markdown_content.append("")

    # 3. 테이블 헤더와 구분선 추가
    markdown_content.append("| 문제 분류 | 문제 번호 | 문제 제목 | 진행 상황 |")
    markdown_content.append("| :-------: | :-------: | :-------: | :-------: |")

    # 4. 문제 데이터 추가
    for p in problems:
        status = "완료" if p["완료"] else "미완료"
        problem_link = f"https://www.acmicpc.net/problem/{p['번호']}"
        markdown_content.append(f"| {p['분류']} | {p['번호']} | [{p['제목']}]({problem_link}) | {status} |")

    # 마크다운 파일로 저장
    file_name = "CURRENT.md"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(markdown_content))
        print(f"'{file_name}' 파일이 성공적으로 생성되었습니다.")
    except Exception as e:
        print(f"파일 생성 중 오류가 발생했습니다: {e}")

# 함수 실행
if __name__ == "__main__":
    generate_progress_markdown()