from fractions import Fraction

import pytest

from src.recurrence_relation import calculate_probability_fraction
from src.three_rows_chomp_prob import (
    calculate_three_row_probability,
    is_multiple_number,
)


class TestCalculateThreeRowProbability:
    """calculate_three_row_probability関数のテストクラス。"""

    def test_compare_with_two_row_n1_1_n2_0_n3_0(self) -> None:
        """n1=1, n2=0, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(1, 0, 0)
        expected = calculate_probability_fraction(1, 0)
        assert result == expected

    def test_compare_with_two_row_n1_2_n2_0_n3_0(self) -> None:
        """n1=2, n2=0, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(2, 0, 0)
        expected = calculate_probability_fraction(2, 0)
        assert result == expected

    def test_compare_with_two_row_n1_2_n2_1_n3_0(self) -> None:
        """n1=2, n2=1, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(2, 1, 0)
        expected = calculate_probability_fraction(2, 1)
        assert result == expected

    def test_compare_with_two_row_n1_3_n2_1_n3_0(self) -> None:
        """n1=3, n2=1, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(3, 1, 0)
        expected = calculate_probability_fraction(3, 1)
        assert result == expected

    def test_compare_with_two_row_n1_3_n2_2_n3_0(self) -> None:
        """n1=3, n2=2, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(3, 2, 0)
        expected = calculate_probability_fraction(3, 2)
        assert result == expected

    def test_compare_with_two_row_n1_4_n2_2_n3_0(self) -> None:
        """n1=4, n2=2, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(4, 2, 0)
        expected = calculate_probability_fraction(4, 2)
        assert result == expected

    def test_compare_with_two_row_n1_4_n2_3_n3_0(self) -> None:
        """n1=4, n2=3, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(4, 3, 0)
        expected = calculate_probability_fraction(4, 3)
        assert result == expected

    def test_compare_with_two_row_n1_5_n2_3_n3_0(self) -> None:
        """n1=5, n2=3, n3=0の場合、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(5, 3, 0)
        expected = calculate_probability_fraction(5, 3)
        assert result == expected

    def test_base_case_all_zero(self) -> None:
        """n1=0, n2=0, n3=0の基底ケースを確認。"""
        result = calculate_three_row_probability(0, 0, 0)
        expected = calculate_probability_fraction(0, 0)
        assert result == expected

    def test_return_type_is_fraction(self) -> None:
        """返り値の型がFractionであることを確認。"""
        result = calculate_three_row_probability(2, 1, 0)
        assert isinstance(result, Fraction)

    @pytest.mark.parametrize(
        "n1,n2",
        [
            (1, 0),
            (2, 0),
            (2, 1),
            (3, 1),
            (3, 2),
            (4, 2),
            (4, 3),
            (5, 3),
            (5, 4),
            (6, 4),
        ],
    )
    def test_compare_with_two_row_parametrized(self, n1: int, n2: int) -> None:
        """様々な2行盤面(n3=0)において、2行の確率計算と一致することを確認。"""
        result = calculate_three_row_probability(n1, n2, 0)
        expected = calculate_probability_fraction(n1, n2)
        assert result == expected, f"Failed for n1={n1}, n2={n2}"


class TestIsMultipleNumber:
    """is_multiple_number関数のテストクラス。

    二行のChompでは、n=2の場合に確率の分母が∏(n1+n2-i)の約数になることが
    特定の盤面サイズで成り立つことが知られている。
    このテストではn3=0（二行盤面）の場合について、n=2でis_multiple_number関数が
    Trueを返すケースを確認する。
    """

    @pytest.mark.parametrize(
        "n1,n2",
        [
            # 小さい盤面でn=2がTrueになるケース
            (2, 1),
            (3, 1),
            (3, 2),
            (4, 2),
            (5, 3),
        ],
    )
    def test_two_row_chomp_n_equals_2_divisible(self, n1: int, n2: int) -> None:
        """二行盤面(n3=0)において、n=2の場合にis_multiple_numberがTrueを返すことを確認。

        二行のChompでは、小さい盤面サイズにおいて1/2 - P(n1, n2, 0)の分母が
        ∏_{i=0}^{2}(n1+n2-i)の約数になる。
        """
        # n3=0（二行盤面）で確率を計算
        prob = calculate_three_row_probability(n1, n2, 0)

        # n=2でis_multiple_numberがTrueを返すことを確認
        result = is_multiple_number(prob, 2, n1, n2, 0)
        assert result is True, (
            f"Expected True for n1={n1}, n2={n2}, n3=0, n=2, "
            f"but got {result}. Probability was {prob}"
        )

    def test_raises_error_when_recurrence_denominator_is_zero(self) -> None:
        """recurrence_denominatorが0になる場合にValueErrorが発生することを確認。

        n >= n1 + n2 + n3の場合、積の計算で0が含まれるためエラーになる。
        """
        prob = calculate_three_row_probability(3, 2, 0)
        n = 5  # n1 + n2 + n3 = 5なので、n=5で0になる

        with pytest.raises(ValueError, match="盤面を十分に大きくしてください"):
            is_multiple_number(prob, n, 3, 2, 0)

    def test_small_boards_with_n_equals_2(self) -> None:
        """小さい盤面でn=2の場合のテスト。"""
        test_cases = [(2, 1), (3, 1), (3, 2), (4, 2), (5, 3)]

        for n1, n2 in test_cases:
            prob = calculate_three_row_probability(n1, n2, 0)
            result = is_multiple_number(prob, 2, n1, n2, 0)
            assert result is True, f"Failed for n1={n1}, n2={n2}"

    def test_edge_case_with_minimal_board(self) -> None:
        """最小盤面でn=2の境界条件をテスト。"""
        prob = calculate_three_row_probability(2, 1, 0)
        result = is_multiple_number(prob, 2, 2, 1, 0)
        assert result is True

    def test_various_n_values_to_show_n_2_is_special(self) -> None:
        """n=2が特別であることを示すため、様々なnの値をテスト。

        二行のChompではn=2で常にTrueになるが、他のnでは必ずしもTrueにならない。
        """
        n1, n2, n3 = 5, 3, 0
        prob = calculate_three_row_probability(n1, n2, n3)

        # n=2の場合は必ずTrue
        result_n2 = is_multiple_number(prob, 2, n1, n2, n3)
        assert result_n2 is True, "n=2 should always return True for two-row Chomp"

        # 他のnの値では必ずしもTrueにならないことを示す
        # （この部分は参考情報として、エラーなく実行できるかを確認）
        for n in [0, 1]:
            try:
                result = is_multiple_number(prob, n, n1, n2, n3)
                # 結果が何であれ、エラーが出なければOK
            except ValueError:
                # n >= n1+n2+n3の場合はエラーが出る可能性がある
                pass
