import pytest
from hueb.apps.hueb20.models.utils import (
    close_range,
    open_range,
    timerange_serialization,
)
from psycopg2.extras import NumericRange


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # Convert infinite ranges into bounded ranges
        (NumericRange(1, None), NumericRange(1, 2)),
        (NumericRange(2, None), NumericRange(2, 3)),
        (NumericRange(None, 2), NumericRange(2, 3)),
        (NumericRange(None, 1), NumericRange(1, 2)),
        # Convert non-ranges (shouldn't occur because postgres creates empty ranges out of them)
        (NumericRange(1, 1), NumericRange(1, 2)),
        (NumericRange(2, 2), NumericRange(2, 3)),
        # Empty
        (NumericRange(empty=True), NumericRange(empty=True)),
        # None
        (None, None),
    ],
)
def test_close_range(test_input, expected):
    output = close_range(test_input)
    assert output == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # Convert infinite ranges into bounded ranges
        (NumericRange(1, 2), NumericRange(1, None)),
        (NumericRange(2, 3), NumericRange(2, None)),
        # Convert closed ranges with a greater delta than one from a range with excluded upper bound to one with an included upper bound
        (NumericRange(2, 4), NumericRange(2, 3)),
        (NumericRange(2, 5), NumericRange(2, 4)),
    ],
)
def test_open_range(test_input, expected):
    output = open_range(test_input)
    assert output == expected


@pytest.mark.parametrize(
    "timerange,expected",
    [
        # delta 1 range, return only single value
        (NumericRange(2, 3), "2"),
        (NumericRange(3, 4), "3"),
        (NumericRange(4, 5), "4"),
        # default range, reduce upper end by one
        (NumericRange(1, 3), "1 - 2"),
        (NumericRange(1, 4), "1 - 3"),
        (NumericRange(1, 5), "1 - 4"),
        # upper end unknown
        (NumericRange(1, None), "1 - ?"),
        (NumericRange(1, None), "1 - ?"),
        (NumericRange(1, None), "1 - ?"),
        # lower end unknown
        (NumericRange(None, 3), "? - 2"),
        (NumericRange(None, 4), "? - 3"),
        (NumericRange(None, 5), "? - 4"),
        # unbound range
        (NumericRange(None, None), "? - ?"),
        # empty range
        (NumericRange(empty=True), "-"),
        # None
        (None, "-"),
    ],
)
def test_timerange_serialization(timerange, expected):
    output = timerange_serialization(timerange)
    assert output == expected
