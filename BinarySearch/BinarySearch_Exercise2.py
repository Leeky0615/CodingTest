'''
    정렬된 배열에서 특정 수의 개수 구하기
    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서
    x가 등장하는 횟수를 계산하세요. 예를 들어, {1, 1, 2, 2, 2, 2, 3}이 있을 때
    x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
    단, 이문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.

    풀이 시간 30분 / 시간제한 1초 / 메모리 제한 128MB / 기출 Zoho 인터뷰
    입력 조건. 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
              둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
    출력 조건. 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가
              하나도 없다면 -1을 출력합니다.

    입력 예시
        7 2
        1 1 2 2 2 2 3
    출력 예시
        4
'''
# 표준 라이브러리 사용
from bisect import bisect_left, bisect_right

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

count = bisect_right(array, x) - bisect_left(array, x)
if count == 0:
    print(-1)
else:
    print('값이 ', x, '인 원소의 개수 : ', count)
