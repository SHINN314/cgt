import numpy as np

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
        # 盤面からTrue(食べられる)セルの位置を取得
        board = game.get_board()
        valid_positions = np.argwhere(board)

        if len(valid_positions) == 0:
            msg = "No valid cells to select."
            raise ValueError(msg)

        # ランダムに1つ選択
        rng = np.random.default_rng()
        idx = rng.integers(len(valid_positions))
        row, col = valid_positions[idx]
        return int(row), int(col)
