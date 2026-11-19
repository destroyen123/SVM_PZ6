
def min_deletions_wagner_fischer(s):
    r = s[::-1]
    n = len(s)

    d = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = i
        d[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == r[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(
                    d[i - 1][j],
                    d[i][j - 1]
                ) + 1

    return d[n][n] // 2



def restore_palindrome(s):
    n = len(s)

    if n == 0:
        return ""

    p = [[0] * n for _ in range(n)]

    for i in range(n):
        p[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                p[i][j] = p[i + 1][j - 1] + 2
            else:
                p[i][j] = max(
                    p[i + 1][j],
                    p[i][j - 1]
                )

    left, right = 0, n - 1
    first_half = []
    second_half = []

    while left <= right:
        if s[left] == s[right]:
            first_half.append(s[left])

            if left != right:
                second_half.append(s[right])

            left += 1
            right -= 1

        elif p[left + 1][right] >= p[left][right - 1]:
            left += 1
        else:
            right -= 1

    return "".join(first_half + second_half[::-1])


s = "BAADS"

count = min_deletions_wagner_fischer(s)
result = restore_palindrome(s)

print("Исходная строка:", s)
print("Обратная строка:", s[::-1])
print("Полученный палиндром:", result)
print("Минимальное количество удалений:", count)

# Матрица Вагнера — Фишера
n = len(s)
r = s[::-1]

d = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    d[i][0] = i
    d[0][i] = i

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if s[i - 1] == r[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = 1 + min(
                d[i - 1][j],
                d[i][j - 1]
            )

print("\nМатрица Вагнера — Фишера:")
print("    -", *r)

for i in range(n + 1):
    symbol = "-" if i == 0 else s[i - 1]
    print(symbol, " ", *d[i])


# Матрица восстановления палиндрома
p = [[0] * n for _ in range(n)]

for i in range(n):
    p[i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1

        if s[i] == s[j]:
            p[i][j] = p[i + 1][j - 1] + 2
        else:
            p[i][j] = max(
                p[i + 1][j],
                p[i][j - 1]
            )

print("\nМатрица восстановления палиндрома:")
print("  ", *s)

for i in range(n):
    print(s[i], *[
        p[i][j] if j >= i else "-"
        for j in range(n)
    ])
