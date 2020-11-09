import pytest
from hueb.apps.hueb20.widgets.timerange import TimeRangeWidget
from psycopg2.extras import NumericRange


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # an empty value should return an empty object with exact selected
        (None, ["exact", None, NumericRange(None, None)]),
        (NumericRange(empty=True), ["exact", None, NumericRange(None, None)]),
        (NumericRange(None, None), ["exact", None, NumericRange(None, None)]),
        # a value where the delta between lower and upper is only 1 should return an exact selection and the lower value
        (NumericRange(1, 2), ["exact", 1, NumericRange(None, None)]),
        (NumericRange(-2, -1), ["exact", -2, NumericRange(None, None)]),
        # a value where the delta between lower and upper is greater than 1 should return a "range"-selection and a NumericRange Object where the upper value is reduced by one to convert a "[)" range into a "[]" for more intuitive editing
        (NumericRange(1, 3), ["range", None, NumericRange(1, 2)]),
        (NumericRange(1, 4), ["range", None, NumericRange(1, 3)]),
        (NumericRange(1, 5), ["range", None, NumericRange(1, 4)]),
        # an upwards open ended range should return as such without modifiaction
        (NumericRange(1, None), ["range", None, NumericRange(1, None)]),
        (NumericRange(2, None), ["range", None, NumericRange(2, None)]),
        (NumericRange(3, None), ["range", None, NumericRange(3, None)]),
        (NumericRange(4, None), ["range", None, NumericRange(4, None)]),
        # an downwards open ended range should return as such but the upper end should be reduced by one to convert a "[)" range into a "[]" for more intuitive editing
        (NumericRange(None, 1), ["range", None, NumericRange(None, 0)]),
        (NumericRange(None, 2), ["range", None, NumericRange(None, 1)]),
        (NumericRange(None, 3), ["range", None, NumericRange(None, 2)]),
        (NumericRange(None, 4), ["range", None, NumericRange(None, 3)]),
    ],
)
def test_decompress(test_input, expected):
    tr = TimeRangeWidget()
    output = tr.decompress(test_input)
    assert output == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # an empty value should return an empty object with exact selected
        (["exact", None, [None, None]], [None, None]),
        (["exact", "", [None, None]], [None, None]),
        # an exact value should be extendend with an upper range with the delta of one to compensate for the "[]" to "[)" conversion
        (["exact", 1, [None, None]], [1, 2]),
        (["exact", -2, [None, None]], [-2, -1]),
        (["exact", "1", [None, None]], [1, 2]),
        (["exact", "-2", [None, None]], [-2, -1]),
        # a range value should be extendend with an upper range with the delta of one to compensate for the "[]" to "[)" conversion
        (["range", None, ["1", "2"]], [1, 3]),
        (["range", None, ["1", "3"]], [1, 4]),
        (["range", None, ["1", "4"]], [1, 5]),
        (["range", None, [1, 3]], [1, 4]),
        (["range", None, [1, 4]], [1, 5]),
        # an upwards open ended range should return as such without modifiaction
        (["range", None, ["1", None]], [1, None]),
        (["range", None, ["2", None]], [2, None]),
        (["range", None, [3, None]], [3, None]),
        (["range", None, [4, None]], [4, None]),
        (["range", None, ["1", ""]], [1, None]),
        (["range", None, ["2", ""]], [2, None]),
        (["range", None, [3, ""]], [3, None]),
        (["range", None, [4, ""]], [4, None]),
        # an downwards open ended range should return as such but the upper end should be reduced by one to convert a "[)" range into a "[]" for more intuitive editing
        (["range", None, ["", 0]], [None, 1]),
        (["range", None, ["", 1]], [None, 2]),
        (["range", None, [None, "2"]], [None, 3]),
        (["range", None, [None, "3"]], [None, 4]),
        (["range", None, ["", 0]], [None, 1]),
        (["range", None, ["", 1]], [None, 2]),
        (["range", None, [None, "2"]], [None, 3]),
        (["range", None, [None, "3"]], [None, 4]),
    ],
)
def test_value_from_datadict(test_input, expected):
    tr = TimeRangeWidget()
    output = tr._value_from_datadict(test_input[0], test_input[1], test_input[2])
    assert output == expected
