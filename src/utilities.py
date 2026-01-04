from fractions import Fraction


def sum_fraction_unnormalized(f: Fraction, g: Fraction) -> Fraction:
    """正規化を行わない分数の和を計算する。

    Args:
        f (Fraction): 分数f
        g (Fraction): 分数g

    Returns:
        Fraction: f + gの結果(正規化なし)

    """
    numerator = f.numerator * g.denominator + g.numerator * f.denominator
    denominator = f.denominator * g.denominator
    return Fraction(numerator, denominator, normalize=False)


def sub_fraction_unnormalized(f: Fraction, g: Fraction) -> Fraction:
    """正規化を行わない分数の差を計算する。

    Args:
        f (Fraction): 分数f
        g (Fraction): 分数g

    Returns:
        Fraction: f - gの結果(正規化なし)

    """
    numerator = f.numerator * g.denominator - g.numerator * f.denominator
    denominator = f.denominator * g.denominator
    return Fraction(numerator, denominator, normalize=False)
