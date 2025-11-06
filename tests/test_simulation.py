from unittest.mock import patch

import pytest

from scripts.simulation import simulate_with_log


def test_simulate_with_log_outputs_logs_and_winner(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """simulate_with_logがログと勝者を出力することを確認する。"""
    user_inputs = ["1", "1", "1"]
    with patch("builtins.input", side_effect=user_inputs), patch(
        "src.agent.Agent.select_eat_cell",
        return_value=(0, 0),
    ) as mock_select:
        simulate_with_log()

    captured = capsys.readouterr()

    log_snippet = (
        "player_name: 先手プレイヤー, selected_row: 0, selected_col: 0"
    )
    if log_snippet not in captured.out:
        msg = "ログ出力が期待した形式ではありません。"
        raise AssertionError(msg)

    if "winner: prev_player" not in captured.out:
        msg = "勝者の出力が期待値と一致しません。"
        raise AssertionError(msg)

    if mock_select.call_count != 1:
        msg = "select_eat_cellの呼び出し回数が不正です。"
        raise AssertionError(msg)
