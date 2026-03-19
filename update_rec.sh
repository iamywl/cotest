#!/bin/bash
# REC README 업데이트 스크립트
# - 두괄식: 디렉토리별 요약 → 파일 상세 (최신순, 누적 추가)

REC_FILE="REC.md"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

TMP_CURRENT=$(mktemp)
TMP_ALL=$(mktemp)
trap "rm -f $TMP_CURRENT $TMP_ALL" EXIT

# 현재 소스코드 파일 목록 수집 (최신순 정렬용 데이터)
total_count=0
boj_count=0
sejong_count=0
swea_count=0
other_count=0

find . -type f \( -name "*.py" -o -name "*.c" -o -name "*.cpp" -o -name "*.java" -o -name "*.js" -o -name "*.ts" -o -name "*.rs" -o -name "*.go" -o -name "*.rb" \) -not -path './.git/*' | while IFS= read -r filepath; do
    fname=$(basename "$filepath")
    dirpath=$(dirname "$filepath" | sed 's|^\./||')
    fdate=$(stat -f '%Sm' -t '%Y-%m-%d %H:%M' "$filepath" 2>/dev/null || echo "unknown")
    echo "| ${fdate} | ${fname} | ${dirpath} |" >> "$TMP_CURRENT"
done

# 현재 파일 카운트
while IFS= read -r line; do
    dirpath=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
    total_count=$((total_count + 1))
    case "$dirpath" in
        boj*) boj_count=$((boj_count + 1)) ;;
        sejong*) sejong_count=$((sejong_count + 1)) ;;
        swea*) swea_count=$((swea_count + 1)) ;;
        *) other_count=$((other_count + 1)) ;;
    esac
done < "$TMP_CURRENT"

# 기존 REC.md에서 이전 기록 추출 후 현재 목록과 병합 (중복 제거)
cp "$TMP_CURRENT" "$TMP_ALL"
if [ -f "$REC_FILE" ]; then
    grep -E '^\| [0-9]{4}-' "$REC_FILE" | while IFS= read -r line; do
        fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
        dirpath=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
        # 현재 목록에 같은 파일명+디렉토리가 없으면 추가 (삭제된 파일 기록 유지)
        if ! grep -q "| ${fname} | ${dirpath} |" "$TMP_CURRENT" 2>/dev/null; then
            echo "$line" >> "$TMP_ALL"
        fi
    done
fi

# 날짜 역순(최신순) 정렬
sorted_rows=$(sort -t'|' -k2 -r "$TMP_ALL")

# 날짜별로 분할된 파일 현황 생성
file_section=""
prev_date=""
while IFS= read -r line; do
    [ -z "$line" ] && continue
    cur_date=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f1)
    if [ "$cur_date" != "$prev_date" ]; then
        file_section="${file_section}
### ${cur_date}

| 시간 | 파일명 | 디렉토리 |
|:---:|:---:|:---:|
"
        prev_date="$cur_date"
    fi
    # 시간만 추출
    cur_time=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f2)
    fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
    dirpath=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
    file_section="${file_section}| ${cur_time} | ${fname} | ${dirpath} |
"
done <<< "$sorted_rows"

# 디렉토리별 요약 표
dir_summary="| sejong | ${sejong_count} |\n| swea | ${swea_count} |\n| boj | ${boj_count} |"
if [ "$other_count" -gt 0 ]; then
    dir_summary="${dir_summary}\n| 기타 | ${other_count} |"
fi

# REC.md 생성
cat > "$REC_FILE" << EOF
# REC - Repository Record

> 마지막 업데이트: ${TIMESTAMP}

---

## 디렉토리별 요약

| 디렉토리 | 총 개수 |
|:---:|:---:|
$(echo -e "$dir_summary")
| **합계** | **${total_count}** |

---

## 소스코드 파일 현황
${file_section}
EOF

# CSV 파일 저장 (날짜별 정리, 최신순)
CSV_FILE="REC.csv"
echo "날짜,시간,파일명,디렉토리" > "$CSV_FILE"
while IFS= read -r line; do
    [ -z "$line" ] && continue
    csv_date=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f1)
    csv_time=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f2)
    csv_fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
    csv_dir=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
    echo "${csv_date},${csv_time},${csv_fname},${csv_dir}" >> "$CSV_FILE"
done <<< "$sorted_rows"

echo "REC.md 업데이트 완료!"
echo "REC.csv 저장 완료!"
echo "  시간: ${TIMESTAMP}"
echo "  전체: ${total_count}개 (sejong: ${sejong_count}, swea: ${swea_count}, boj: ${boj_count})"
