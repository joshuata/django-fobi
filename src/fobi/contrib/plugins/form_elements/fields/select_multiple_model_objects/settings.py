from .conf import get_setting

from fobi.helpers import validate_submit_value_as

__title__ = (
    "fobi.contrib.plugins.form_elements.fields."
    "select_multiple_model_objects.settings"
)
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "IGNORED_MODELS",
    "SUBMIT_VALUE_AS",
)

IGNORED_MODELS = get_setting("IGNORED_MODELS")

SUBMIT_VALUE_AS = get_setting("SUBMIT_VALUE_AS")

validate_submit_value_as(SUBMIT_VALUE_AS)
