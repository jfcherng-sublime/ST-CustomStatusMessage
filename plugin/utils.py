from typing import Any, Dict

import sublime

from .constant import PLUGIN_NAME


def get_plugin_setting(key: str, default: Any = None) -> Any:
    return get_plugin_settings().get(key, default)


def get_plugin_settings() -> sublime.Settings:
    return sublime.load_settings(f"{PLUGIN_NAME}.sublime-settings")


def is_regular_view(view: sublime.View) -> bool:
    return bool(view.is_valid() and not view.is_loading() and not view.element() and view.window())


def get_template_variables(view: sublime.View, *, point: int) -> Dict[str, Any]:
    buffer = view.buffer()
    window = view.window()
    assert window

    row_0, col_0 = view.rowcol(point)
    row_1, col_1 = row_0 + 1, col_0 + 1
    scope = view.scope_name(point).strip()

    return {
        # row/col/point
        "row": row_1,
        "col": col_1,
        "row_0": row_0,
        "col_0": col_0,
        "point": point,
        # scope
        "scope": scope,
        "base_scope": scope.partition(" ")[0],
        "last_scope": scope.rpartition(" ")[2],
        # buffer/view/sheet/window
        "buffer_id": buffer.id(),
        "view_id": view.id(),
        "sheet_id": view.sheet_id(),
        "window_id": window.id(),
        # others
        "encoding": view.encoding(),
        "line_endings": view.line_endings(),
        "size": view.size(),
        "syntax": view.syntax(),
    }
