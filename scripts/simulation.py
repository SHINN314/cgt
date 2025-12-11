from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from config import RESULT_DIR
from src.agent import Agent
from src.chomp import Chomp
from src.recurrence_relation import calculate_probability


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
    print(
        f"Simulating {simulation_count} games on a {board_rows}x{board_cols} board...",
    )
    agent1: Agent = Agent("エージェント1")  # 先手のプレイヤー
    agent2: Agent = Agent("エージェント2")  # 後手のプレイヤー
    agent1_wins: int = 0
    agent2_wins: int = 0

    for _ in range(simulation_count):
        game: Chomp = Chomp(board_rows, board_cols)
        is_agent1_turn: bool = True

        while not game.is_empty_board():
            if is_agent1_turn:
                row, col = agent1.select_eat_cell(game)
            else:
                row, col = agent2.select_eat_cell(game)
            game.eat(row, col)
            is_agent1_turn = not is_agent1_turn

        if is_agent1_turn:
            agent1_wins += 1
        else:
            agent2_wins += 1

    return agent1_wins / simulation_count


def compare_theory_and_simulation(
    k: int,
    simulation_count: int = 10000,
    file_name: str = "theory_vs_simulation.png",
) -> None:
    """理論値とシミュレーション値の違いを視覚的に確認する関数。

    2xi (1 <= i <= k)の長方形Chompの先手勝率を理論値とシミュレーションで比較する。

    Parameters
    ----------
    k : int
        2列目のチョコレートの最大数
    simulation_count : int, optional
        各盤面でのシミュレーション回数 (デフォルト: 10000)
    file_name : str
        グラフを保存するファイル名

    """
    if k < 1:
        msg: str = "kは1以上の整数でなければなりません。"
        raise ValueError(msg)

    # データを格納する配列
    i_values = np.arange(1, k + 1)
    theory_values = np.zeros(k)
    simulation_values = np.zeros(k)

    # 各iについてシミュレーションと理論値を計算
    for idx, i in enumerate(i_values):
        print(f"i={i}/{k} を処理中...")

        # 理論値の計算
        theory_prob = calculate_probability(int(i), int(i))
        theory_values[idx] = theory_prob

        # シミュレーション値の計算
        sim_prob = simulate_game(
            simulation_count=simulation_count,
            board_rows=2,
            board_cols=int(i),
        )
        simulation_values[idx] = sim_prob

        print(f"  理論値: {theory_prob:.4f}, シミュレーション値: {sim_prob:.4f}")

    # グラフの作成
    plt.figure(figsize=(12, 6))

    plt.plot(
        i_values,
        theory_values,
        marker="o",
        label="Theory",
        linewidth=2,
        markersize=8,
        color="blue",
    )

    plt.plot(
        i_values,
        simulation_values,
        marker="s",
        label=f"Simulation (N={simulation_count})",
        linewidth=2,
        markersize=8,
        color="red",
        alpha=0.7,
    )

    plt.xlabel("Number of Chocolates in Column 2 (i)")
    plt.ylabel("First Player Winning Probability")
    plt.title(f"Theory vs Simulation: 2xi Chomp (1 <= i <= {k})")
    plt.legend()
    plt.grid(visible=True, alpha=0.3)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(RESULT_DIR / file_name)
    plt.show()


def simulate_square_chomp() -> None:
    """正方形Chompのシミュレーションを複数回実行し、結果を可視化する関数。"""
    max_edge_length: int = int(
        input(
            "シミュレーションする正方形領域の1辺の最大値を入力してください(デフォルト: 2): ",  # noqa: E501
        )
        or "2",
    )
    simulate_count: int = int(
        input(
            "各盤面でシミュレーションする回数を入力して下さい(デフォルト: 10000): ",
        )
        or "10000",
    )
    file_name: str = (
        input(
            "画像ファイルの名前を入力してください(デフォルト: square_chomp_simulation_yyyymmdd_v.png): ",  # noqa: E501
        )
        or "square_chomp_simulation_yyyymmdd_v.png"
    )
    ns = np.arange(1, max_edge_length + 1)
    probabilities = np.array(
        [
            simulate_game(
                simulation_count=simulate_count,
                board_rows=edge_length,
                board_cols=edge_length,
            )
            for edge_length in range(1, max_edge_length + 1)
        ],
    )
    print(probabilities)  # デバッグ用出力

    plt.figure(figsize=(10, 6))
    plt.plot(ns, probabilities, marker="o")
    plt.title("Probability of nxn Chomp - First Player Winning")
    plt.xlabel("Number of Chocolates in Each Column (n)")
    plt.ylabel("First Player Winning Probability")
    plt.ylim(0, 1)
    plt.grid()
    plt.savefig(RESULT_DIR / file_name)
    plt.show()


def simulate_with_log() -> None:
    """ログをつけながらシミュレーションを実行する関数"""
    init_row: int = int(
        input("盤面の行数を入力してください(デフォルト: 2): ") or "2",
    )
    init_col: int = int(
        input("盤面の列数を入力してください(デフォルト: 2): ") or "2",
    )
    simulation_count: int = int(
        input("各盤面でのシミュレーション回数を入力してください(デフォルト: 10000): ")
        or "10000",
    )
    file_name: str = (
        input("ログを保存するファイル名を入力して下さい(デフォルト: simulation.log): ")
        or "simulation.log"
    )

    with Path.open(RESULT_DIR / file_name, mode="w") as f:
        for _ in range(1, simulation_count + 1):
            game: Chomp = Chomp(init_row, init_col)
            next_player: Agent = Agent("先手プレイヤー")
            prev_player: Agent = Agent("後手プレイヤー")
            is_next_player_turn: bool = True
            logs: list[
                dict[str, str | int]
            ] = []  # [{player_name: str, row: int, col: int}]
            # Note: ログは辞書のリストなので、そのまま保持

            while game.is_empty_board() is False:
                if is_next_player_turn:
                    row, col = next_player.select_eat_cell(game)
                    logs.append(
                        {
                            "player_name": next_player.name,
                            "selected_row": row,
                            "selected_col": col,
                        },
                    )
                else:
                    row, col = prev_player.select_eat_cell(game)
                    logs.append(
                        {
                            "player_name": prev_player.name,
                            "selected_row": row,
                            "selected_col": col,
                        },
                    )
                game.eat(row, col)
                is_next_player_turn = not is_next_player_turn

            # logの出力
            for log in logs:
                f.write(
                    f"player_name: {log['player_name']}, selected_cell: ({log['selected_row']}, {log['selected_col']})\n",  # noqa: E501
                )

            # 勝者の出力
            if is_next_player_turn:
                f.write("winner: next_player\n")
            else:
                f.write("winner: prev_player\n")


if __name__ == "__main__":
    simulate_square_chomp()
