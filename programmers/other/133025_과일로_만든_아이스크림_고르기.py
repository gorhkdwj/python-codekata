# 과일로 만든 아이스크림 고르기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133025
# 작성자: 김재천
# 작성일: 2026. 01. 19. 10:34:01

-- 코드를 입력하세요
SELECT
    i.flavor
from
    icecream_info as i
    left join first_half as f
    on f.flavor = i.flavor
where
    ingredient_type = 'fruit_based'
group by
    i.flavor
having
    sum(total_order) > 3000
order by
    sum(total_order) desc;