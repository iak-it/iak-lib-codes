"""Tests of the iak_lib_codes._codes module."""
from src.iak_lib_codes import Code


class TestCodes:  # pylint: disable=too-few-public-methods
    """Tests for Code class."""

    def test_basic(self) -> None:
        """Base test."""
        code = Code(0)
        assert code == 0
        assert code is Code.EMPTY
