# 평균 구하기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 알고리즘: 기본연산, 배열
# 작성자: 김재천
# 작성일: 2026. 01. 20. 08:47:45

def solution(arr):
    arr_sum = sum(arr)
    arr_len = len(arr)
    answer = arr_sum/arr_len
    return answer