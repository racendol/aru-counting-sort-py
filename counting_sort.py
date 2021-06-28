def counting_sort(lst):
    n = len(lst)
    i = 0
    j = 0
    k = max(lst)
    A = lst
    B = [None] * n
    C = [None] * (k+1)

    while i <= k:
        C[i] = 0
        i = i + 1
        
    while j < n:
        C[A[j]] = C[A[j]] + 1
        j = j + 1

    i = 1
    j = n - 1
    while i <= k:
        C[i] = C[i] + C[i - 1]
        i = i + 1
        
    while j >= 0:
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
        j = j - 1
        
    return B
