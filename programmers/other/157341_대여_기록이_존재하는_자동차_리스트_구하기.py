# 대여 기록이 존재하는 자동차 리스트 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157341
# 작성자: 김재천
# 작성일: 2026. 01. 19. 10:23:12

-- where car_type = 세단
-- and 10월 대여 시작
-- 자동차 id 컬럼
SELECT
    h.car_id
from
    car_rental_company_rental_history as h
    left join car_rental_company_car as c
    on h.car_id = c.car_id
where
    c.car_type = '세단'
    and month(h.start_date)=10
group by
    h.car_id
order by
    h.car_id desc