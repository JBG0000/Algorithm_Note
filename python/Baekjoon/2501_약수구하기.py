N, K=map(int, input().split())  #N, K 입력받기

num_list=[]

for i in range(1, N+1, 1): #1부터 N+1까지, 1씩 증가하며 반복문 돌기
    if N%i==0:  #약수면 num_list에 추가, 배열엔 자동으로 오름차순으로 값 입력
        num_list.append(i)

if len(num_list)>=K:    #num_lest 배열 길이가 K보다 크다면, 즉 K번째로 큰 약수가 존재한다면
    print(num_list[K-1])    #배열 인덱스는 0부터 시작이므로 K번째 약수는 K-1인덱스에 존재
else:   #K개만큼 약수가 존재하지 않는다면 0출력
    print(0)