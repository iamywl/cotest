#!/bin/bash

# sejong 디렉토리 내 파일들을 수정일 기준 날짜별 디렉토리로 정리하는 스크립트

DIR="$(cd "$(dirname "$0")" && pwd)"
SEJONG_DIR="$DIR/sejong"

cd "$SEJONG_DIR" || exit 1

# 현재 디렉토리의 파일들을 순회
for file in *; do
    # 디렉토리는 건너뛰기
    [ -d "$file" ] && continue

    # 파일의 수정일에서 날짜만 추출 (YYYY-MM-DD)
    date_dir=$(stat -f "%Sm" -t "%Y-%m-%d" "$file")

    # 날짜 디렉토리 생성
    mkdir -p "$date_dir"

    # 파일 이동
    mv "$file" "$date_dir/"
    echo "  $file -> $date_dir/"
done

echo "정리 완료!"
