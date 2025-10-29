import matplotlib.pyplot as plt

from src.recurrence_relation import calculate_probability


def visualize_probability(max_n: int) -> None:
    """2xnのChompにおける先手の勝率を可視化する関数。

    Parameters
    ----------
    max_n : int
        1列目のチョコレートの最大数。

    """
    ns: list[int] = list(range(1, max_n + 1))
    probabilities: list[float] = [
        calculate_probability(n, n) for n in range(1, max_n + 1)
    ]
    print(probabilities)  # デバッグ用出力

    plt.figure(figsize=(10, 6))
    plt.plot(ns, probabilities, marker="o")
    plt.title("Probability of 2xn Chomp - First Player Winning")
    plt.xlabel("Number of Chocolates in Column 1 (n)")
    plt.ylabel("First Player Winning Probability")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()


def visualize_probability_2d(max_n: int) -> None:
    """2行のChompにおける先手の勝率を2次元で可視化する関数。

    2列目のチョコレートの数(k)ごとに異なる色で表示します。

    Parameters
    ----------
    max_n : int
        1列目と2列目のチョコレートの最大数。

    """
    plt.figure(figsize=(12, 8))

    # 各kについて、nを動かして線をプロット
    for k in range(1, max_n + 1):
        n_values: list[int] = []
        prob_values: list[float] = []

        # kを固定して、nをkからmax_nまで動かす
        for n in range(k, max_n + 1):
            n_values.append(n)
            prob_values.append(calculate_probability(n, k))

        # k値ごとに異なる色で線をプロット
        plt.plot(
            n_values,
            prob_values,
            marker="o",
            label=f"k={k} (Column 2)",
            linewidth=2,
            markersize=6,
        )

    plt.xlabel("Number of Chocolates in Column 1 (n)")
    plt.ylabel("First Player Winning Probability")
    plt.title("Winning Probability in 2-row Chomp (by Column 2 size)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(visible=True, alpha=0.3)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    input_max_n: int = int(input("nの最大値を入力してください: "))
    print("2次元グラフを表示します...")
    visualize_probability_2d(input_max_n)
