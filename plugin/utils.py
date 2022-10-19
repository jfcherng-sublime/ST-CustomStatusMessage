from typing import Any

import sublime

from .constant import PLUGIN_NAME


def get_plugin_setting(key: str, default: Any = None) -> Any:
    return get_plugin_settings().get(key, default)


def get_plugin_settings() -> sublime.Settings:
    return sublime.load_settings(f"{PLUGIN_NAME}.sublime-settings")


def is_regular_view(view: sublime.View) -> bool:
    return bool(view.is_valid() and not view.is_loading() and not view.element() and view.window())
