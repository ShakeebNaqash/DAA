def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

def lcs_memo(X, Y):
    m, n = len(X), len(Y)
    memo = [[-1]*(n+1) for _ in range(m+1)]

    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if X[i-1] == Y[j-1]:
            memo[i][j] = 1 + dp(i-1, j-1)
        else:
            memo[i][j] = max(dp(i-1, j), dp(i, j-1))
        return memo[i][j]

    dp(m, n)

    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i =i-1
            j =j-1
        elif memo[i-1][j] > memo[i][j-1]:
            i =i-1
        else:
            j =j-1
    return memo[m][n], ''.join(reversed(lcs_str))

if __name__ == "__main__":
    X = input("Enter first string: ")
    Y = input("Enter second string: ")
    print("LCS length (recursive):", lcs_recursive(X, Y, len(X), len(Y)))
    length, lcs_str = lcs_memo(X, Y)
    print("LCS length (DP with memoization):", length)
    print("LCS string:", lcs_str)