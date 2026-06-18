import matplotlib.pyplot as plt
import numpy as np

from config import RESULT_DIR
from src.game.agent import Agent
from src.game.chomp import Chomp


def simulate_game(row: int, col: int, agent1: Agent, agent2: Agent) -> str:
    """Chompのゲームをシミュレーションする関数。

    Parameters
    ----------
    row : int
        盤面の行数。
    col : int
        盤面の列数。
    agent1 : Agent
        最初のプレイヤー。
    agent2 : Agent
        2番目のプレイヤー。

    Returns
    -------
    str
        勝者の名前。

    """
    game = Chomp(row, col)
    current_agent = agent1

    while not game.is_empty_board():
        row, col = current_agent.select_eat_cell(game)
        game.eat(row, col)
        current_agent = agent2 if current_agent == agent1 else agent1

    return agent2.name if current_agent == agent1 else agent1.name


def batch_simulate_games(
    num_games: int,
    row: int,
    col: int,
    agent1: Agent,
    agent2: Agent,
) -> dict[str, int]:
    """複数回のChompゲームをシミュレーションする関数。

    Parameters
    ----------
    num_games : int
        シミュレーションするゲームの回数。
    row : int
        盤面の行数。
    col : int
        盤面の列数。
    agent1 : Agent
        最初のプレイヤー。
    agent2 : Agent
        2番目のプレイヤー。

    Returns
    -------
    dict of str to int
        勝者の名前とその勝利回数の辞書。

    """
    results = {agent1.name: 0, agent2.name: 0}

    for _ in range(num_games):
        winner = simulate_game(row, col, agent1, agent2)
        results[winner] += 1

    return results


def calculate_win_rate(results: dict[str, int]) -> dict[str, float]:
    """勝率を計算する関数。

    Parameters
    ----------
    results : dict of str to int
        勝者の名前とその勝利回数の辞書。

    Returns
    -------
    dict of str to float
        勝者の名前とその勝率の辞書。

    """
    total_games = sum(results.values())
    if total_games == 0:
        return dict.fromkeys(results, 0.0)

    win_rates = {name: wins / total_games for name, wins in results.items()}
    return win_rates


def batch_calculate_win_rate(
    num_batches: int,
    num_games_per_batch: int,
    row: int,
    col: int,
    agent1: Agent,
    agent2: Agent,
) -> dict[str, np.ndarray[np.float64]]:
    """複数回のChompゲームをシミュレーションし、勝率を計算する関数。

    Parameters
    ----------
    num_games : int
        バッチ処理を行う回数。
    row : int
        盤面の行数。
    col : int
        盤面の列数。
    agent1 : Agent
        最初のプレイヤー。
    agent2 : Agent
        2番目のプレイヤー。

    Returns
    -------
    dict of str to np.ndarray[np.float64]
        勝者の名前とその勝率の配列。

    """
    win_rates = {agent1.name: np.zeros(num_batches), agent2.name: np.zeros(num_batches)}

    for batch in range(num_batches):
        results = batch_simulate_games(num_games_per_batch, row, col, agent1, agent2)
        batch_win_rates = calculate_win_rate(results)
        for name, win_rate_array in win_rates.items():
            win_rate_array[batch] = batch_win_rates[name]

    return win_rates


def visualize_win_rates_distribution(
    win_rates: dict[str, np.ndarray[np.float64]],
    file_name: str = "win_rates_distribution.png",
) -> None:
    """勝率の分布をヒストグラムで可視化する関数。

    Parameters
    ----------
    win_rates : dict of str to np.ndarray[np.float64]
        勝者の名前とその勝率の配列。
    file_name : str
        保存するファイル名。
        デフォルトは "win_rates_distribution.png"。

    Returns
    -------
    None

    """
    plt.figure(figsize=(10, 6))
    for name, win_rate_array in win_rates.items():
        plt.hist(win_rate_array, bins=20, alpha=0.5, label=name)
    plt.title("Distribution of Win Rates")
    plt.xlabel("Win Rate")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{RESULT_DIR}/{file_name}")
    plt.close()


def main() -> None:
    """Chompのゲームをシミュレーションし、勝率の分布を可視化する関数。"""
    next_player = Agent("next_player")
    previous_player = Agent("previous_player")
    num_batches = 1000
    num_games_per_batch = 1000
    row, col = 10, 10

    win_rates = batch_calculate_win_rate(
        num_batches,
        num_games_per_batch,
        row,
        col,
        next_player,
        previous_player,
    )
    visualize_win_rates_distribution(
        win_rates,
        file_name="win_rates_distribution_b1000_gpb1000_r10_c10.png",
    )


if __name__ == "__main__":
    main()
