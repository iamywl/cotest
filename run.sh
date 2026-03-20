#!/bin/bash
# ============================================================
#  코딩테스트 저장소 통합 관리 스크립트
#  사용법:
#    ./run.sh          → 전체 실행 (정리 → 기록 → 커밋&푸시)
#    ./run.sh organize → 파일 날짜별 정리만
#    ./run.sh update   → REC.md / REC.csv 업데이트만
#    ./run.sh push     → git add → commit → push만
#    ./run.sh "메시지"  → 전체 실행 + 커밋 메시지 지정
# ============================================================

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# ─────────────── 1. 파일 정리 (organize) ───────────────
do_organize() {
    echo "========================================="
    echo "  [organize] 파일 날짜별 정리"
    echo "========================================="

    for target in sejong swea boj; do
        TARGET_DIR="$DIR/$target"
        [ -d "$TARGET_DIR" ] || continue

        cd "$TARGET_DIR" || continue
        moved=0

        for file in *; do
            [ -d "$file" ] && continue
            date_dir=$(stat -f "%Sm" -t "%Y-%m-%d" "$file")
            mkdir -p "$date_dir"
            mv "$file" "$date_dir/"
            echo "  [$target] $file -> $date_dir/"
            moved=$((moved + 1))
        done

        if [ "$moved" -eq 0 ]; then
            echo "  [$target] 정리할 파일 없음"
        else
            echo "  [$target] ${moved}개 파일 정리 완료"
        fi
        cd "$DIR"
    done
    echo ""
}

# ─────────────── 2. REC 업데이트 (update) ───────────────
do_update() {
    echo "========================================="
    echo "  [update] REC.md / REC.csv 업데이트"
    echo "========================================="

    REC_FILE="$DIR/REC.md"
    CSV_FILE="$DIR/REC.csv"
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

    TMP_CURRENT=$(mktemp)
    TMP_ALL=$(mktemp)
    trap "rm -f $TMP_CURRENT $TMP_ALL" EXIT

    cd "$DIR"

    # 소스코드 파일 목록 수집
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

    # 파일 카운트
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

    # 이전 기록 병합
    cp "$TMP_CURRENT" "$TMP_ALL"
    if [ -f "$REC_FILE" ]; then
        grep -E '^\| [0-9]{4}-' "$REC_FILE" | while IFS= read -r line; do
            fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
            dirpath=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
            if ! grep -q "| ${fname} | ${dirpath} |" "$TMP_CURRENT" 2>/dev/null; then
                echo "$line" >> "$TMP_ALL"
            fi
        done
    fi

    sorted_rows=$(sort -t'|' -k2 -r "$TMP_ALL")

    # 날짜별 파일 현황
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
        cur_time=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f2)
        fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
        dirpath=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
        file_section="${file_section}| ${cur_time} | ${fname} | ${dirpath} |
"
    done <<< "$sorted_rows"

    dir_summary="| sejong | ${sejong_count} |\n| swea | ${swea_count} |\n| boj | ${boj_count} |"
    [ "$other_count" -gt 0 ] && dir_summary="${dir_summary}\n| 기타 | ${other_count} |"

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

    echo "날짜,시간,파일명,디렉토리" > "$CSV_FILE"
    while IFS= read -r line; do
        [ -z "$line" ] && continue
        csv_date=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f1)
        csv_time=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $2); print $2}' | cut -d' ' -f2)
        csv_fname=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}')
        csv_dir=$(echo "$line" | awk -F'|' '{gsub(/^ +| +$/, "", $4); print $4}')
        echo "${csv_date},${csv_time},${csv_fname},${csv_dir}" >> "$CSV_FILE"
    done <<< "$sorted_rows"

    echo "  REC.md 업데이트 완료"
    echo "  REC.csv 저장 완료"
    echo "  전체: ${total_count}개 (sejong: ${sejong_count}, swea: ${swea_count}, boj: ${boj_count})"
    echo ""
}

# ─────────────── 3. Git Push ───────────────
do_push() {
    echo "========================================="
    echo "  [push] Git 커밋 & 푸시"
    echo "========================================="

    cd "$DIR"

    if [ -z "$(git status --porcelain)" ]; then
        echo "  변경사항이 없습니다."
        return
    fi

    local msg="${1:-auto commit}"
    git add -A
    git commit -m "$msg"
    git push

    echo "  푸시 완료!"
    echo ""
}

# ─────────────── 메인 ───────────────
case "$1" in
    organize)
        do_organize
        ;;
    update)
        do_update
        ;;
    push)
        do_push "$2"
        ;;
    *)
        # 인자가 없거나 커밋 메시지인 경우 → 전체 실행
        do_organize
        do_update
        do_push "$1"
        echo "========================================="
        echo "  전체 완료!"
        echo "========================================="
        ;;
esac
