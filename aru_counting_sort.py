import math

def aru_counting_sort(lst):
    i = 0
    j = 0 
    k = max(lst)
    m = math.ceil(math.sqrt(k))
    n = len(lst)

    A = lst
    B = [None] * n
    Q = [None] * (m+1)
    R = [None] * (m+1)

    while i <= m:
        Q[i] = 0
        R[i] = 0
        i = i + 1

    while j < n:
        Q[A[j]//m] = Q[A[j]//m] + 1
        R[A[j]%m] = R[A[j]%m] + 1
        j = j + 1

    i = 1
    while i <= m:
        Q[i] = Q[i] + Q[i - 1]
        R[i] = R[i] + R[i - 1]
        i = i + 1

    j = n - 1
    while j >= 0:
        d = A[j]%m
        R[d] = R[d] - 1
        B[R[d]] = A[j]
        j = j - 1

    i = n - 1
    while i >= 0:
        d = B[i]//m
        Q[d] = Q[d] - 1
        A[Q[d]] = B[i]
        i = i - 1

    return A