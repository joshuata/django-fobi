from __future__ import absolute_import

from . import UID

from fobi.base import FormElementPluginWidget

__title__ = "fobi.contrib.plugins.form_elements.fields.datetime.widgets"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("BaseDateTimePluginWidget",)


class BaseDateTimePluginWidget(FormElementPluginWidget):
    """Base datetime form element plugin widget."""

    plugin_uid = UID
