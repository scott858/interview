def edit_distance(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # insert
                    dp[i - 1][j],  # remove
                    dp[i - 1][j - 1],  # replace
                )

    print(dp[m][n])


if __name__ == '__main__':
    str1 = 'food'
    m = len(str1)
    str2 = 'money'
    n = len(str2)
    edit_distance(str1, str2, m, n)
