import sublime

from .constant import STATUS_MSG_KEY
from .listener import CustomStatusMessageListener

__all__ = (
    # ST: core
    "plugin_loaded",
    "plugin_unloaded",
    # ST: listeners
    "CustomStatusMessageListener",
)


def plugin_loaded() -> None:
    pass


def plugin_unloaded() -> None:
    for window in sublime.windows():
        for view in window.views():
            view.erase_status(STATUS_MSG_KEY)
