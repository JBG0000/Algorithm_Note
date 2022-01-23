import sys
sys.setrecursionlimit(10 ** 6)
#깊이 탐색시 파이썬 깊이는 얕기떄문에 위 코드 입력하여 범위를 넓게 지정


###찾은 자료 1###
# def append_star(LEN):
#     if LEN == 1: return ['*']   #1일시 * 출력
#     Stars = append_star(LEN // 3)   #이전 거듭제곱 시의 코드 : LEN이 9라면 3, LEN이 27이라면 9일때의 출력
#     L = []  #출력할 완성된 별
#     for S in Stars: L.append(S * 3) #.append(x) : 리스트 끝에 x원소 그대로 추가 -> 이경우엔 stars를 세배해서 이어붙임
#     for S in Stars: L.append(S + ' ' * (LEN // 3) + S)
#     for S in Stars: L.append(S * 3)
#     return L    #출력할 완성된 별
#
# n = int(sys.stdin.readline().strip())   #입력받는 방식
# print('\n'.join(append_star(n)))    #join(리스트) : 문자열 합치기


### 찾은자료 2 ###
def get_stars(n):
    # 출력할 완성된 별
    Temp = []
    for i in range(3 * len(n)):
        # n(즉 len(stars))이 3으로 나누어 떨어지지 않는다면(1이 남는다면) 가운데 공백을 줌(n의 길이 만큼)
        if i // len(n) == 1:
            Temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])

        # n이 3으로 나누어 떨어진다면, 공백 없이 가득 채움
        else:
            Temp.append(n[i % len(n)] * 3)

    return Temp


stars = ["***", "* *", "***"]
n = int(input())    #입력
k = 0

# 만약 n이 3이 될 때 까지 n은 3으로 나눠준 값을 다시 n값으로 지정하고 k 1씩 추가
while n != 3:
    n = int(n / 3)

    # k는 함수를 몇번 실행할지 정하는 변수 : 3의 거듭제곱 수
    k += 1

for i in range(k):
    stars = get_stars(stars)    #거듭제곱만큼 반복
for i in stars:
    print(i)