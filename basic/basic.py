"""
    정수형, 실수형이 가장 핵심적으로 사용된다.
    특히 정수형이 코딩테스트에서 많이 사용된다.
"""
# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 양의 실수
a = 123.23

# 음의 실수
a = -123.123

# 소수부가 0일때 0을 생략 가능
a = 5.

# 정수부가 0일때 0을 생략 가능
a = -.8

# 지수 표현 방식 -> 임의의 큰 수를 표현할때 사용됨 예를 들어 무한의 의미를 가진 큰수를 1e9로 표현 가능
# 1,000,000,000
a = 1e9
# 만약 문제에서 정수형 데이터를 처리한다고 하면 오류발생을 막기 위해 int함수를 사용
a = int(1e9)

# 752.5
a = 75.25e1

# 3.954
a = 3954e-3

'''
    컴퓨터 시스템은 실수 정보를 표현하는 정확도 측면에서 한계를 가진다.
    2진수 이기 때문에 0.3과 0.6을 더한 값인 0.9를 정확하게 표현할 수 없다.
'''
a = 0.3 + 0.6

if a == 0.9:
    print(True)
else:
    print(False)
# 결과 : False

# 이럴 때 사용하는 것이 round함수 이다.

b = round(a, 1)
if b == 0.9:
    print(True)
else:
    print(False)
# 결과 : True

'''
    나누기 연산자 : /
    나누기를 사용하면 실수형으로 반환된다.
    나머지 연산자 : %
    몫 연산자 : //
    거듭 제곱 연산자 : **
'''

'''
    파이썬의 리스트는 자바의 arraylist와 기능적으로 유사하다.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
# 4번째 원소
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 인덱스 값을 입력해서 리스트의 특정한 원소의 접근하는 것을 인덱싱이라고 한다.
a = [1, 2, 3, 4, 5, 6, 7, 8]
# -를 붙이면 뒤에서부터 접근할 수 있다.
print(a[-2])  # 뒤에서 두번째 원소

'''
    연속적인 위치를 갖는 원소를 가져올때는 슬라이싱을 사용한다.
    콜론(:)을 사용
    이 때 끝 인덱스는 +1한 값을 넣는다.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8]
#    0 1 2 3 4 5 6 7
print(a[1:4])

'''
    리스트 컴프리헨션
    대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화할 수 있다.
    또한 2차원 리스트를 초기화할 때 효과적으로 사용된다.
'''
a = [i for i in range(10)]
print(a)

# 0 부터 19 까지의 수 중에서 홀수만 포함하는 리스트
a = [i for i in range(20) if i % 2 == 1]
print(a)

# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
a = [i * i for i in range(1, 10)]
print(a)

# 2차원 리스트 초기화 좋은 예시
m = 5
n = 4
a = [[0] * m for _ in range(n)]
print(a)
# 2차원 리스트 초기화 잘못된 예시
'''
    파이썬은 리스트로 어떤 변수값을 할당하면 내부적으로 리스트는 객체형태로 처리되고
    별도의 주소값을 갖게 된다.
    그래서 어떤 리스트 객체 자체를 n번 곱하면 길이가 m인 리스트를 단순히 n번 곱한것과 같다.
     
'''
b = [[0] * m] * n
print(b)
b[1][1] = 5
print(b)
# (1,1)만 바뀌어야 되는데 다바뀌게 된다.

'''
    파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 사용한다.
    즉, 단순 반복
'''
for _ in range(5):
    print('hi')

# 특정 원소 모두 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

'''
    튜플 자료형
    소괄호를 사용하고 한 번 선언된 값을 변경할 수 없다.
    리스트에 비해 공간 활용적이다.(적은 공간)
    장점
      -> 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
         최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용
         ex) 학번, 성적 등..
      -> 해싱의 키 값으로 사용해야 할 때
         튜플은 변경이 불가능 하므로 리스트와 다르게 키 값으로 사용될 수 있다.
      -> 리스트보다 메모리를 효율적으로 사용해야 할 때 
'''

"""
    사전 자료형
    키와 값의 쌍으로 데이터를 가지는 자료형이다.
    원하는 변경 불가능한 자료형을 키로 사용한다.
    데이터의 조회 및 수정에 있어서 상수 시간 복잡도 O(1)
"""
data = dict()

data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다")

# 키와 값을 별도로 뽑아내는 함수를 지원한다.

key_list = list(data.keys())
value_list = list(data.values())
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

'''
    집합 자료형
    중복을 허용하고, 순서가 없는 자료형.
    어떤 데이터의 존재 여부를 확인할 때 유용하다.
    데이터의 조회 및 수정에 있어서 상수 시간복잡도를 가진다.
'''

data1 = set([1, 1, 2, 3, 4, 5, 5, 5])
data2 = {1, 1, 1, 2, 2, 2, 3, 4, 4, 5}
# 합(|) , 교(&), 차집합(-) 지원


'''
    input() 함수는 한 줄의 문자열을 입력 받는 함수
    map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
'''
# 데이터의 개수 입력
# n = int(input())
# print(n)

# 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))
# print(data)

# 데이터가 공백 기준으로 무조건 3개만.
# a, b, c = map(int, input().split())
# print(a,b,c)

'''
    입력을 최대한 빠르게 받아야 하는 경우
    sys.stdin.readline()을 사용한다.
    단, 엔터가 줄바꿈 기호로 입력 되므로 rstrip() 메서드를 함께 사용한다
    실제로, 이진 탐색, 정렬, 그래프 관련 문제에서 자주 사용
'''

import sys

# data = sys.stdin.readline().rstrip()
# print(data)

'''
    f-string 예제
'''
answer = 7
print(f"정답은 {answer}입니다")

