from src.agent import Agent
from src.chomp import Chomp


def simulate_game(simulation_count: int, board_rows: int, board_cols: int) -> float:
    """Chompゲームのシミュレーションを実行する関数。

    Parameters
    ----------
    simulation_count : int
        シミュレーションの回数。
    board_rows : int
        盤面の行数。
    board_cols : int
        盤面の列数。

    Return
    ----------
    probability : float
        先手の勝率

    """
    agent1: Agent = Agent("エージェント1")
    agent2: Agent = Agent("エージェント2")
    agent1_wins: int = 0
    agent2_wins: int = 0

    for _ in range(simulation_count):
        game: Chomp = Chomp(board_rows, board_cols)
        is_agent1_turn: bool = True

        while not game.is_game_over():
            if is_agent1_turn:
                row, col = agent1.select_eat_cell(game)
            else:
                row, col = agent2.select_eat_cell(game)
            game.eat(row, col)
            is_agent1_turn = not is_agent1_turn

        if is_agent1_turn:
            agent2_wins += 1
        else:
            agent1_wins += 1

    return agent1_wins / simulation_count


def compare_theory_and_simulation() -> None:
    """理論値とシミュレーション値の違いを視覚的に確認する関数。"""


if __name__ == "__main__":
    simulate_game(simulation_count=1000, board_rows=2, board_cols=1000)
