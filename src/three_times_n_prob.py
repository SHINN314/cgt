from fractions import Fraction


def calculate_3_row_probability(n1: int, n2: int, n3: int) -> Fraction:  # noqa: C901
    """3行のChomp盤面における確率を計算する関数

    Parameters
    ----------
    n1: int
        1行目のマスの個数
    n2: int
        2行目のマスの個数
    n3: int
        3行目のマスの個数

    Returns
    -------
    Fraction
        確率 (分数形式)

    Notes
    -----
        画像の再帰式に基づいて実装:
        1 - 1/(n1*n2*n3) * (
            Σ(i=n2 to n1-1) f(i, n2, n3) +
            Σ(i=n3 to n2-1) f(i, i, n3) +
            Σ(i=0 to n3-1) f(i, i, i) +
            Σ(i=n3 to n2-1) f(n1, i, n3) +
            Σ(i=0 to n3-1) f(n1, i, i) +
            Σ(i=0 to n3-1) f(n1, n2, i)
        )

    """
    # メモ化用の辞書
    memo = {}

    def f(a: int, b: int, c: int) -> Fraction:
        """内部関数: メモ化を用いた再帰計算

        Args:
            a: 1行目のマスの個数
            b: 2行目のマスの個数
            c: 3行目のマスの個数

        Returns:
            確率 (分数形式)

        """
        # 基底条件
        if a == 0 and b == 0 and c == 0:
            return Fraction(0)

        # メモ化チェック
        if (a, b, c) in memo:
            return memo[(a, b, c)]

        # 再帰式の計算
        total = a + b + c
        if total == 0:
            result = Fraction(0)
        else:
            sum_value = Fraction(0)

            # Σ(i=n2 to n1-1) f(i, n2, n3)
            for i in range(b, a):
                sum_value += f(i, b, c)

            # Σ(i=n3 to n2-1) f(i, i, n3)
            for i in range(c, b):
                sum_value += f(i, i, c)

            # Σ(i=0 to n3-1) f(i, i, i)
            for i in range(c):
                sum_value += f(i, i, i)

            # Σ(i=n3 to n2-1) f(n1, i, n3)
            for i in range(c, b):
                sum_value += f(a, i, c)

            # Σ(i=0 to n3-1) f(n1, i, i)
            for i in range(c):
                sum_value += f(a, i, i)

            # Σ(i=0 to n3-1) f(n1, n2, i)
            for i in range(c):
                sum_value += f(a, b, i)

            result = Fraction(1) - sum_value / total

        # メモ化
        memo[(a, b, c)] = result
        return result

    return f(n1, n2, n3)


if __name__ == "__main__":
    # テスト
    print("3行Chomp確率計算のテスト")
    print(f"f(1, 1, 1) = {calculate_3_row_probability(1, 1, 1)}")
    print(f"f(2, 2, 2) = {calculate_3_row_probability(2, 2, 2)}")
    print(f"f(3, 3, 3) = {calculate_3_row_probability(3, 3, 3)}")
    print(f"f(3, 2, 1) = {calculate_3_row_probability(3, 2, 1)}")
