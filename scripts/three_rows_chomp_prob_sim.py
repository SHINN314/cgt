from src.three_rows_chomp_prob import is_multiple_number


def check_prob_denominator(n: int, n1: int, n2: int, n3: int) -> None:
    """Chompの確率の分母の倍数判定を行い、結果を表示する関数。

    Parameters
    ----------
    n: int
        積のループ回数
    n1: int
        1行目のマスの個数
    n2: int
        2行目のマスの個数
    n3: int
        3行目のマスの個数

    Returns
    -------
    None

    """
    if is_multiple_number(n, n1, n2, n3):
        print(f"(n1 + n2 + n3) permutation {n} はChompの確率の分母の倍数です。 ")
    else:
        print(
            f"(n1 + n2 + n3) permutation {n}はChompの確率の分母の倍数ではありません。",
        )


if __name__ == "__main__":
    n: int = 3  # 積のループ回数
    boards = [  # (n1, n2, n3)
        (3, 3, 3),
        (3, 3, 2),
        (3, 3, 1),
        (3, 2, 2),
        (3, 2, 1),
    ]

    for n1, n2, n3 in boards:
        check_prob_denominator(n, n1, n2, n3)

    for n1, n2, n3 in boards:
        check_prob_denominator(n, n1, n2, n3)
