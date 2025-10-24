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
        valid_cells = [
            (r, c)
            for r in range(game.get_board_rows())
            for c in range(game.get_board_cols())
        ]
        if not valid_cells:
            msg = "No valid cells to select."
            raise ValueError(msg)
        return random.choice(valid_cells)
