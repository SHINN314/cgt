from fractions import Fraction

import pytest

from src.recurrence_relation import calculate_probability_fraction
from src.three_times_n_prob import calculate_three_row_probability


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
