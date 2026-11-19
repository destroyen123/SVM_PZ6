field = [
    [0, 5, 0, 1, 2],
    [1, "#", 4, 3, 1],
    [2, 3, 2, "#", 0],
    [4, 1, "#", 5, 2],
    [0, 2, 4, 1, 6]
]

print("Исходный лабиринт (вариант 9):")

for row in field:
    for cell in row:
        print(f"{cell:>3}", end=" ")
    print()

print("\nСтарт: (1, 1)")
print("Финиш: (5, 5)")
print("Разрешённые движения: вправо и вниз")


# Таблица динамического программирования

def solve_maze(field):
    n = len(field)
    dp = [[None] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if field[i][j] == "#":
                continue

            if i == 0 and j == 0:
                dp[i][j] = field[i][j]
                continue

            candidates = []

            if i > 0 and dp[i - 1][j] is not None:
                candidates.append((dp[i - 1][j], (i - 1, j)))

            if j > 0 and dp[i][j - 1] is not None:
                candidates.append((dp[i][j - 1], (i, j - 1)))

            if not candidates:
                continue

            best_value, best_cell = max(
                candidates, key=lambda item: item[0]
            )

            dp[i][j] = best_value + field[i][j]
            parent[i][j] = best_cell

    if dp[n - 1][n - 1] is None:
        return None, [], dp

    path = []
    i, j = n - 1, n - 1

    while True:
        path.append((i + 1, j + 1))

        if i == 0 and j == 0:
            break

        i, j = parent[i][j]

    path.reverse()
    return dp[n - 1][n - 1], path, dp


maximum, path, dp = solve_maze(field)

print("Таблица динамического программирования:")
for row in dp:
    print(row)

if maximum is None:
    print("Маршрут до выхода отсутствует.")
else:
    print("Максимум драгоценностей:", maximum)
    print("Оптимальный маршрут:")
    for cell in path:
        print(cell)

if maximum is not None:
    moves = ""
    total = 0

    for i, j in path:
        total += field[i - 1][j - 1]

    for k in range(1, len(path)):
        if path[k][0] > path[k - 1][0]:
            moves += "D"
        else:
            moves += "R"

    print("\nМаршрут:", moves)
    print("Проверка суммы:", total)
    print("Результат совпадает:", total == maximum)
