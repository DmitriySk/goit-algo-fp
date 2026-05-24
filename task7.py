import random
import matplotlib.pyplot as plt

def roll_dice(n):
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(n):
        counts[random.randint(1, 6) + random.randint(1, 6)] += 1

    return {s: counts[s] / n for s in range(2, 13)}

def print_table(a, mc):
    print(f"{'Сума':>5} | {'Аналітична':>14} | {'Монте-Карло':>14} | 'Відхилення'")
    print("-" * 48)
    for s in range(2, 13):
        analytical_pct = a[s] * 100
        mc_pct = mc[s] * 100
        diff = mc_pct - analytical_pct
        print(
            f"{s:>5} | {analytical_pct:>12.2f}%  | {mc_pct:>12.2f}%  | {diff:>+.4f}%"
        )

def draw_chart(a, mc):
    sums = list(range(2, 13))
    analytical_vals = [ANALYTICAL[s] * 100 for s in sums]
    mc_vals = [monte_carlo[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.4

    fig, ax = plt.subplots(figsize=(11, 6))
    bars_mc = ax.bar([i - width / 2 for i in x], mc_vals, width, label=f"Монте-Карло ({ROLLS:,} кидків)", color="#3498DB", alpha=0.85)
    bars_an = ax.bar([i + width / 2 for i in x], analytical_vals, width, label="Аналітична", color="#E74C3C", alpha=0.85)

    ax.set_xticks(list(x))
    ax.set_xticklabels(sums)
    ax.set_xlabel("Сума двох кубиків")
    ax.set_ylabel("Ймовірність, %")
    ax.set_title("Метод Монте-Карло vs Аналітичні значення\n(два кубики)")
    ax.legend()
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)

    for bar in bars_mc:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                f"{bar.get_height():.2f}%", ha="center", va="bottom", fontsize=7.5)
    for bar in bars_an:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                f"{bar.get_height():.2f}%", ha="center", va="bottom", fontsize=7.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ROLLS = 1_000_000

    ANALYTICAL = {s: c / 36 for s, c in {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1,
    }.items()}

    monte_carlo = roll_dice(ROLLS)

    print_table(ANALYTICAL, monte_carlo)
    draw_chart(ANALYTICAL, monte_carlo)
