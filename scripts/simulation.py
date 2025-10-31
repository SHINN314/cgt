import matplotlib.pyplot as plt

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

    # データを格納するリスト
    i_values: list[int] = []
    theory_values: list[float] = []
    simulation_values: list[float] = []

    # 各iについてシミュレーションと理論値を計算
    for i in range(1, k + 1):
        print(f"i={i}/{k} を処理中...")
        i_values.append(i)

        # 理論値の計算
        theory_prob = calculate_probability(i, i)
        theory_values.append(theory_prob)

        # シミュレーション値の計算
        sim_prob = simulate_game(
            simulation_count=simulation_count,
            board_rows=2,
            board_cols=i,
        )
        simulation_values.append(sim_prob)

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


def simulate_square_chomp(batch_num: int, simulate_count: int) -> None:
    """正方形Chompのシミュレーションを複数回実行し、結果を可視化する関数。

    正方形は2✕2に制限してシミュレーションを行う。

    Parameters
    ----------
    batch_num : int
        シミュレーションバッチの数。
    simulate_count : int
        各バッチでのシミュレーション回数。

    """
    ns: list[int] = list(range(1, batch_num + 1))
    probabilities: list[float] = [
        simulate_game(simulation_count=simulate_count, board_rows=n, board_cols=n)
        for n in range(1, batch_num + 1)
    ]
    print(probabilities)  # デバッグ用出力

    plt.figure(figsize=(10, 6))
    plt.plot(ns, probabilities, marker="o")
    plt.title("Probability of nxn Chomp - First Player Winning")
    plt.xlabel("Number of Chocolates in Each Column (n)")
    plt.ylabel("First Player Winning Probability")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # 正方形盤面でシミュレーション
    batch_num: int = int(
        input("シミュレーションのバッチ回数を入力してください: "),
    )
    simulate_count: int = int(
        input("各バッチでのシミュレーション回数を入力してください: "),
    )
    simulate_square_chomp(batch_num, simulate_count)
