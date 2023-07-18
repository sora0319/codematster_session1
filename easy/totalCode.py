'''# 거울
import sys

N = (sys.stdin.readline())
nums = str(N).split()

print(nums[0][::-1] if nums[0][::-1] > nums[1][::-1] else nums[1][::-1])
'''
''' # 세로행렬
# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())

for i in range (1, N+1):
    for j in range (0, N):
        print(i + j * N, end = ' ')
    print()
'''
'''# 자리수 처리하기
import sys

num = int(sys.stdin.readline())

string_num = str(num)[::-1]

n_sum = 0
for i in string_num:
    n_sum += int(i)

print(int(string_num))
print(n_sum)
'''
''' # 비밀번호 찾기
import sys

hint = (sys.stdin.readline())

for word in hint:
    if word == 'c':
        print(word, end = '')
        break
    else:
        print(word, end = '')
'''
''' # 등차수열
import sys

hint = (sys.stdin.readline())

sequence = hint.split(' ')

print(int(sequence[0]) + int(sequence[1]) * (int(sequence[2]) - 1))
'''
''' # 8진수, 
import sys

num = int(sys.stdin.readline())

octal_n = ''
hexadecimal_n = ''
N = num
while N != 0:
    octal = N % 8
    octal_n = str(octal) + octal_n
    N = N // 8

N = num
while N != 0:
    hxd = N % 16
    if hxd >= 10 and hxd <= 15:
        hexadecimal_n = chr(hxd + 55) + hexadecimal_n
    else:
        
        hexadecimal_n = str(hxd) + hexadecimal_n
    N = N // 16

print(octal_n + " " + hexadecimal_n)
'''
''' #아이디 만들기
import sys

Id = (sys.stdin.readline())

print('P' if len(Id) <= 20 else 'I')
'''
''' 나머지 비교
import sys

num = int (sys.stdin.readline())

five = num % 5
seven = num % 7

print(five if five > seven else seven)
'''
''' # 1등급 한우
import sys

num = int (sys.stdin.readline())

if num >= 200:
    print('A')
elif num >= 180:
    print('B')
elif num >= 150:
    print('C')
else:
    print('D')
'''
'''# 자녀의 키
import sys

num = (sys.stdin.readline())
parent = num.split()
parent = list(map(int, parent))
print(sum(parent) // 2)
'''
''' # 삼각형 조건
import sys

num = (sys.stdin.readline())
angle = num.split()
angle = list(map(int, angle))
print('P' if sum(angle) == 180 else 'F')
'''
''' # 기억상실
import sys

num = (sys.stdin.readline())
count = num.split()
count = list(map(int, count))

gap = count[0] - count[1]
day = 1
while True:
    if gap * (day - 1) + count[0] >= count[2]:
        break
    else:
        day += 1
print(day)
'''
'''# 림보게임
import sys

N = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))

for i, h in enumerate(height):
    if h <= 160:
        print(f'I {h}')
        break
    if i == (N-1):
        print('P')
'''
'''# 원의 넓이
import sys

r = int(sys.stdin.readline())
size = r*r*3.14
if r % 10 == 0:
    print("{:.0f}".format(size))
else:
    print(size)
'''
'''# 최대공약수
import sys

nums = list(map(int, sys.stdin.readline().split()))
if nums[0] > nums[1]:
    min = nums[1]
    max = nums[0]
else:
    min = nums[0]
    max = nums[1]

start = min
while True:
    if min % start == 0 and max % start == 0:
        print(start)
        break
    start -= 1
'''
'''# 소수 구하기
import sys

N = int(sys.stdin.readline())

prime = 0
for i in range(2,N+1):
    check = 0
    for j in range(2, i-1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        prime += 1

print(prime)
'''
'''# 3인 체조경기
import sys

nums = list(map(int, (sys.stdin.readline().split())))
gap1 = nums[1] - nums[0] -1
gap2 = nums[2] - nums[1] -1
print(gap1 if gap1 > gap2 else gap2)
'''
'''# 문자 k 찾기
import sys

print((sys.stdin.readline()).count('k'))
'''