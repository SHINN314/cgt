class Chomp:
    """Chompの盤面に関するクラス。

    Attributes
    ----------
    board : list of list of bool
        盤面の状態を表す2次元リスト。Trueは食べられていない部分、Falseは食べられた部分を示す。

    """

    def __init__(self, row: int, col: int) -> None:
        """Chompクラスのコンストラクタ。"""
        self.board = [[True for _ in range(col)] for _ in range(row)]

    def eat(self, row: int, col: int) -> None:
        """指定された位置から右下の部分を食べる。

        Parameters
        ----------
        row : int
            食べ始める行のインデックス。
        col : int
            食べ始める列のインデックス。

        """
        for r in range(row, len(self.board)):
            for c in range(col, len(self.board[r])):
                self.board[r][c] = False

    def is_game_over(self) -> bool:
        """ゲームが終了しているかどうかを判定する。

        Returns
        -------
        bool
            ゲームが終了している場合はTrue、そうでない場合はFalse。

        """
        return not self.board[0][0]

    def display(self) -> None:
        """盤面の状態を表示する。"""
        for row in self.board:
            print(" ".join(["O" if cell else "X" for cell in row]))
        print()
