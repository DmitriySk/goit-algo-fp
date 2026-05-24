items_data = {
    "pizza":      {"cost": 50, "calories": 300},
    "hamburger":  {"cost": 40, "calories": 250},
    "hot-dog":    {"cost": 30, "calories": 200},
    "pepsi":      {"cost": 10, "calories": 100},
    "cola":       {"cost": 15, "calories": 220},
    "potato":     {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: dict, budget: int) -> tuple[int, list[str]]:
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )

    total_calories = 0
    chosen = []

    for name, data in sorted_items:
        if budget >= data["cost"]:
            budget -= data["cost"]
            total_calories += data["calories"]
            chosen.append(name)

    return total_calories, chosen


def dynamic_programming(items: dict, budget: int) -> tuple[int, list[str]]:
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if costs[i - 1] <= w:
                with_item = dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                if with_item > dp[i][w]:
                    dp[i][w] = with_item

    chosen = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]

    return dp[n][budget], chosen


MAX_BUDGET = 100

greedy_calories, greedy_items = greedy_algorithm(items_data, MAX_BUDGET)
print("=== Жадібний алгоритм ===")
print(f"Бюджет: {MAX_BUDGET} грн")
print(f"Обрані страви: {greedy_items}")
print(f"Загальна калорійність: {greedy_calories} ккал")

print()

dp_calories, dp_items = dynamic_programming(items_data, MAX_BUDGET)
print("=== Динамічне програмування ===")
print(f"Бюджет: {MAX_BUDGET} грн")
print(f"Обрані страви: {dp_items}")
print(f"Загальна калорійність: {dp_calories} ккал")
