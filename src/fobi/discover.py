# import imp
import logging
import sys

import six
# from django.conf import settings
from django.utils.module_loading import autodiscover_modules

from .conf import get_setting

logger = logging.getLogger(__file__)

__title__ = "fobi.discover"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("autodiscover",)


def autodiscover():
    """Auto-discovers files that should be found by fobi."""
    # For Python 3 we need to increase the recursion limit, otherwise things
    # break. What we want is to set the recursion limit back to its' initial
    # value after all plugins have been discovered.
    recursion_limit = 1500
    default_recursion_limit = sys.getrecursionlimit()

    if six.PY3 and recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(recursion_limit)

    FORM_ELEMENT_PLUGINS_MODULE_NAME = get_setting(
        "FORM_ELEMENT_PLUGINS_MODULE_NAME"
    )
    FORM_HANDLER_PLUGINS_MODULE_NAME = get_setting(
        "FORM_HANDLER_PLUGINS_MODULE_NAME"
    )
    THEMES_MODULE_NAME = get_setting("THEMES_MODULE_NAME")
    FORM_CALLBACKS_MODULE_NAME = get_setting("FORM_CALLBACKS_MODULE_NAME")

    INTEGRATION_FORM_ELEMENT_PLUGINS_MODULE_NAME = get_setting(
        "INTEGRATION_FORM_ELEMENT_PLUGINS_MODULE_NAME"
    )

    INTEGRATION_FORM_HANDLER_PLUGINS_MODULE_NAME = get_setting(
        "INTEGRATION_FORM_HANDLER_PLUGINS_MODULE_NAME"
    )

    FORM_IMPORTER_PLUGINS_MODULE_NAME = get_setting(
        "FORM_IMPORTER_PLUGINS_MODULE_NAME"
    )

    # Discover modules
    autodiscover_modules(FORM_ELEMENT_PLUGINS_MODULE_NAME)
    autodiscover_modules(FORM_HANDLER_PLUGINS_MODULE_NAME)
    autodiscover_modules(THEMES_MODULE_NAME)
    autodiscover_modules(FORM_CALLBACKS_MODULE_NAME)

    # Do not yet discover form importers
    autodiscover_modules(FORM_IMPORTER_PLUGINS_MODULE_NAME)

    # Do not yet discover custom field instance plugins
    autodiscover_modules(INTEGRATION_FORM_ELEMENT_PLUGINS_MODULE_NAME)
    autodiscover_modules(INTEGRATION_FORM_HANDLER_PLUGINS_MODULE_NAME)

    if six.PY3 and recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(default_recursion_limit)
