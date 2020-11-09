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

