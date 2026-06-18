import numpy as np
from scipy.stats import describe


def calculate_statistics(data: np.ndarray) -> dict[str, float]:
    """与えられたデータの基本統計量を計算する関数

    Parameters
    ----------
    data : np.ndarray
        数値データの配列

    Returns
    -------
    dict[str, float]
        基本統計量を含む辞書。キーは 'mean', 'variance', 'skewness', 'kurtosis'。

    """
    stats = describe(data)
    return {
        "mean": stats.mean,
        "variance": stats.variance,
        "skewness": stats.skewness,
        "kurtosis": stats.kurtosis,
    }
