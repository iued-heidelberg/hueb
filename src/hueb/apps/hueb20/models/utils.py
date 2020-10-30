from psycopg2.extras import NumericRange


def close_range(range_value):
    if range_value is not None:
        if not range_value.isempty:
            if (range_value.lower is not None) & (range_value.upper is None):
                return NumericRange(range_value.lower, range_value.lower + 1)
            elif (range_value.lower is None) & (range_value.upper is not None):
                return NumericRange(range_value.upper, range_value.upper + 1)
            else:
                return NumericRange(range_value.lower, range_value.upper + 1)
                pass
    return range_value


def open_range(range_value):
    if range_value is not None:
        if not range_value.isempty:
            if range_value.lower + 1 == range_value.upper:
                return NumericRange(range_value.lower, None)
            elif (range_value.lower is not None) & (range_value.upper is not None):
                return NumericRange(range_value.lower, range_value.upper - 1)
            else:
                pass
    return range_value
