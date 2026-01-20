from pathlib import Path

import matplotlib.pyplot as plt

from src.prob.three_rows_chomp_prob import calculate_three_rows_prob_fraction

# Output directory setup
OUTPUT_DIR = Path(__file__).parent / "output"


def visualize_three_rows_chomp_prob(
    init_n1: int,
    init_n2: int,
    init_n3: int,
    output_file: str | None = None,
) -> None:
    """指定した初期盤面からn3を動かしながら3行のChompの勝率を計算して可視化する関数。

    Parameters
    ----------
    init_n1 : int
        1行目のマスの数の初期値
    init_n2: int
        2行目のマスの数の初期値
    init_n3: int
        3行目のマスの数の初期値
    output_file: str
        出力するファイルのパス

    Returns
    -------
    None

    """
    if (init_n1 < init_n2) or (init_n2 < init_n3):
        msg: str = "盤面は n1 >= n2 >= n3 の形で指定してください。"
        raise ValueError(msg)

    if output_file is None:
        output_file = str(OUTPUT_DIR / "three_rows_chomp.png")

    # Prepare data for plotting
    prob_list = [
        float(calculate_three_rows_prob_fraction(init_n1, init_n2, n3))
        for n3 in range(init_n3 + 1)
    ]
    n3_values = list(range(init_n3 + 1))

    # Create matplotlib figure
    _, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        n3_values,
        prob_list,
        "o-",
        linewidth=2,
        markersize=6,
        label="Winning Probability",
    )
    ax.set_xlabel("Number of squares in row 3 (n3)", fontsize=12)
    ax.set_ylabel("Winning Probability", fontsize=12)
    ax.set_title(
        f"Three Rows Chomp Winning Probability (n1={init_n1}, n2={init_n2})",
        fontsize=14,
    )
    # Set y-axis limits based on data with margin
    y_min = min(prob_list)
    y_max = max(prob_list)
    y_margin = (y_max - y_min) * 0.1 if y_max > y_min else 0.05
    ax.set_ylim([max(0, y_min - y_margin), min(1, y_max + y_margin)])
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Graph saved to {output_file}")


def batch_visualize_three_rows_prob(
    init_n1: int,
    init_n2: int,
    init_n3: int,
    output_file: str | None = None,
) -> None:
    """複数の盤面をまとめて可視化する関数。

    この関数ではn1, n2も動かしながらChompの勝率を計算して可視化する。

    Parameters
    ----------
    init_n1: int
        1行目のマスの数の初期値
    init_n2: int
        2行目のマスの数の初期値
    init_n3: int
        3行目のマスの数の初期値
    output_file: str
        出力するファイルのパス

    Returns
    -------
    None

    """
    if (init_n1 < init_n2) or (init_n2 < init_n3):
        msg: str = "盤面は n1 >= n2 >= n3 の形で指定してください。"
        raise ValueError(msg)

    if output_file is None:
        output_file = str(OUTPUT_DIR / "batch_three_rows_chomp.png")

    # Create matplotlib subplots
    rows = init_n1 + 1
    cols = init_n2 + 1
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 3, rows * 3))

    # Flatten axes array for easier iteration
    if rows == 1:
        axes = axes.reshape(1, -1)
    if cols == 1:
        axes = axes.reshape(-1, 1)

    for n1 in range(init_n1 + 1):
        for n2 in range(init_n2 + 1):
            ax = axes[n1, n2]

            if n2 <= n1:
                # Prepare data for plotting
                prob_list = [
                    float(calculate_three_rows_prob_fraction(n1, n2, n3))
                    for n3 in range(min(n2, init_n3) + 1)
                ]
                n3_values = list(range(min(n2, init_n3) + 1))

                # Plot data
                ax.plot(n3_values, prob_list, "o-", linewidth=2, markersize=4)
                # Set y-axis limits based on data with margin
                y_min = min(prob_list)
                y_max = max(prob_list)
                y_margin = (y_max - y_min) * 0.1 if y_max > y_min else 0.05
                ax.set_ylim([max(0, y_min - y_margin), min(1, y_max + y_margin)])
                ax.set_title(f"n1={n1}, n2={n2}", fontsize=10)
                ax.set_xlabel("n3", fontsize=9)
                ax.set_ylabel("Prob", fontsize=9)
                ax.grid(True, alpha=0.3)
            else:
                # Hide unused subplots
                ax.set_visible(False)

    fig.suptitle(
        "Three Rows Chomp Winning Probability - Batch Visualization",
        fontsize=16,
    )
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Batch graph saved to {output_file}")


def batch_visualize_three_rows_prob_overlap_col(
    init_n1: int,
    init_n2: int,
    init_n3: int,
    output_file: str | None = None,
) -> None:
    """同じ列のグラフを1つにまとめて可視化する関数。

    この関数ではn2ごとに1つのグラフを作成し、同じn2を持つ複数のn1の値を重ねて表示する。

    Parameters
    ----------
    init_n1: int
        1行目のマスの数の初期値
    init_n2: int
        2行目のマスの数の初期値
    init_n3: int
        3行目のマスの数の初期値
    output_file: str
        出力するファイルのパス

    Returns
    -------
    None

    """
    if (init_n1 < init_n2) or (init_n2 < init_n3):
        msg: str = "盤面は n1 >= n2 >= n3 の形で指定してください。"
        raise ValueError(msg)

    if output_file is None:
        output_file = str(OUTPUT_DIR / "batch_three_rows_chomp_overlap.png")

    # Create matplotlib subplots (1 row, multiple columns for each n2)
    cols = init_n2 + 1
    fig, axes = plt.subplots(1, cols, figsize=(cols * 4, 5))

    # Ensure axes is always iterable
    if cols == 1:
        axes = [axes]

    # Create color map based on n1 values (all possible n1 values)
    all_n1_values = list(range(init_n1 + 1))
    cmap_name = "tab10" if len(all_n1_values) <= 10 else "hsv"
    cmap = plt.get_cmap(cmap_name)
    colors = {
        n1: cmap(i / max(1, len(all_n1_values) - 1))
        for i, n1 in enumerate(all_n1_values)
    }

    for n2 in range(init_n2 + 1):
        ax = axes[n2]

        # Collect all data for this n2 value with different n1 values
        all_y_values = []
        for n1 in range(n2, init_n1 + 1):
            # Prepare data for plotting
            prob_list = [
                float(calculate_three_rows_prob_fraction(n1, n2, n3))
                for n3 in range(min(n2, init_n3) + 1)
            ]
            n3_values = list(range(min(n2, init_n3) + 1))
            all_y_values.extend(prob_list)

            # Plot data with color assigned by n1
            ax.plot(
                n3_values,
                prob_list,
                "o-",
                linewidth=2,
                markersize=4,
                label=f"n1={n1}",
                color=colors[n1],
            )

        # Set y-axis limits based on all data with margin
        y_min = min(all_y_values)
        y_max = max(all_y_values)
        y_margin = (y_max - y_min) * 0.1 if y_max > y_min else 0.05
        ax.set_ylim([max(0, y_min - y_margin), min(1, y_max + y_margin)])
        ax.set_title(f"n2={n2}", fontsize=12)
        ax.set_xlabel("n3", fontsize=10)
        ax.set_ylabel("Prob", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)

    fig.suptitle(
        "Three Rows Chomp Winning Probability - Overlap Visualization",
        fontsize=16,
    )
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Overlap graph saved to {output_file}")


def batch_visualize_three_rows_prob_overlap_row(
    init_n1: int,
    init_n2: int,
    init_n3: int,
    output_file: str | None = None,
) -> None:
    """同じ行のグラフを1つにまとめて可視化する関数。

    この関数ではn1ごとに1つのグラフを作成し、同じn1を持つ複数のn2の値を重ねて表示する。

    Parameters
    ----------
    init_n1: int
        1行目のマスの数の初期値
    init_n2: int
        2行目のマスの数の初期値
    init_n3: int
        3行目のマスの数の初期値
    output_file: str
        出力するファイルのパス

    Returns
    -------
    None

    """
    if (init_n1 < init_n2) or (init_n2 < init_n3):
        msg: str = "盤面は n1 >= n2 >= n3 の形で指定してください。"
        raise ValueError(msg)

    if output_file is None:
        output_file = str(OUTPUT_DIR / "batch_three_rows_chomp_overlap_row.png")

    # Create matplotlib subplots (multiple rows, 1 column for each n1)
    rows = init_n1 + 1
    fig, axes = plt.subplots(rows, 1, figsize=(6, rows * 3))

    # Ensure axes is always iterable
    if rows == 1:
        axes = [axes]

    # Create color map based on n2 values (all possible n2 values)
    all_n2_values = list(range(init_n2 + 1))
    cmap_name = "tab10" if len(all_n2_values) <= 10 else "hsv"
    cmap = plt.get_cmap(cmap_name)
    colors = {
        n2: cmap(i / max(1, len(all_n2_values) - 1))
        for i, n2 in enumerate(all_n2_values)
    }

    for n1 in range(init_n1 + 1):
        ax = axes[n1]

        # Collect all data for this n1 value with different n2 values
        all_y_values = []
        for n2 in range(min(n1, init_n2) + 1):
            # Prepare data for plotting
            prob_list = [
                float(calculate_three_rows_prob_fraction(n1, n2, n3))
                for n3 in range(min(n2, init_n3) + 1)
            ]
            n3_values = list(range(min(n2, init_n3) + 1))
            all_y_values.extend(prob_list)

            # Plot data with color assigned by n2
            ax.plot(
                n3_values,
                prob_list,
                "o-",
                linewidth=2,
                markersize=4,
                label=f"n2={n2}",
                color=colors[n2],
            )

        # Set y-axis limits based on all data with margin
        y_min = min(all_y_values)
        y_max = max(all_y_values)
        y_margin = (y_max - y_min) * 0.1 if y_max > y_min else 0.05
        ax.set_ylim([max(0, y_min - y_margin), min(1, y_max + y_margin)])
        ax.set_title(f"n1={n1}", fontsize=12)
        ax.set_xlabel("n3", fontsize=10)
        ax.set_ylabel("Prob", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)

    fig.suptitle(
        "Three Rows Chomp Winning Probability - Overlap Row Visualization",
        fontsize=16,
    )
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Overlap row graph saved to {output_file}")


if __name__ == "__main__":
    # batch_visualize_three_rows_prob(20, 16, 12)
    # batch_visualize_three_rows_prob_overlap_col(20, 16, 12)
    batch_visualize_three_rows_prob_overlap_row(20, 16, 12)
