from src.agent import Agent
from src.chomp import Chomp


def simulate_game(simulation_count: int, board_rows: int, board_cols: int) -> None:
    """Chompゲームのシミュレーションを実行する関数。

    Parameters
    ----------
    simulation_count : int
        シミュレーションの回数。
    board_rows : int
        盤面の行数。
    board_cols : int
        盤面の列数。

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

    print(f"エージェント1の勝利数: {agent1_wins}")
    print(f"エージェント2の勝利数: {agent2_wins}")


if __name__ == "__main__":
    simulate_game(simulation_count=1000, board_rows=2, board_cols=1000)
