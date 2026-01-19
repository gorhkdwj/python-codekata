# 중성화 여부 파악하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59409
# 작성자: 김재천
# 작성일: 2026. 01. 19. 11:36:19

-- 코드를 입력하세요
SELECT
    animal_id,
    name,
    case when sex_upon_intake like 'neutered%'
              or sex_upon_intake like 'spayed%'
              then 'O'
    else 'X'
    end as "중성화"
from
    animal_ins
order by
    animal_id asc