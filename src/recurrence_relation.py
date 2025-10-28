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
    if k < 0:
        msg: str = "kは0以上の整数でなければなりません。"
        raise ValueError(msg)

    recurrent_vector: np.ndarray = np.zeros(2, dtype=int)
    recurrent_vector[0] = 1
    recurrent_vector[1] = -1

    for _ in range(k - 1):
        operator = np.array(
            [[k * (4 * k + 1), 1], [-k * (k + 1), 4 * k**2 - k - 1]],
            dtype=int,
        )
        recurrent_vector = np.dot(operator, recurrent_vector)

    return recurrent_vector
