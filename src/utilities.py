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
    result: Fraction = Fraction.__new__(Fraction)
    result._numerator = numerator  # noqa: SLF001
    result._denominator = denominator  # noqa: SLF001
    return result


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
    result: Fraction = Fraction.__new__(Fraction)
    result._numerator = numerator  # noqa: SLF001
    result._denominator = denominator  # noqa: SLF001
    return result
