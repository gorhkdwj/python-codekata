# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 22. 09:32:05

# 반복문으로 리스트를 돌면서, 각 값의 대소관계를 비교한다.

def solution(numbers):
    answer = 0
    fir = 0
    sec = 0
    for i in numbers:
        if i >= fir :
            sec = fir
            fir = i
        else:
            if i > sec :
                sec = i
    answer = fir * sec
    return answer