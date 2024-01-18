from src.iak_lib_codes import Code


class TestCodes:

    def test_basic(self) -> None:
        code = Code(0)
        assert code == 0
        assert code is Code.EMPTY
