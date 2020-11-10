import logging

from django.contrib.postgres.forms import RangeWidget
from django.forms import MultiWidget, NumberInput, RadioSelect
from django.utils.translation import gettext_lazy as _
from psycopg2.extras import NumericRange

logger = logging.getLogger(__name__)


class TimeRangeWidget(MultiWidget):
    """Widget for editing NumericRanges used as YearRanges

    """

    template_name = "hueb20/widgets/timerange.html"

    choices = (
        ("exact", _("Exakt")),
        ("range", _("Bereich")),
    )

    def __init__(self, *args, **kwargs):
        widgets = (
            RadioSelect(choices=self.choices),
            NumberInput(),
            RangeWidget(NumberInput()),
        )
        super().__init__(widgets=widgets, *args, **kwargs)

    def get_context(self, name, value, attrs):
        """
        The Integer Rangefield that is used to store the Timerange returns an list containing the lower and upper values of the range. This causes the render function of MultiWidget to short curcuit and not call decompress before rendering the widget out.
        We can avoid this 'if not isinstance(value, list):'-check in the Multiwidget-Check by reinitializing value as a Range-Object before render() is called
        """
        value = NumericRange(value[0], value[1])
        context = super().get_context(name, value, attrs)
        return context

    def decompress(self, value):
        """
        Decompresses the timerange stored in the database into the array of values needed for the timerange widget.

        It reduces the upper end of the passed numeric range by 1 to convert the range from upper end excluded ("[)") into upper end included ("[]").

        Args:
            value (NumericRange): NumericRange value out of the database

        Returns:
            [str, Integer, NumericRange]: list of the three values needed in the widget
        """
        if value and isinstance(value, NumericRange):
            if not value.isempty:
                lower = value.lower
                try:
                    upper = value.upper - 1
                except TypeError:
                    upper = None

                if lower == upper:
                    return ["exact", lower, NumericRange(None, None)]
                else:
                    return ["range", None, NumericRange(lower, upper)]

        return ["exact", None, NumericRange(None, None)]

    def value_from_datadict(self, data, files, name):
        """Turns form values into an array for the NumericRange Field to use   """
        choice, exact_value, range_value = super().value_from_datadict(
            data, files, name
        )
        return self._value_from_datadict(choice, exact_value, range_value)

    def _value_from_datadict(self, choice, exact_value, range_value):
        lower, upper = None, None
        if choice:
            if choice == "exact":
                try:
                    lower = int(exact_value)
                    upper = int(exact_value) + 1
                except (ValueError, TypeError):
                    pass

            elif choice == "range":
                try:
                    lower = int(range_value[0])
                except (ValueError, TypeError):
                    pass

                try:
                    upper = int(range_value[1]) + 1
                except (ValueError, TypeError):
                    pass

                return [lower, upper]

        return [lower, upper]
