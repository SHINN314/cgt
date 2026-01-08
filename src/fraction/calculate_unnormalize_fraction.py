from src.fraction.unnormalize_fraction import UnnormalizeFraction


def add_fraction(
    frac1: UnnormalizeFraction,
    frac2: UnnormalizeFraction,
) -> UnnormalizeFraction:
    """2つの分数を加算する関数。

    Parameters
    ----------
    frac1 : Fraction
        分数1
    frac2 : Fraction
        分数2

    Returns
    -------
    Fraction
        加算結果の分数

    """
    numerator = (
        frac1.numerator * frac2.denominator + frac2.numerator * frac1.denominator
    )
    denominator = frac1.denominator * frac2.denominator
    return UnnormalizeFraction(numerator, denominator)


def sub_fraction(
    frac1: UnnormalizeFraction,
    frac2: UnnormalizeFraction,
) -> UnnormalizeFraction:
    """2つの分数を減算する関数。

    Parameters
    ----------
    frac1 : Fraction
        分数1
    frac2 : Fraction
        分数2

    Returns
    -------
    Fraction
        減算結果の分数

    """
    numerator = (
        frac1.numerator * frac2.denominator - frac2.numerator * frac1.denominator
    )
    denominator = frac1.denominator * frac2.denominator
    return UnnormalizeFraction(
        numerator,
        denominator,
    )


def mul_fraction(
    frac1: UnnormalizeFraction,
    frac2: UnnormalizeFraction,
) -> UnnormalizeFraction:
    """2つの分数を乗算する関数。

    Parameters
    ----------
    frac1 : Fraction
        分数1
    frac2 : Fraction
        分数2

    Returns
    -------
    Fraction
        乗算結果の分数

    """
    numerator = frac1.numerator * frac2.numerator
    denominator = frac1.denominator * frac2.denominator
    return UnnormalizeFraction(
        numerator,
        denominator,
    )


def div_fraction(
    frac1: UnnormalizeFraction,
    frac2: UnnormalizeFraction,
) -> UnnormalizeFraction:
    """2つの分数を除算する関数。

    Parameters
    ----------
    frac1 : Fraction
        分数1
    frac2 : Fraction
        分数2

    Returns
    -------
    Fraction
        除算結果の分数

    """
    numerator = frac1.numerator * frac2.denominator
    denominator = frac1.denominator * frac2.numerator
    return UnnormalizeFraction(
        numerator,
        denominator,
    )
