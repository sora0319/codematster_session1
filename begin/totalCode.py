''' # 내 이름 찾기
import sys
temp = (sys.stdin.readline()).split()
names = (sys.stdin.readline()).split()

print(names.index(temp[1]) + 1)
'''
'''# 정렬된 많은 원소 사이에서 특정 원소 찾기
import sys
temp = (sys.stdin.readline()).split()
nums = (sys.stdin.readline()).split()

for i, n in enumerate(nums):
    if temp[1] == n:
        print(i+1)
        break
    if i == len(nums)-1:
        print(-1)
'''
'''# 타일 깔기1
import sys
N = int(sys.stdin.readline())

tile = [0 for i in range(0,N+1)]
tile[0] = 1
tile[1] = 1
tile[2] = 2

for n in range(3,N+1):
    tile[n] = tile[n-1] + tile[n-2]

print(tile[N] % 796796)
'''
'''# 우리반 아이큐왕
import sys
N = int(sys.stdin.readline())

names = ['' for  i in range (0,3)]
IQ = [0 for i in range(0,3)]
start = 2
end = 3
for i in range (0, N):
    temp = (sys.stdin.readline()).split()
    t_IQ = int(temp[1])
    
    if IQ[0] < t_IQ:
        end = 0
    elif IQ[1] < t_IQ:
        end = 1
    elif IQ[2] < t_IQ:
        end = 2
    
    for j in range(start, end, -1):
        names[j] = names[j-1]
        IQ[j] = IQ[j-1]
    
    if end != 3:
        names[end] = temp[0]
        IQ[end] = t_IQ
    
    end = 3

for i in names:
    print(i)
'''
'''# 사전만들기
import sys

N = int(sys.stdin.readline())
eDict = ['' for i in range(0,N)]

start = 0
end = 0
for n in range(0, N):
    save = (sys.stdin.readline()).strip()
    same = 0
    for i in range(0, n+1):    
        if (len(eDict[i]) > len(save)) or (eDict[i] == ''):
            end = i
            break
        elif len(eDict[i]) == len(save):
            if eDict[i] > save:
                end = i
                break
            elif eDict[i] == save:
                same = 1
        elif (same == 1) and (len(eDict[i]) < len(save)):
            end = i-1
            break
    
    if same == 0:
        for j in range(start, end, -1):
            eDict[j] = eDict[j-1]
        eDict[end] = save
        start += 1
    
for i in eDict:
    if i != '':
        print(i)
'''
'''# 누적합
import sys
import math

N = int(sys.stdin.readline())
temp = list(map(int, (sys.stdin.readline()).split()))

if (N & (N-1)) == 0:
    deep = int(math.log(N, 2)) + 1
else:
    deep = int(math.log(N, 2)) + 2

totalNode = 2 ** (deep)
firstNode = 2 ** (deep-1)

k = 0
sumNode = []
for i in range(0, totalNode):
    if i >= firstNode and k < N:
        sumNode.append(temp[k])
        k += 1
    else:
        sumNode.append(0)


node = firstNode
n = node
while node > 1:
    sumNode[n//2] = sumNode[n] + sumNode[n+1]
    n += 2
    if n == (node  * 2):
        node = node // 2
        n = node

t = 1
for i in range(1, len(sumNode)):        
    if i == (2**t)-1:
        print(sumNode[i])
        t +=1
    else:
        print(sumNode[i], end = ' ')
'''
'''# 컴퓨터학원(자리배치)
import sys

N = int(sys.stdin.readline())
dp = [0] * (N+1)

dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
    dp[i] = dp[i-1] * 3 - (dp[i-1] - dp[i-2])

print(dp[N] % 796796)
'''
'''# You
import sys

string = sys.stdin.readline()

result = string.find('You')
if result != -1:
    print('Me')
else:
    print('No')
'''
'''# 숫자 맞추기
import sys
from collections import deque

nums = list(map(int,sys.stdin.readline().split()))

N = nums[0]
K = nums[1]
count = 0
check = False
#visit = set()

q = deque([[N]])

while N > K:
    
    Q = q.popleft()
    temp = []
    
    for T in Q:
        if T % 2 == 0 and T // 2 >= K:
            temp.append(T // 2)
        elif T % 2 == 0 and T // 2 < K:
            plus = T  + 1
            minus = T - 1
            if minus >= K:
                temp.append(minus)
            temp.append(plus)
            temp.append(T // 2)
        elif T % 2 != 0:
            plus = T  + 1
            minus = T - 1
            if minus >= K:
                temp.append(minus)
            temp.append(plus)

    temp = set(temp)
    if K in temp:
        count += 1
        check = True
        break
    
    q.append(list(temp))
    count += 1
    
    if check == True:
        break
if N  < K:
    count = K - N
print(count)
'''
'''# 조합
import sys

nums = list(map(int, (sys.stdin.readline()).split()))

A = nums[0]
B = nums[1]

n = 1

for i in range(A, (A-B), -1):
    n *= i

for i in range(2, B+1):
    n //= i

print(n)
'''
'''# 설거지 담당
import sys

num = int(sys.stdin.readline())
wash = set([1,3,5,7])

if num in wash:
    print('RUN')

else:
    print('STAY')
'''
'''# 이별 30분전
import sys

nums = list(map(int, (sys.stdin.readline()).split()))
H = nums[0]
M = nums[1]

if M >= 30:
    print(H, M-30)
else:
    if H == 0:
        H = 23
    else:
        H -= 1
    print(H, M+60-30)
'''
'''# 구름 별
import sys

num = int(sys.stdin.readline())
star = '**'
for i in range(0, num):
    print(' ' * i, end = '')
    print(star)
'''
'''# 주사위의 합
import sys

num = int(sys.stdin.readline())

for i in range(1, 7):
    if 0 < num - i <= 6:
        print(i, num-i)
'''
'''기둥세우기
import sys
from collections import deque

nums = list(map(int, (sys.stdin.readline()).split()))
length = nums[0]
width = nums[1]

floor = deque()
total = []
count = 0

for i in range(0, length):
    temp = (sys.stdin.readline()).split()
    if '0' not in set(temp):
        floor.append(i)
    total.append(temp)

for i in range(0, width):
    check = False
    for one in total:
        if one[i] == '0':
            check = True
            break
    if check == False:
        if len(floor) != 0:
            floor.popleft()
        count += 1
count += len(floor)
print(count)
'''
'''### N을 보는 시각
import sys

num = int(sys.stdin.readline())

H = 24
M = 60
total = 0

if num == 1:
    total = 12 * 60 * 60
    total += (H-12) * 15 * 60
    total += (H-12) * (M-15) * 15
elif num == 2:
    total = 6 * 60 * 60
    total += (H-6) * 15 * 60
    total += (H-6) * (M-15) * 15
elif num == 3:
    total = 3 * 60 * 60
    total += (H-3) * 15 * 60
    total += (H-3) * (M-15) * 15
elif 4<= num <= 5:
    total = 2 * 60 * 60
    total += (H-2) * 15 * 60
    total += (H-2) * (M-15) * 15
elif 6<= num <= 9:
    total = 2 * 60 * 60
    total += (H-2) * 6 * 60
    total += (H-2) * (M-6) * 6
print(total)
'''
'''# 두더지게임
import sys

count = 0
for i in range(0, 8):
    mole = (sys.stdin.readline())
    for j in range(0, 8):
        if i % 2 == 0 and j % 2 == 0 and mole[j] == 'F':
            count += 1
        if i % 2 != 0 and j % 2 != 0 and mole[j] == 'F':
            count += 1
print(count)
'''
'''#바닥공사3
import sys

N =  int(sys.stdin.readline())
stone = []

for _ in range(N):
    stone.append(list(sys.stdin.readline()))

min_sum = N * N+1

for bit in range(1<<N):
    temp = [stone[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if temp[i][j] == 'W':
                    temp[i][j] = 'B'
                else:
                    temp[i][j] = 'W'
    column_sum = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if temp[j][i] == 'W':
                count += 1
        column_sum += min(count, N - count)
    min_sum = min(min_sum, column_sum)
print(min_sum)
'''
'''# 계단 맞추기
import sys
from collections import deque

nums = list(map(int,sys.stdin.readline().split()))

N = nums[0]
K = nums[1]

gap = K - N
if gap % 3 == 0:
    print(gap // 3)
else:
    move = gap // 3
    gap = gap % 3
    move += 1
    gap = gap - 3

    while gap != 0:
        gap += 1
        move += 1
    print(move)
'''
'''# 몇번씩 나올까
import sys
from collections import deque

N = int(sys.stdin.readline())
dp = [0] * 10

for i in range(1, N+1):
    s = str(i)
    for j in range(0, 10):
        t = str(j)
        dp[j] += s.count(t)

for r in dp:
    print(r, end = ' ')
'''
'''# 가우스와 정다각형
import sys
from collections import deque

N = int(sys.stdin.readline())

if N % 3 == 0:
    N = N // 3
if N % 5 == 0:
    N = N // 5
if N % 17 == 0:
    N = N // 17
if N % 257 == 0:
    N = N // 257
if N % 65537 == 0:
    N = N // 65537

if (N&(N-1))==0:
    print('YES')
else:
    print('NO')
'''
'''# 분수를 소수로
import sys

nums = list(map(int, (sys.stdin.readline()).split()))
limit = int(sys.stdin.readline())
p = nums[0]
q = nums[1]

result = []
result.append(p//q)
result.append('.')
for i in range(1, limit+2):
    p = p % q
    p *= 10
    
    result.append(p // q)
    
for i in range(len(result)-1, 0, -1):  
    if result[i] == 10 and result[i-1] == '.':
        result[i] = 0
        result[i-2] += 1
        break
    
    if result[i] == 10:
        result[i-1] += 1
        result[i] = 0
    elif result[i] >= 5 :
        result[i-1] += 1
    else:
        break

for i in range(0, len(result)-1):
    print(result[i], end='')
'''
'''# 별찍기
import sys

n = int(sys.stdin.readline())
li = ['* *', ' * ', '* *']
s = ' '
K = 3**(n-2)

if n == 1:
    print('*')
elif n == 2:
    for i in li:
        print(i)
elif n == 3:
    for i in range(K):
        for j in range(3):
            if i % 2 == 0:
                print(li[j] +s * 3 + li[j])
            else:
                print(s * 3 + li[j] + s * 3)
elif n == 4:
    for i in range(K):
        for j in range(3):
            if 3<= i <= 5:
                print(s * K, end = '')
                if i % 2 == 0:
                    print(s * 3 + li[j] + s * 3, end='')
                else:
                    print(li[j] +s * 3 + li[j], end='')
                print(s * K)
            elif i % 2 == 0:
                print(li[j] +s * 3 + li[j], end='')
                print(s * K, end = '')
                print(li[j] +s * 3 + li[j])
            elif i % 2 != 0:
                print(s * 3 + li[j] + s * 3, end='')
                print(s * K, end = '')
                print(s * 3 + li[j] + s * 3)
elif n == 5:
    for i in range(K):
        for j in range(3):
            if  3<= i <= 5 or 21<= i <= 23:
                if i % 2 == 0:
                    print(s * 9, end = '')
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 45, end = '')
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 9)
                else:
                    print(s * 9, end = '')
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 45, end = '')
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 9)
            elif 12<= i <= 14:
                print(s * 36, end = '')
                if i % 2 == 0:
                    print(li[j] +s * 3 + li[j], end='')
                else:
                    print(s * 3 + li[j] + s * 3, end='')
                print(s * 36)
            elif 9<= i <=11 or 12<= i <=17:
                print(s * 27, end = '')
                if i % 2 != 0:
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 9, end = '')
                    print(li[j] +s * 3 + li[j], end='')
                elif i % 2 == 0:
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 9, end = '')
                    print(s * 3 + li[j] + s * 3, end='')
                print(s * 27)
            else:
                if i % 2 == 0:
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 9, end = '')
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 27, end='')
                    print(li[j] +s * 3 + li[j], end='')
                    print(s * 9, end = '')
                    print(li[j] +s * 3 + li[j])
                elif i % 2 != 0:
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 9, end = '')
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 27, end='')
                    print(s * 3 + li[j] + s * 3, end='')
                    print(s * 9, end = '')
                    print(s * 3 + li[j] + s * 3)             
'''
'''#선분
import sys

n = int(sys.stdin.readline())
print(n+n-3)
'''
'''# 조삼모사
import sys

N = int(sys.stdin.readline())
monkey = list(map(int, (sys.stdin.readline()).split()))
M = int(sys.stdin.readline())
sums = [0] * (N+1)
result = 0

monkey.sort()
for i in range(N):
    sums[i+1] = sums[i] + monkey[i]

for i in range(N-1, -1, -1):
    gap = M - sums[i+1]
    if gap >= 0:
        if N-i-1 == 0:
            print(monkey[i])
            break
        else:
            m = gap//(N-i-1)
            if m >= monkey[i]:
                print(m)
                break
'''
'''# 친척
import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
m = max(nums)

for i in range(1, m):
    if all(num % i == nums[0] % i for num in nums):
        print(i, end =' ')
        
import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
m = max(nums)


for i in range(1, m):
    save = True
    for num in nums:
        if num % i != nums[0] % i:
            save = False
            break
    if save == True:
        print(i, end =' ')
'''
'''# 카페사장 철수
import sys
from collections import deque

nums = list(map(int, (sys.stdin.readline()).split()))
N = nums[0]
M = nums[1]
store = []
visit = []

count = 0

for i in range(M):
    temp = (sys.stdin.readline()).strip()
    visit.append(temp)

visit.sort()

for i in range(M):
    in_s, out = visit[i].split()
    if len(store) == N:
        store.sort()
        if store[0] <= in_s:
            store = store[1:]
            store.append(out)
            count += 1
    else:
        store.append(out)
        count += 1
print(count)
'''
'''# 구간단속
import sys
from collections import deque

meter = int(sys.stdin.readline())
car = int(sys.stdin.readline())

start = []
end = []

for i in range(car):
    temp = (sys.stdin.readline()).strip()
    start.append(temp)
    
for i in range(car):
    temp = (sys.stdin.readline()).strip()
    end.append(temp)

start.sort()
end.sort()

for i in range(car):
    temp = start[i].split()
    temp2 = end[i].split()
    p = temp[1]
    q = temp2[1]
    
    p = list(map(int, p.split(':')))
    q = list(map(int, q.split(':')))
    
    s_check = 0
    m_check = 0
    second= 0
    minute = 0 
    hour = 0
    total = 0

    if q[2] < p[2]:
        second = q[2] + 60 - p[2]
        s_check = 1
    else:
        second = q[2] - p[2]

    if s_check == 1:
        q[1] = q[1] - 1 
    if q[1] < p[1]:
        minute = q[1] + 60 - p[1]
        m_check = 1
    else:
        minute = q[1] - p[1]

    if m_check == 1:
        q[0] = q[0] - 1 
    hour = q[0] - p[0]
    
    total = hour + minute / 60 + second /60 /60
    
    result = meter / total
    print(temp[0], int(result))
'''