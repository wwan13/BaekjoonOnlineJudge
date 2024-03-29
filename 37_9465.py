"""
DATE: 2023.04.03
QUE NUM: 9465
QUE NAME: 스티커
QUE TYPE: dynamic programming
https://www.acmicpc.net/problem/9465
"""

import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range (2)]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][n-1], dp[1][n-1]))