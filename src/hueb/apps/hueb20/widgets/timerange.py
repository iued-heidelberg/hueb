import logging

from django.contrib.postgres.forms import RangeWidget
from django.forms import MultiWidget, NumberInput, RadioSelect
from django.utils.translation import gettext_lazy as _
from psycopg2.extras import NumericRange

logger = logging.getLogger(__name__)


class TimeRangeWidget(MultiWidget):
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
        try:
            if (int(value.lower) + 1) == int(value.upper):
                return [
                    "exact",
                    value.lower,
                    NumericRange(None, None, "[)"),
                ]
            else:
                return [
                    "range",
                    None,
                    NumericRange(value.lower, value.upper - 1),
                ]
        except TypeError:
            pass

        return ["exact", None, None]

    def value_from_datadict(self, data, files, name):
        choice, exact_value, range_value = super().value_from_datadict(
            data, files, name
        )
        if choice == "exact":
            return [int(exact_value), int(exact_value) + 1]
        elif choice == "range":
            return [int(range_value[0]), int(range_value[1]) + 1]
