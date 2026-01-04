from fractions import Fraction

from src.utilities import sub_fraction_unnormalized, sum_fraction_unnormalized


def calculate_three_row_probability(n1: int, n2: int, n3: int) -> Fraction:
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
        再帰式は以下のように表される。:
        1 - 1/(n1+n2+n3) * (
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

        Parameters
        ----------
        a: int
            1行目のマスの個数
        b: int
            2行目のマスの個数
        c: int
            3行目のマスの個数

        Returns
        -------
        Fraction
            確率 (分数形式)

        """
        # 基底条件
        if a == 0 and b == 0 and c == 0:
            return Fraction(1)

        # メモ化チェック
        if (a, b, c) in memo:
            return memo[(a, b, c)]

        # 再帰式の計算
        total = a + b + c
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

        result = Fraction(1) - Fraction(sum_value, total)

        # メモ化
        memo[(a, b, c)] = result
        return result

    return f(n1, n2, n3)


def calculate_three_row_probability_unnormalized(n1: int, n2: int, n3: int) -> Fraction:
    """3行のChomp盤面における正規化されていない確率を計算する関数

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
        正規化されていない確率 (分数形式)

    Notes
    -----
        再帰式は以下のように表される。:
        1 - 1/(n1+n2+n3) * (
            Σ(i=n2 to n1-1) f(i, n2, n3) +
            Σ(i=n3 to n2-1) f(i, i, n3) +
            Σ(i=0 to n3-1) f(i, i, i) +
            Σ(i=n3 to n2-1) f(n1, i, n3) +
            Σ(i=0 to n3-1) f(n1, i, i) +
            Σ(i=0 to n3-1) f(n1, n2, i)
        )

    """
    # メモ
    memo = {}

    def f(a: int, b: int, c: int) -> Fraction:
        """内部関数: メモ化を用いた再帰計算

        Parameters
        ----------
        a: int
            1行目のマスの個数
        b: int
            2行目のマスの個数
        c: int
            3行目のマスの個数

        Returns
        -------
        Fraction
            正規化されていない確率 (分数形式)

        """
        # 基底条件
        if a == 0 and b == 0 and c == 0:
            return Fraction(1, normalize=False)

        # メモ化チェック
        if (a, b, c) in memo:
            return memo[(a, b, c)]

        # 再帰式の計算
        total: int = a + b + c
        sum_value_numerator: int = 0
        sum_value_denominator: int = 1
        sum_value: Fraction = Fraction(
            sum_value_numerator,
            sum_value_denominator,
            normalize=False,
        )

        # Σ(i=n2 to n1-1) f(i, n2, n3)
        for i in range(b, a):
            sum_value = sum_fraction_unnormalized(sum_value, f(i, b, c))

        # Σ(i=n3 to n2-1) f(i, i, n3)
        for i in range(c, b):
            sum_value = sum_fraction_unnormalized(sum_value, f(i, i, c))

        # Σ(i=0 to n3-1) f(i, i, i)
        for i in range(c):
            sum_value = sum_fraction_unnormalized(sum_value, f(i, i, i))

        # Σ(i=n3 to n2-1) f(n1, i, n3)
        for i in range(c, b):
            sum_value = sum_fraction_unnormalized(sum_value, f(a, i, c))

        # Σ(i=0 to n3-1) f(n1, i, i)
        for i in range(c):
            sum_value = sum_fraction_unnormalized(sum_value, f(a, i, i))

        # Σ(i=0 to n3-1) f(n1, n2, i)
        for i in range(c):
            sum_value = sum_fraction_unnormalized(sum_value, f(a, b, i))

        # 確率の計算
        result: Fraction = sub_fraction_unnormalized(
            Fraction(1),
            Fraction(sum_value, total, normalize=False),
        )

        # メモ化
        memo[(a, b, c)] = result
        return result

    return f(n1, n2, n3)


def is_multiple_number(prob: Fraction, n: int, n_1: int, n_2: int, n_3: int) -> bool:
    """整数nがChompの確率の分母の倍数であるかを判定する関数。

    Parameters
    ----------
    prob: Fraction
        Chompの確率(分数形式)
    n: int
        積のループ回数
    n_1: int
        1行目のマスの個数
    n_2: int
        2行目のマスの個数
    n_3: int
        3行目のマスの個数

    Returns
    -------
    bool
        nが確率の分母の倍数であればTrue、そうでなければFalse

    Raises
    ------
    ValueError
        recurrence_denominatorが0になった場合

    """
    recurrence_denominator: int = 1
    diffed_frac = Fraction(1, 2) - prob
    diffed_denominator = diffed_frac.denominator

    for i in range(n + 1):
        recurrence_denominator *= n_1 + n_2 + n_3 - i

    if recurrence_denominator == 0:
        msg: str = "盤面を十分に大きくしてください"
        raise ValueError(msg)

    return recurrence_denominator % diffed_denominator == 0


if __name__ == "__main__":
    # テスト
    # ValueErrorが発生しないことの確認
    prob_1 = calculate_three_row_probability(3, 2, 2)
    print(is_multiple_number(prob_1, 3, 3, 2, 2))

    # ValueErrorが発生することの確認
    prob_2 = calculate_three_row_probability(1, 1, 1)
    print(is_multiple_number(prob_2, 3, 1, 1, 1))
