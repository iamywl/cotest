#!/bin/bash

# 모든 변경사항을 커밋하고 푸쉬하는 스크립트

cd "$(dirname "$0")" || exit 1

# 변경사항 확인
if [ -z "$(git status --porcelain)" ]; then
    echo "변경사항이 없습니다."
    exit 0
fi

# 커밋 메시지 (인자로 받거나 기본값 사용)
MSG="${1:-auto commit}"

git add -A
git commit -m "$MSG"
git push

echo "푸쉬 완료!"
