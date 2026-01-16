# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 16. 09:27:39

def solution(my_string):
    answer = ''
    lst = list(my_string)
    reversed_lst = lst[::-1]
    answer="".join(reversed_lst)
    return answer