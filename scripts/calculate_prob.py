from fractions import Fraction

from src.recurrence_relation import calculate_probability_fraction

if __name__ == "__main__":
    n: int = int(input("1行目のチョコレートの数を入力してください: "))
    k: int = int(input("2行目のチョコレートの数を入力してください: "))
    probability: Fraction = calculate_probability_fraction(n, k)
    print(
        f"2行のChompにおける({n}, {k})の先手の勝率は {probability} です。",
    )
