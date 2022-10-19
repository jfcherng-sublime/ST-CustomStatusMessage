from typing import Any, Dict

import sublime
import sublime_plugin

from .constant import PLUGIN_NAME, STATUS_MSG_KEY
from .utils import get_plugin_setting, is_regular_view


class CustomStatusMessageListener(sublime_plugin.ViewEventListener):
    def __init__(self, view: sublime.View, *args, **kwargs) -> None:
        super().__init__(view, *args, **kwargs)
        self.v_settings = view.settings()
        self.v_settings.add_on_change(PLUGIN_NAME, self._update_all_variables)

        self.variables: Dict[str, Any] = {}
        self._update_all_variables()

    def __del__(self) -> None:
        self.v_settings.clear_on_change(PLUGIN_NAME)

    def on_activated_async(self) -> None:
        self._update_variables_on_view_activated()
        self._update_status_message()

    on_post_move_async = on_activated_async

    def on_selection_modified_async(self) -> None:
        self._update_variables_on_selection_changed()
        self._update_status_message()

    def on_reload_async(self) -> None:
        self._update_all_variables()
        self._update_status_message()

    on_associate_buffer_async = on_reload_async
    on_revert_async = on_reload_async
    on_post_save_async = on_reload_async

    def _is_enabled(self, view: sublime.View) -> bool:
        return bool(get_plugin_setting("enabled") and is_regular_view(view) and len(view.sel()) == 1)

    def _update_status_message(self) -> None:
        if not self._is_enabled(self.view):
            self.view.erase_status(STATUS_MSG_KEY)
            return

        try:
            msg = str(get_plugin_setting("template")).format_map(self.variables)
        except KeyError as e:
            msg = f"[{PLUGIN_NAME}] Unknown template variable: {e}"
        except Exception as e:
            msg = f"[{PLUGIN_NAME}] Error parsing template: {e}"

        self.view.set_status(STATUS_MSG_KEY, msg)

    def _update_all_variables(self) -> None:
        self._update_variables_on_view_activated()
        self._update_variables_on_selection_changed()

    def _update_variables_on_selection_changed(self) -> None:
        point = self.view.sel()[0].b  # caret's visual position
        row_0, col_0 = self.view.rowcol(point)
        row_1, col_1 = row_0 + 1, col_0 + 1
        scope = self.view.scope_name(point).strip()

        self.variables.update(
            {
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
            }
        )

    def _update_variables_on_view_activated(self) -> None:
        buffer = self.view.buffer()
        window = self.view.window()
        assert window

        self.variables.update(
            {
                # containers
                "buffer_id": buffer.id(),
                "view_id": self.view.id(),
                "sheet_id": self.view.sheet_id(),
                "window_id": window.id(),
                # others
                "encoding": self.view.encoding(),
                "line_endings": self.view.line_endings(),
                "size": self.view.size(),
                "syntax": self.view.syntax(),
            }
        )
