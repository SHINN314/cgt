import numpy as np
import pytest

from src.recurrence_relation import calculate_mutual_recurrence_relation


class TestCalculateMutualRecurrenceRelation:
    """calculate_mutual_recurrence_relation関数のテストクラス。"""

    def test_k_equals_1(self) -> None:
        """k=1の場合のテスト。"""
        result = calculate_mutual_recurrence_relation(1)
        expected = np.array([1, -1], dtype=int)
        np.testing.assert_array_equal(result, expected)

    def test_k_equals_2(self) -> None:
        """k=2の場合のテスト。"""
        result = calculate_mutual_recurrence_relation(2)
        expected = np.array([4, -4], dtype=int)
        np.testing.assert_array_equal(result, expected)

    def test_k_equals_3(self) -> None:
        """k=3の場合のテスト。"""
        result = calculate_mutual_recurrence_relation(3)
        expected = np.array([68, -76], dtype=int)
        np.testing.assert_array_equal(result, expected)

    def test_k_equals_4(self) -> None:
        """k=4の場合のテスト。"""
        result = calculate_mutual_recurrence_relation(4)
        expected = np.array([2576, -3248], dtype=int)
        np.testing.assert_array_equal(result, expected)

    def test_k_equals_0_raises_value_error(self) -> None:
        """k=0が渡された場合にValueErrorが発生することを確認。"""
        with pytest.raises(ValueError, match="kは1以上の整数でなければなりません。"):
            calculate_mutual_recurrence_relation(0)

    def test_negative_k_raises_value_error(self) -> None:
        """負のkが渡された場合にValueErrorが発生することを確認。"""
        with pytest.raises(ValueError, match="kは1以上の整数でなければなりません。"):
            calculate_mutual_recurrence_relation(-1)

    def test_return_type_is_ndarray(self) -> None:
        """返り値の型がnumpy.ndarrayであることを確認。"""
        result = calculate_mutual_recurrence_relation(1)
        assert isinstance(result, np.ndarray)

    def test_return_array_length(self) -> None:
        """返り値の配列の長さが2であることを確認。"""
        result = calculate_mutual_recurrence_relation(2)
        assert len(result) == 2

    def test_return_array_dtype(self) -> None:
        """返り値の配列のdtypeがintであることを確認。"""
        result = calculate_mutual_recurrence_relation(1)
        assert result.dtype == np.dtype("int64") or result.dtype == np.dtype("int32")
