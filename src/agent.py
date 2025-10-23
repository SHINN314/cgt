import random

from src.chomp import Chomp


class Agent:
    """Chompのシミュレーション用のエージェントクラス。

    セルの選び方は盤面に対して一様ランダムに選択する。

    Attributes
    ----------
    name : str
        エージェントの名前。

    """

    def __init__(self, name: str) -> None:
        """Agentクラスのコンストラクタ。"""
        self.name = name

    def select_eat_cell(self, game: Chomp) -> tuple[int, int]:
        """食べるセルをランダムに選択する。

        Parameters
        ----------
        game : Chomp
            現在のChompゲームの状態。

        Returns
        -------
        tuple of int
            選択されたセルの行と列のインデックス。

        """
        row_weights: list[int] = []
        col_weights: list[int] = []
        for r in range(game.get_board_rows()):
            row_weight: int = sum(
                1 for c in range(game.get_board_cols()) if game.get_board_cell(r, c)
            )
            row_weights.append(row_weight)
        for c in range(game.get_board_cols()):
            col_weight: int = sum(
                1 for r in range(game.get_board_rows()) if game.get_board_cell(r, c)
            )
            col_weights.append(col_weight)

        select_row: int = random.choices(
            population=list(range(game.get_board_rows())),
            weights=row_weights,
            k=1,
        )[0]
        select_col: int = random.choices(
            population=list(range(game.get_board_cols())),
            weights=col_weights,
            k=1,
        )[0]
        return select_row, select_col
