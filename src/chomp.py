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

    def get_board(self) -> list[list[bool]]:
        """盤面の状態を取得する。

        Returns
        -------
        list of list of bool
            盤面の状態を表す2次元リスト。

        """
        return self.board

    def get_board_rows(self) -> int:
        """盤面の行数を取得する。

        Returns
        -------
        int
            盤面の行数。

        """
        return len(self.board)

    def get_board_cols(self) -> int:
        """盤面の列数を取得する。

        Returns
        -------
        int
            盤面の列数。

        """
        return len(self.board[0]) if self.board else 0

    def get_board_cell(self, row: int, col: int) -> bool:
        """指定された位置の盤面の状態を取得する。

        Parameters
        ----------
        row : int
            行のインデックス。
        col : int
            列のインデックス。

        Returns
        -------
        bool
            指定された位置が食べられていない場合はTrue、食べられている場合はFalse。

        """
        if row < 0 or row >= self.get_board_rows():
            msg: str = "行のインデックスが範囲外です"
            raise IndexError(msg)
        if col < 0 or col >= self.get_board_cols():
            msg: str = "列のインデックスが範囲外です"
            raise IndexError(msg)
        return self.board[row][col]

    def get_row_cell_count(self, row: int) -> int:
        """指定された行の残っているセルの数を取得する。

        Parameters
        ----------
        row : int
            行のインデックス。

        Returns
        -------
        int
            指定された行の残っているセルの数。

        """
        if row < 0 or row >= self.get_board_rows():
            msg: str = "行のインデックスが範囲外です"
            raise IndexError(msg)
        return len(self.board[row]) - self.board[row].count(False)

    def get_col_cell_count(self, col: int) -> int:
        """指定された列の残っているセルの数を取得する。

        Parameters
        ----------
        col : int
            列のインデックス。

        Returns
        -------
        int
            指定された列の残っているセルの数。

        """
        if col < 0 or col >= self.get_board_cols():
            msg: str = "列のインデックスが範囲外です"
            raise IndexError(msg)
        return sum(1 for row in self.board if row[col])

    def eat(self, row: int, col: int) -> None:
        """指定された位置から右下の部分を食べる。

        Parameters
        ----------
        row : int
            食べ始める行のインデックス。
        col : int
            食べ始める列のインデックス。

        """
        if row < 0 or row >= self.get_board_rows():
            msg: str = "行のインデックスが範囲外です"
            raise IndexError(msg)
        if col < 0 or col >= self.get_board_cols():
            msg: str = "列のインデックスが範囲外です"
            raise IndexError(msg)
        for r in range(row, len(self.board)):
            for c in range(col, len(self.board[r])):
                self.board[r][c] = False

    def is_empty_board(self) -> bool:
        """盤面が空であるかどうかを判定する。

        Returns
        -------
        bool
            盤面が空である場合はTrue、そうでない場合はFalse。

        """
        return not self.board[0][0]

    def is_eatable_cell(self, row: int, col: int) -> bool:
        """指定された位置のセルが食べられるかどうかを判定する。

        Parameters
        ----------
        row : int
            行のインデックス。
        col : int
            列のインデックス。

        Returns
        -------
        bool
            指定された位置のセルが食べられる場合はTrue、そうでない場合はFalse。

        """
        if row < 0 or row >= self.get_board_rows():
            msg: str = "行のインデックスが範囲外です"
            raise IndexError(msg)
        if col < 0 or col >= self.get_board_cols():
            msg: str = "列のインデックスが範囲外です"
            raise IndexError(msg)
        return self.board[row][col]

    def display(self) -> None:
        """盤面の状態を表示する。"""
        # 列のインデックスを表示
        col_count = len(self.board[0]) if self.board else 0
        print("   " + " ".join(str(i) for i in range(col_count)))

        # 各行を行インデックスと共に表示
        for i, row in enumerate(self.board):
            print(f"{i}: " + " ".join(["O" if cell else "X" for cell in row]))
        print()
