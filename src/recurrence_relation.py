import math
from fractions import Fraction

import numpy as np


def calculate_mutual_recurrence_relation(k: int) -> np.ndarray:
    """相互再帰関係を計算する関数。

    Parameters
    ----------
    k : int
        再帰関係の深さ。

    Returns
    -------
    list of int
        計算された相互再帰関係のリスト。

    """
    if k < 1:
        msg: str = "kは1以上の整数でなければなりません。"
        raise ValueError(msg)

    recurrent_vector: np.ndarray = np.zeros(2, dtype=int)
    recurrent_vector[0] = 1
    recurrent_vector[1] = -1

    for i in range(1, k):
        operator = np.array(
            [[i * (4 * i + 1), 1], [-i * (i + 1), 4 * i**2 - i - 1]],
            dtype=int,
        )
        recurrent_vector = np.dot(operator, recurrent_vector)

    return recurrent_vector


def calculate_mutual_recurrence_relation_fraction(k: int) -> Fraction:
    """相互再帰関係を分数型で計算する関数。

    Parameters
    ----------
    k : int
        再帰関係の深さ。

    Returns
    -------
    Fraction
        計算された相互再帰関係の分数型。

    """
    if k < 1:
        msg: str = "kは1以上の整数でなければなりません。"
        raise ValueError(msg)

    recurrent_vector: list[Fraction] = [Fraction(1), Fraction(-1)]

    for i in range(1, k):
        a11 = Fraction(i * (4 * i + 1))
        a12 = Fraction(1)
        a21 = Fraction(-i * (i + 1))
        a22 = Fraction(4 * i**2 - i - 1)

        new_recurrent_vector_0 = a11 * recurrent_vector[0] + a12 * recurrent_vector[1]
        new_recurrent_vector_1 = a21 * recurrent_vector[0] + a22 * recurrent_vector[1]

        recurrent_vector[0] = new_recurrent_vector_0
        recurrent_vector[1] = new_recurrent_vector_1

    return recurrent_vector[0] / recurrent_vector[1]


def calculate_probability(n: int, k: int) -> float:
    """2行のChompにおいて一様ランダムに手を打ったときの先手の勝率を求める関数。

    Parameters
    ----------
    n: int
        1行目のチョコレートの数。
    k: int
        2行目のチョコレートの数。

    Returns
    -------
    float
        先手の勝率。

    """
    recurrence_relation: np.ndarray = calculate_mutual_recurrence_relation(k)
    a_k: int = recurrence_relation[0]
    b_k: int = recurrence_relation[1]
    winning_probability: float = 0.5 - (n * a_k + b_k) / (
        math.factorial(2 * (k - 1)) * (n + k) * (n + k - 1) * (n + k - 2)
    )
    return winning_probability


def calculate_probability_fraction(n: int, k: int) -> Fraction:
    """2行のChompにおいて一様ランダムに手を打ったときの先手の勝率を分数型で求める関数。

    Parameters
    ----------
    n: int
        1行目のチョコレートの数。
    k: int
        2行目のチョコレートの数。

    Returns
    -------
    Fraction
        先手の勝率。

    """
    recurrence_relation: np.ndarray = calculate_mutual_recurrence_relation(k)
    a_k: int = recurrence_relation[0]
    b_k: int = recurrence_relation[1]

    numerator: Fraction = Fraction(1, 2) * Fraction(
        math.factorial(2 * (k - 1)) * (n + k) * (n + k - 1) * (n + k - 2),
    ) - Fraction(n * a_k + b_k)

    denominator: Fraction = Fraction(
        math.factorial(2 * (k - 1)) * (n + k) * (n + k - 1) * (n + k - 2),
    )

    winning_probability: Fraction = numerator / denominator
    return winning_probability
