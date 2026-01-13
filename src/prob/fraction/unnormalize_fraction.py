class UnnormalizeFraction:
    """正規化しない分数クラス。

    Attributes
    ----------
    numerator : int
        分子
    denominator : int
        分母

    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """クラスの初期化関数。"""
        self.numerator = numerator
        self.denominator = denominator

    def show_fraction(self) -> None:
        """分数を表示する関数。"""
        print(f"{self.numerator}/{self.denominator}")
