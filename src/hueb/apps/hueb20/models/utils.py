from psycopg2.extras import NumericRange

LATEIN = "LATEIN"
LIDOS = "LIDOS "
LEGACY = "LEGACY"
HUEB20 = "HUEB20"

HUEB_APPLICATIONS = [
    (LATEIN, "HÜB Latein Datensatz"),
    (LIDOS, "HÜB Lidos Datensatz"),
    (LEGACY, "HÜB Basis Datensatz"),
    (HUEB20, "HÜB 2020 Datensatz"),
]


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


def timerange_serialization(timerange):
    """Serializes a NumericRange to handle all cases

    Args:
        timerange ([type]): [description]

    Returns:
        [type]: [description]
    """
    if timerange is not None:
        if not timerange.isempty:
            try:
                if timerange.lower == (timerange.upper - 1):
                    return str(timerange.lower)
            except (ValueError, TypeError):
                pass

            if timerange.lower is not None:
                lower = str(timerange.lower)
            else:
                lower = "?"
            if timerange.upper is not None:
                upper = str(timerange.upper - 1)
            else:
                upper = "?"

            return lower + " - " + upper

    return "-"
