'''
    메모이제이션
     - 다이나믹 프로그래밍을 구현하는 방법 중 하나 입니다.
     - 한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다.
       같은 문제를 다시 호출하면 메모했던 결과를 그래도 가져옵니다.
       값을 기록해 놓는다는 점에서 캐싱이라고도 합니다.

     탑다운 VS 바텀업
     탑다운(메모이제이션) 방식은 하향식이라고도 하며 재귀함수를 이용하며, 바텀업 방식은
     상향식이라고도 하고 먼저 계산했던 문제들의 값을 활용해 그다음에 문제도 해결한다.
     다이나믹 프로그래밍의 전형적인 형태는 바텀업 방식이다.
        - 결과 저장용 리스트는 DP테이블이라고도 부른다.
     엄밀히 말하면 이런 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넒은
     개념을 의미한다. 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아니며
     한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수 있다.
'''

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수를 재귀함수로 구현(탑다운)
def fibo(x):
    # 종료 조건(1혹은 2일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# 바텀업 방식
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])