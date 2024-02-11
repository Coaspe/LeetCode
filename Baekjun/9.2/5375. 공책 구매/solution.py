import sys

input = sys.stdin.readline

T = int(input())
inf = 10**9

for _ in range(T):
    N, M = map(int, input().split())

    shop = []
    # dp[i] = i개 샀을 때 최소 비용
    dp = [inf] * (N + 1)
    dp[0] = 0
    ans = inf

    for _ in range(M):
        shop.append(list(map(int, input().split())))

    # 단가가 가장 낮은 쇼핑몰부터
    shop.sort(key=lambda x: x[1])

    # 몇개, 비용, 배송
    # 한 가게에 대해서 이전에 이미 몇개 샀는지 다 수행해본다.
    for s, p, o in shop:
        # j -> 몇 개 샀는가?
        for j in range(N, -1, -1):
            if j + s >= N:
                ans = min(ans, dp[j] + (N - j) * p + o)
            if j >= s:
                dp[j] = min(dp[j], dp[j - s] + s * p + o)

    print(ans)
