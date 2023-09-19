def MatrixPlus(A, B):
    ans = [[0]*len(A[0]) for _ in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            ans[i][j] = A[i][j] + B[i][j]
    return ans


str1 = input().split()
row = eval(str1[0])
col = eval(str1[1])
A = eval(input())
B = eval(input())
C = MatrixPlus(A, B)
out = str(C)
out = out.replace(" ", "")
print(out)
