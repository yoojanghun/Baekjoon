import sys
input = sys.stdin.readline

def get_pi(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    return pi

L = int(input())
s = input().rstrip()
pi = get_pi(s)
print(L - pi[-1])
