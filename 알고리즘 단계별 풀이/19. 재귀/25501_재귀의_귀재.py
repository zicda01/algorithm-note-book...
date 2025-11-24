import sys
sys.stdin = open("input.txt", "r")

def recursion(s, l, r, Count):
    if l >= r: return 1, Count
    elif s[l] != s[r]: return 0, Count
    else: return recursion(s, l+1, r-1, Count + 1)

def isPalindrome(s, Count):
    return recursion(s, 0, len(s)-1, Count)

N = int(input())
for _ in range(N):
    word = input()

    print(*isPalindrome(word, 1))