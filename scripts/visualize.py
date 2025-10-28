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


if __name__ == "__main__":
    input_max_n: int = int(input("nの最大値を入力してください: "))
    visualize_probability(input_max_n)
